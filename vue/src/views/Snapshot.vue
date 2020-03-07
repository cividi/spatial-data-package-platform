<!-- eslint-disable -->
<i18n>
{
  "de": {
    "calltoactionText": "Angebot einholen für Ihre Gemeinde"
  },
  "fr": {
    "calltoactionText": "FR: Angebot einhohlen für Ihre Gemeinde"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div id="snapshotview">
    <v-navigation-drawer
      id="snapshotnav"
      width="320"
      clipped="clipped"
      app
      v-model="snapshotnav"
      >
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-divider />

      <div class="ma-4">
        <search :dense="true" :term="municipalityName"/>

        <div class="nodata pb-8">
          <div class="smaller hint">
            <h4>nodata title hint</h4>
            <p>no data explenation </p>
          </div>
          <div class="useractions">
            <v-btn small block outlined color="primary">
              <router-link key="signup" :to="'/' + $i18n.locale + '/signup'">
                {{ $t('calltoactionText') }}
              </router-link>
            </v-btn>
          </div>
        </div>

        <snapshot-list :snapshots="snapshotsExamples" :exclude="hash" />
      </div>

      <v-toolbar
      width="320"
      absolute
      bottom>
        <div class="useractions">
          <user-actions noRequest="1" />
        </div>
        <v-spacer/>
        <language-switch/>
      </v-toolbar>
    </v-navigation-drawer>

    <v-content>

      <v-slide-x-reverse-transition>
        <v-btn fab absolute small
          style="top:1.2em; right:2em;"
          color="primary"
          v-if="!snapshotnav"
          @click="snapshotnav=!snapshotnav">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </v-slide-x-reverse-transition>

      <v-container fluid class="pa-0">
        <div id='map'></div>
      </v-container>

      <v-btn fab absolute small
        style="bottom:2em; right:2em;"
        color="white"
        @click="mapinfoopen=!mapinfoopen">
        <v-icon  >mdi-information-variant</v-icon>
      </v-btn>

      <v-card
      id="mapinfo"
      class="px-4 py-2"
      v-bind:class="{open: mapinfoopen}"
      >
        <v-icon
          style="position: absolute; top:0; right:0;"
          class="pa-2"
          @click="mapinfoopen=!mapinfoopen" >mdi-close-circle-outline</v-icon>
        <snapshot-meta :title="title" :description="description" />
      </v-card>


    </v-content>
  </div>
</template>

<style>
#snapshotnav {
  z-index: 9999; /* must be above mapbox interface */
}
#map {
  position: relative;
  height: 100vh;
  width: 100%;
}
#mapinfo {
  position: absolute;
  bottom: 2em;
  right: 2em;
  min-width: 320px;
  clip-path: circle(0% at 95% 90%);
  transition: clip-path 0.3s ease-out;
  z-index: 10;
}

#mapinfo.open {
  clip-path: circle(100% at center);
}

#snapshotview .v-text-field--outlined fieldset {
  border-color: rgba(0, 0, 0, 0.12);
}
#snapshotview .gemeindesuche input::placeholder {
  color: #000;
  opacity: 1;
  font-weight: 900;
}
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import L from 'mapbox.js';
import geoViewport from '@mapbox/geo-viewport';
import SnapshotMeta from '../components/SnapshotMeta.vue';
import SnapshotList from '../components/SnapshotList.vue';

Vue.component('snapshot-meta', SnapshotMeta);
Vue.component('snapshot-list', SnapshotList);

function geostring2array(s) {
  const array = s.split(':')[1].split(',');
  return array.map(x => parseFloat(x));
}

