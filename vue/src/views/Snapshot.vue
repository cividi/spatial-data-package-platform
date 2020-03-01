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
  <v-container>
    <v-navigation-drawer
      :width="320"
      left app >
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-toolbar
      :width="320"
      absolute
      bottom
        class="useractions center">
        <user-actions />
      </v-toolbar>
    </v-navigation-drawer>

    <v-layout >
      <v-flex>
        <div id='map'></div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style>
#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}
</style>

<script>
import gql from 'graphql-tag';
import L from 'mapbox.js';
import geoViewport from '@mapbox/geo-viewport';

function geostring2array(s) {
  const array = s.split(':')[1].split(',');
  return array.map(x => parseFloat(x)).reverse();
}

export default {
  data() {
    return {
      map: null,
      geojson: {},
      geobounds: [],
      layers: []
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
          }
        }`,
        variables: {
          hash: btoa(`SnapshotNode:${hash}`)
        }
      });
      this.geojson = result.data.snapshot.data;
    },

    setupMapbox() {
      this.geobounds = [
        geostring2array(this.geojson.views[0].bounds[0]),
        geostring2array(this.geojson.views[0].bounds[1])
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
      console.log(this.geobounds.flat());
      const bounds = geoViewport.viewport(this.geobounds.flat(), [boxSize, boxSize]);
      this.map = L.mapbox.map('map').setView(bounds.center, bounds.zoom);
      this.layers.forEach((layer) => {
        if (layer.mediatype === 'application/vnd.mapbox-vector-tile') {
          this.map.addLayer(L.mapbox.styleLayer(layer.path));
        } else if (layer.mediatype === 'application/vnd.geo+json') {
          this.map.addLayer(L.mapbox.featureLayer(layer.data, {
            attribution: 'Data Analysis by cividi, Swisstopo'
          }));
        }
      });
      this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    }
  },

  async created() {
    const hash = this.$route.params.hash;
    const result = await this.getSnapshot(hash);
    this.setupMapbox();
    this.displayMapbox();
    return result;
  },

  destroy() {
    this.map.destroy();
    this.map = null;
    this.geojson = null;
    this.geobounds = [];
    this.layers = null;
  }
};
</script>
