<!-- eslint-disable -->
<i18n>
{
  "de": {
    "calltoactionText": "Angebot für {municipalityText} einholen",
    "hasSnapshot.title": "Datenverfügbarkeit",
    "hasSnapshot.p1": "Für {municipalityText} stehen erste Daten zur Verfügung.",
    "hasSnapshot.p2": "Erkunden Sie unsere weiteren Fallbeispiele um ein besseres Bild der Anwendungs-möglichkeiten für Ihre Gemeinde zu erhalten.",
    "noSnapshot.title": "Datenverfügbarkeit",
    "noSnapshot.municipalityText": "diese Gemeinde",
    "noSnapshot.p1": "Für {municipalityText} stehen zur Zeit noch keine Daten zur Verfügung.",
    "noSnapshot.p2": "Erkunden Sie unsere Fallbeispiele um ein besseres Bild der Möglichkeiten für Ihre Gemeinde zu erhalten."
  },
  "fr": {
    "calltoactionText": "Veuillez recueillir l’offre pour votre commune",
    "hasSnapshot.title": "Disponibilité des données",
    "hasSnapshot.p1": "Les premières données concernants {municipalityText} sont disponibles.",
    "hasSnapshot.p2": "Prenez compte de nos études pour une meilleure vue d’ensemble des possibilitiées qui s’offrent à votre commune.",
    "noSnapshot.title": "Disponibilité des données",
    "noSnapshot.municipalityText": "cette communauté",
    "noSnapshot.p1": "En ce moment il n’éxiste pas encore de données pour {municipalityText}.",
    "noSnapshot.p2": "Prenez compte de nos études pour une meilleure vue d’ensemble des possibilitiées qui s’offrent à votre commune."
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div id="snapshotview">
    <v-navigation-drawer
      v-if="$store.state.notIframe"
      id="snapshotnav"
      clipped="clipped"
      app
      width="320"
      v-model="snapshotnav"
      >
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-divider />

      <div class="ma-4">
        <search :dense="true" :term="municipalityName"/>

        <div class="nodata pb-8">
          <div v-if="hash" class="smaller hint">
            <h4>{{ $t('hasSnapshot.title') }}</h4>
            <p>{{ $t('hasSnapshot.p1', { municipalityText: municipalityText }) }}</p>
            <p>{{ $t('hasSnapshot.p2') }}</p>
          </div>
          <div v-else class="smaller hint">
            <h4>{{ $t('noSnapshot.title') }}</h4>
            <p>{{ $t('noSnapshot.p1', { municipalityText: municipalityText }) }}</p>
            <p>{{ $t('noSnapshot.p2') }}</p>
          </div>
          <div class="useractions">
            <v-btn small block outlined color="primary">
              <router-link key="signup" :to="'/' + $i18n.locale + '/signup/'">
                {{ $t('calltoactionText', { municipalityText: municipalityText }) }}
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

      <v-btn
        v-if="hash"
        fab absolute small
        style="bottom:2em; right:2em;"
        color="white"
        @click="mapinfoopen=!mapinfoopen">
        <v-icon>mdi-information-variant</v-icon>
      </v-btn>

      <v-card
        v-if="hash"
        id="mapinfo"
        class="px-4 py-2"
        :style="'width:' + legendWidth"
        v-bind:class="{open: mapinfoopen}"
      >
        <v-icon
          style="position: absolute; top:0; right:0;"
          class="pa-2"
          @click="mapinfoopen=!mapinfoopen" >mdi-close-circle-outline</v-icon>
        <snapshot-meta :title="title" :description="description" :hash="hash" :legend="legend" />
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
  min-width: 240px;
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
      bfsNumber: this.$route.params.bfsNumber,
      map: null,
      geojson: null,
      geobounds: [],
      layers: [],
      title: '',
      description: '',
      legend: [],
      municipalityName: '',
      snapshotsExamples: [],
      snapshotnav: true,
      mapinfoopen: true
    };
  },

  computed: {
    municipality() {
      if (this.$route.params.hasOwnProperty('municipality') && this.$route.params.municipality) {
        return this.$route.params.municipality;
      }
      return null;
    },

    municipalityText() {
      return this.municipalityName ? this.municipalityName : this.$t('noSnapshot.municipalityText');
    },

    legendWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return '280px';
        default: return '320px';
      }
    }
  },

  methods: {
    async getSnapshot(hash) {
      const result = await this.$apollo.query({
        query: gql`query getsnapshot($hash: ID!) {
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
      if (result.data.hasOwnProperty('snapshot') && result.data.snapshot) {
        this.geojson = result.data.snapshot.data;
        this.municipalityName = result.data.snapshot.municipality.fullname;
      } else {
        this.$router.push({ name: 'home' });
      }
      this.snapshotsExamples = result.data.snapshots.edges;
      this.$store.commit('setBfsnumber', result.data.snapshot.municipality.bfsNumber);
      this.$store.commit('setBfsname', result.data.snapshot.municipality.fullname);
    },

    async getEmpty(bfsNumber) {
      const result = await this.$apollo.query({
        query: gql`query getmunicipality($bfsNumber: ID!) {
          municipality(id: $bfsNumber) {
            id
            bfsNumber
            fullname
            perimeter
            perimeterBounds
          }
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
        }`,
        variables: {
          bfsNumber: btoa(`MunicipalityNode:${bfsNumber}`)
        }
      });
      this.municipalityName = result.data.municipality.fullname;
      this.geojson = result.data.municipality.perimeter;
      this.geobounds = result.data.municipality.perimeterBounds;
      this.snapshotsExamples = result.data.snapshots.edges;
      this.$store.commit('setBfsnumber', result.data.snapshot.bfsNumber);
      this.$store.commit('setBfsname', result.data.snapshot.fullname);
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
      this.legend = this.geojson.views[0].spec.legend;
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
      if (this.hash) { // full snapshot with hash
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
      } else if (this.bfsNumber) { // empty municipality
        this.geojson.coordinates.forEach((polygon) => {
          this.map.addLayer(L.polygon(polygon));
        });
        this.map.addLayer(L.mapbox.styleLayer('mapbox://styles/gemeindescan/ck6qnoijj28od1is9u1wbb3vr'));
      }
      L.control.scale({
        metric: true,
        imperial: false
      }).addTo(this.map);
      // L.control.zoom({ position: 'bottomleft' }).addTo(this.map);
      // this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    }
  },

  async mounted() {
    if (this.hash) {
      await this.getSnapshot(this.hash);
      if (this.geojson) {
        this.setupMeta();
        this.setupMapbox();
        this.displayMapbox();
      }
    } else {
      await this.getEmpty(this.bfsNumber);
      this.displayMapbox();
    }
  },

  destroy() {
    this.map.destroy();
    this.map = null;
  }
};
</script>
