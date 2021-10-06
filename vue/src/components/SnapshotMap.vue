<template>
    <v-main>
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
        <span id="mapstatus" :class="{ loaded: isMapLoaded, waiting: !isMapLoaded }"></span>
      </v-container>

      <v-btn
        v-if="hash && !screenshotIsThumbnail"
        fab absolute small
        style="bottom:2.5em; right:2em;"
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
          v-show="!screenshotMode"
          style="position: absolute; top:0; right:0;"
          class="pa-2"
          @click="mapinfoopen=!mapinfoopen" >mdi-close-circle-outline
        </v-icon>
        <snapshot-meta
          :title="title"
          :description="description"
          :predecessor="predecessor"
          :hash="hash"
          :legend="legend"
          :sources="sources"
        />
      </v-card>
    </v-main>
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
    overflow: hidden;
    background: #dedede
        linear-gradient(90deg, #dedede 0%, #f2f2f2 17%, #dedede 23%) repeat-y;
    background-size: 125% 10%;
    animation: BGani 2s ease infinite;
}

@keyframes BGani {
    0% {
        background-position: 110% 0%;
    }
    66% {
        background-position: -410% 0%;
    }
    100% {
        background-position: -410% 0%;
    }
}
#map.leaflet-container {
    background: #dedede;
    animation: none;
}
.leaflet-popup-content img{
  max-width: 100%;
  min-width: 280px;
}

#mapinfo {
    position: absolute;
    bottom: 2.5em;
    right: 2em;
    min-width: 240px;
    clip-path: circle(0% at 95% 90%);
    transition: clip-path 0.3s ease-out;
    pointer-events: none;
    z-index: 500; /* must be above mapbox icons */
}

#mapinfo.open {
    pointer-events: auto;
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
      geobounds: [],
      screenshotMode: this.$route.query.hasOwnProperty('screenshot'),
      screenshotIsThumbnail: this.$route.query.hasOwnProperty('thumbnail'),
      isMapLoaded: false
    };
  },

  props: {
    snapshot: Object,
    geojson: Object,
    annotations: Array,
    geoboundsIn: Array,
    predecessor: Object
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
          feature.properties.interactive = false;

          if (feature.properties.title || feature.properties.description) {
            feature.properties.className = 'popup-title-description';
            feature.properties.interactive = true;
          }

          let curfeature;
          if (feature.properties.radius) {
            // properties need to match https://leafletjs.com/reference-1.6.0.html#circle
            curfeature = new L.Circle(latlng, feature.properties);
          } else {
            const options = {};
            if (feature.properties.icon) {
              options.icon = new L.Icon(feature.properties.icon);
            }
            curfeature = new L.Marker(latlng, options);
          }
          if (feature.properties.interactive) {
            curfeature.on('click', this.showTitleDescPopup);
          }
          return curfeature;
        }
      });
      return geoJsonExtended;
    },

    showTitleDescPopup(e) {
      console.log(e.target);
      let content = e.target.feature.properties.description;
      if (e.target.feature.properties.title) {
        content = `<b>${e.target.feature.properties.title}</b><br />${content}`;
      }
      new L.Popup()
        .setLatLng(e.target._latlng) // eslint-disable-line no-underscore-dangle
        .setContent(content)
        .openOn(this.map);
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
      try {
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
      } catch (error) {
        console.log(error); // eslint-disable-line no-console
        this.isMapLoaded = true;
      }
    },

    displayMapbox() {
      try {
        L.mapbox.accessToken = process.env.VUE_APP_MAPBOX_ACCESSTOKEN
          || process.env.VUE_APP_MAPBOX_ACCESSTOKEN_DEV;
        const boxSize = 800;
        const bounds = geoViewport.viewport(this.geobounds.flat(), [boxSize, boxSize]);
        this.map = L.mapbox.map('map').setView(bounds.center, bounds.zoom);
        this.layerContainer = new L.LayerGroup();
        // default test layer // this.layerContainer.addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/light-v10'));
        if (this.hash) { // full snapshot with hash
          this.layers.forEach((layer) => {
            if (layer.mediatype === 'application/vnd.mapbox-vector-tile') {
              const tileLayer = L.mapbox.styleLayer(layer.path);
              tileLayer.on('load', () => { this.isMapLoaded = true; });
              this.layerContainer.addLayer(tileLayer);
            } else if (layer.mediatype === 'application/geo+json') {
              this.layerContainer.addLayer(L.mapbox.featureLayer(layer.data, {
                attribution: this.geojson.views[0].spec.attribution
              }));
            } else if (layer.mediatype === 'application/vnd.simplestyle-extended') {
              this.layerContainer.addLayer(this.createFeatureLayer(
                layer.data.features, this.geojson.views[0].spec.attribution
              ));
            } else if (layer.mediatype === 'application/vnd.wms') {
              const tileLayer = L.tileLayer.wms(layer.path, layer.parameters);
              this.layerContainer.addLayer(tileLayer);
            }
          });
        } else if (this.bfsNumber) { // empty municipality
          this.geojson.coordinates.forEach((polygon) => {
            this.layerContainer.addLayer(L.polygon(polygon, { color: '#543076' }));
          });
          const DEFAULT_STYLES = process.env.VUE_APP_MAPBOX_DEFAULT_STYLES
            || process.env.VUE_APP_MAPBOX_DEFAULT_STYLES_DEV;
          if (DEFAULT_STYLES) {
            this.layerContainer.addLayer(L.mapbox.styleLayer(DEFAULT_STYLES));
          }
        }
        if (this.annotations) {
          this.annotations = this.annotations.map((a) => {
            if (a.category.length === 1) {
              a.data.properties.icon = { iconUrl: `/media/${a.category[0].icon}` };
            }
            if (a.attachements.length > 0) {
              const imgs = [];
              a.attachements.map((d) => {
                imgs.push(`<a href="/media/${d.document}" target="_blank"><img src="/media/${d.document}"></a>`);
                return d;
              });
              a.data.properties.description = imgs.join() + a.data.properties.description;
            }
            return a;
          });
          const annotationsdata = this.annotations.map(a => a.data);
          console.log(annotationsdata);
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata, ''
          ));
        }
        this.layerContainer.addTo(this.map);
        L.control.scale({
          metric: true,
          imperial: false
        }).addTo(this.map);

        if (this.screenshotMode) {
          // no zoom controls in screenshot mode
          document.querySelector('.leaflet-control-zoom').style.display = 'none';
          document.querySelector('.leaflet-control-attribution').style.display = 'none';
        } else if (this.hash) {
          // no attribution in normal mode
          document.querySelector('.leaflet-control-attribution').style.background = 'none';
        }
        if (this.screenshotIsThumbnail) {
          document.querySelector('#mapinfo').style.visibility = 'hidden';
        }
      } catch (error) {
        console.log(error); // eslint-disable-line no-console
        this.isMapLoaded = true;
      }
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
      this.isMapLoaded = false;
    }
  }
};
</script>
