<!-- eslint-disable -->
<i18n>
{
  "de": {
  },
  "fr": {
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <v-navigation-drawer
      :width="320"
      clipped="clipped"
      app
      >
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-divider />

      <div class="ma-4">
        <search :term="municipalityName"/>
      </div>

      <div class="ma-4">
        <snapshot-meta :title="title" :description="description" />
        <snapshot-list :snapshots="snapshotsRelated" :exclude="hash"/>
      </div>

      <v-toolbar
      :width="320"
      absolute
      bottom
        class="useractions center">
        <user-actions />
      </v-toolbar>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid class="pa-0">
        <div id='map'></div>
      </v-container>
    </v-content>
  </div>
</template>

<style>
#map {
  position: relative;
  height: 100vh;
  width: 100%;
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
      geojson: {},
      geobounds: [],
      layers: [],
      title: '',
      description: '',
      municipalityName: '',
      snapshotsRelated: []
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
              snapshots {
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
      this.geojson = result.data.snapshot.data;
      this.municipalityName = result.data.snapshot.municipality.fullname;
      this.snapshotsRelated = result.data.snapshot.municipality.snapshots;
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

    displayMapbox() {
      L.mapbox.accessToken = process.env.VUE_APP_MAPBOX_ACCESSTOKEN;
      const boxSize = 800;
      const bounds = geoViewport.viewport(this.geobounds.flat(), [boxSize, boxSize]);
      this.map = L.mapbox.map('map').setView(bounds.center, bounds.zoom);
      this.layers.forEach((layer) => {
        if (layer.mediatype === 'application/vnd.mapbox-vector-tile') {
          this.map.addLayer(L.mapbox.styleLayer(layer.path));
        } else if (layer.mediatype === 'application/vnd.geo+json') {
          this.map.addLayer(L.mapbox.featureLayer(layer.data, {
            attribution: 'Data Analysis by cividi, Swisstopo'
          }));
        } else if (layer.mediatype === 'application/vnd.simplestyle-extended') {
          this.map.addLayer(this.createFeatureLayer(layer.data.features));
        }
      });
      this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    }
  },

  async created() {
    await this.getSnapshot(this.hash);
    this.setupMeta();
    this.setupMapbox();
    this.displayMapbox();
  },

  destroy() {
    this.map.destroy();
    this.map = null;
  }
};
</script>
