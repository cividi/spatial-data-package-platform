<template>
    <v-content>
      <v-slide-x-reverse-transition>
        <v-btn fab absolute small
          style="top:1.2em; right:1.3em;"
          color="primary"
          v-if="!snapshotnav"
          @click="snapshotnav=!snapshotnav">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </v-slide-x-reverse-transition>

      <v-container fluid class="pa-0" ref="mapbox">
        <div id="map"></div>
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
        <snapshot-meta
          :title="title"
          :description="description"
          :hash="hash"
          :legend="legend"
          :sources="sources"
        />
      </v-card>
    </v-content>
</template>

<style>
html,
body,
#app .v-application--wrap,
#map {
  min-height: calc(100vh - var(--vh-offset, 0px));
  height: calc(100vh - var(--vh-offset, 0px));
}

#map {
  position: relative;
  width: 100%;
}

#mapinfo {
  position: absolute;
  bottom: 2em;
  right: 2em;
  min-width: 240px;
  clip-path: circle(0% at 95% 90%);
  transition: clip-path 0.3s ease-out;
  z-index: 1000; /* must be above mapbox icons */
}

#mapinfo.open {
  clip-path: circle(100% at center);
}
</style>

<script>
import Vue from 'vue';
import L from 'mapbox.js';
import geoViewport from '@mapbox/geo-viewport';
import SnapshotMeta from './SnapshotMeta.vue';

Vue.component('snapshot-meta', SnapshotMeta);

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
      layerContainer: null,
      mapinfoopen: true,
      title: '',
      description: '',
      legend: [],
      sources: [],
      layers: [],
      geobounds: []
    };
  },

  props: {
    geojson: Object,
    geoboundsIn: Array
  },

  created() {
    this.geobounds = this.geoboundsIn;
  },

  destroy() {
    this.destroyMap();
  },

  computed: {
    legendWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return '280px';
        default: return '320px';
      }
    },

    snapshotnav: {
      get() {
        return this.$store.state.snapshotnav;
      },
      set(val) {
        this.$store.commit('setSnapshotnav', val);
      }
    }
  },

  methods: {
    createFeatureLayer(geojson, attribution) {
      const geoJsonExtended = L.geoJson(geojson, {
        attribution,
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

    setupEmpty() {
      this.geobounds = this.geoboundsIn;
    },

    setupMeta() {
      this.title = this.geojson.views[0].spec.title;
      this.description = this.geojson.views[0].spec.description;
      this.legend = this.geojson.views[0].spec.legend;
      this.sources = this.geojson.sources;
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
      this.layerContainer = new L.LayerGroup();
      if (this.hash) { // full snapshot with hash
        this.layers.forEach((layer) => {
          if (layer.mediatype === 'application/vnd.mapbox-vector-tile') {
            this.layerContainer.addLayer(L.mapbox.styleLayer(layer.path));
          } else if (layer.mediatype === 'application/geo+json') {
            this.layerContainer.addLayer(L.mapbox.featureLayer(layer.data, {
              attribution: this.geojson.views[0].spec.attribution
            }));
          } else if (layer.mediatype === 'application/vnd.simplestyle-extended') {
            this.layerContainer.addLayer(this.createFeatureLayer(
              layer.data.features, this.geojson.views[0].spec.attribution
            ));
          }
        });
      } else if (this.bfsNumber) { // empty municipality
        this.geojson.coordinates.forEach((polygon) => {
          this.layerContainer.addLayer(L.polygon(polygon, { color: '#543076' }));
        });
        this.layerContainer.addLayer(L.mapbox.styleLayer('mapbox://styles/gemeindescan/ck6rp249516tg1iqkmt48o4pz'));
      }
      this.layerContainer.addTo(this.map);
      L.control.scale({
        metric: true,
        imperial: false
      }).addTo(this.map);
      // L.control.zoom({ position: 'bottomleft' }).addTo(this.map);
      // this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    },

    async destroyMap() {
      this.layerContainer.clearLayers();
      this.map.eachLayer((layer) => {
        this.map.removeLayer(layer);
      });
      try {
        await this.map.remove();
      } catch (err) {
        // catch remove erros
      }
      this.hash = this.$route.params.hash;
      this.bfsNumber = this.$route.params.bfsNumber;
      this.layerContainer = null;
      this.mapinfoopen = true;
      this.title = '';
      this.description = '';
      this.legend = [];
      this.sources = [];
      this.layers = [];
      this.geobounds = [];
      this.map = null;
    }
  }
};
</script>
