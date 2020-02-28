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

export default {
  data() {
    return {
      map: null,
      geojson: null
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

    displayMapbox() {
      L.mapbox.accessToken = process.env.VUE_APP_MAPBOX_ACCESSTOKEN;
      const geobounds = [
        [47.44248559830201, 9.364042282104492], [47.47730398836726, 9.41554069519043]
      ];
      const boxSize = 800;
      const bounds = geoViewport.viewport(geobounds.flat(), [boxSize, boxSize]);
      this.map = L.mapbox.map('map')
        .setView(bounds.center, bounds.zoom)
        // .addLayer(L.mapbox.featureLayer(this.geojson, {
        //   attribution: 'Data Analysis by cividi, Swisstopo'
        // }))
        .addLayer(L.rectangle(geobounds, { color: 'red', weight: 1 }))
        .addLayer(L.mapbox.styleLayer('mapbox://styles/gemeindescan/ck6qnoijj28od1is9u1wbb3vr'));
    }
  },

  async created() {
    const hash = this.$route.params.hash;
    const result = await this.getSnapshot(hash);
    this.displayMapbox();
    return result;
  },

  mounted() {
    // this.displayMapbox();
  },

  destroy() {
    this.map.destroy();
    this.map = null;
    this.geojson = null;
  }
};
</script>