export default {
  data() {
    return {
      hash: this.$route.params.hash,
      map: null,
      geojson: null,
      geobounds: [],
      layers: [],
      title: '',
      description: '',
      municipalityName: '',
      snapshotsExamples: [],
      snapshotnav: true,
      mapinfoopen: true
    };
  },

  methods: {
    async getSnapshot(hash) {
      const result = await this.$apollo.query({
        query: gql`query getsnapshot($hash: ID!){
          snapshot(id: $hash) {
            id
            pk
            data
            municipality {
              bfsNumber
              fullname
            }
          }
          snapshots(isShowcase: true) {
            edges {
              node {
                id
                pk
                title
                topic
                screenshot {
                  url
                }
              }
            }
          }
        }`,
        variables: {
          hash: btoa(`SnapshotNode:${hash}`)
        }
      });
      if (result.data.hasOwnProperty('snapshot')) {
        this.geojson = result.data.snapshot.data;
        this.municipalityName = result.data.snapshot.municipality.fullname;
      }
      this.snapshotsExamples = result.data.snapshots.edges;
    },

    async getSnapshotsExamples() {
      const result = await this.$apollo.query({
        query: gql`query getsnapshotsExamples {
          snapshots {
            edges {
              node {
                id
                pk
                title
                topic
                screenshot {
                  url
                }
              }
            }
          }
        }`
      });
      this.snapshotsExamples = result.data.snapshots.edges;
    },

    createFeatureLayer(geojson) {
      const geoJsonExtended = L.geoJson(geojson, {
        pointToLayer: (feature, latlng) => {
          if (feature.properties.radius) {
            // properties need to match https://leafletjs.com/reference-1.6.0.html#circle
            return new L.Circle(latlng, feature.properties);
          }
          return new L.Marker(latlng);
        }
      });
      return geoJsonExtended;
    },

    setupMeta() {
      this.title = this.geojson.views[0].spec.title;
      this.description = this.geojson.views[0].spec.description;
    },

    setupMapbox() {
      this.geobounds = [
        geostring2array(this.geojson.views[0].spec.bounds[0]),
        geostring2array(this.geojson.views[0].spec.bounds[1])
      ];

      const lookupResources = {}; // name -> index
      this.geojson.resources.forEach((resource, index) => {
        lookupResources[resource.name] = index;
      });

      this.geojson.views[0].resources.forEach((resourceName) => {
        this.layers.push(
          this.geojson.resources[lookupResources[resourceName]]
        );
      });
    },

    displayMapbox() {
      L.mapbox.accessToken = process.env.VUE_APP_MAPBOX_ACCESSTOKEN;
      const boxSize = 800;
      const bounds = geoViewport.viewport(this.geobounds.flat(), [boxSize, boxSize]);
      this.map = L.mapbox.map('map').setView(bounds.center, bounds.zoom);
      this.layers.forEach((layer) => {
        if (layer.mediatype === 'application/vnd.mapbox-vector-tile') {
          this.map.addLayer(L.mapbox.styleLayer(layer.path));
        } else if (layer.mediatype === 'application/geo+json') {
          this.map.addLayer(L.mapbox.featureLayer(layer.data, {
            attribution: this.geojson.views[0].spec.attribution
          }));
        } else if (layer.mediatype === 'application/vnd.simplestyle-extended') {
          this.map.addLayer(this.createFeatureLayer(layer.data.features));
        }
      });
      L.control.scale({
        metric: true,
        imperial: false
      }).addTo(this.map);
      // L.control.zoom({ position: 'bottomleft' }).addTo(this.map);
      // this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    },

    displayEmptyMapbox() {
      L.mapbox.accessToken = process.env.VUE_APP_MAPBOX_ACCESSTOKEN;
      const centerpoint = this.$route.params.municipality.centerpoint.coordinates;
      this.map = L.mapbox.map('map').setView(centerpoint, 13);
      this.map.addLayer(new L.Marker(centerpoint));
      this.map.addLayer(L.mapbox.styleLayer('mapbox://styles/gemeindescan/ck6qnoijj28od1is9u1wbb3vr'));
    }
  },

  async mounted() {
    if (this.hash) {
      await this.getSnapshot(this.hash);
    } else {
      await this.getSnapshotsExamples();
      this.displayEmptyMapbox();
    }
    if (this.geojson) {
      this.setupMeta();
      this.setupMapbox();
      this.displayMapbox();
    }
  },

  destroy() {
    this.map.destroy();
    this.map = null;
  }
};
</script>
