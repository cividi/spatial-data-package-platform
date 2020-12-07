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
        <div id="map">
          <div id="MarkerButtonsHolder" v-if="!markerSelection.includes('tooltip')">
             <div class="row">
                <div style="width: 150px;">
                  <h6 v-if ="!addMarkerMode">Select a <br> marker or Post-it:</h6>
                  <h6 v-else>Click on the map <br> to set the marker</h6>
                </div>
                <div style="width: 50px;">
                  <button v-if ="!addMarkerMode || markerSelection == 'thumbs-up'"
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'thumbs-up'">
                     <v-icon large color="green" > mdi-thumb-up </v-icon>
                  </button>
                  <button v-else
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'thumbs-up'">
                     <v-icon large color="green" style='opacity:0.1'> mdi-thumb-up </v-icon>
                  </button>
                </div>
                <div style="width: 50px;">
                  <button v-if ="!addMarkerMode || markerSelection == 'thumbs-down'"
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'thumbs-down'">
                    <v-icon large color="red" > mdi-thumb-down </v-icon>
                  </button>
                  <button v-else
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'thumbs-down'">
                    <v-icon large color="red" style='opacity:0.1'> mdi-thumb-down </v-icon>
                  </button>
                </div>
                <div style="width: 50px;">
                  <button v-if ="!addMarkerMode"
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'tooltip-text-green'">
                    <v-icon large color="green" > mdi-tooltip-text </v-icon>
                  </button>
                  <button v-else
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'tooltip-text-green'">
                    <v-icon large color="green" style='opacity:0.1'> mdi-tooltip-text </v-icon>
                  </button>
                </div>
                <div style="width: 50px;">
                  <button v-if ="!addMarkerMode"
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'tooltip-text-blue'" >
                    <v-icon large color="blue" > mdi-tooltip-text </v-icon>
                  </button>
                  <button v-else
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'tooltip-text-blue'" >
                    <v-icon large color="blue" style='opacity:0.1'> mdi-tooltip-text </v-icon>
                  </button>
                </div>
                <div style="width: 50px;">
                  <button v-if ="!addMarkerMode"
                     id="ButtonStartMarker"
                     v-on:click="addMarkerMode = !addMarkerMode;
                     markerSelection = 'tooltip-text-yellow'">
                    <v-icon large color="yellow" > mdi-tooltip-text </v-icon>
                  </button>
                  <button v-else
                     id="ButtonStartMarker"
                     v-on:click="addMarkerMode = !addMarkerMode;
                     markerSelection = 'tooltip-text-yellow'">
                    <v-icon large color="yellow" style='opacity:0.1'> mdi-tooltip-text </v-icon>
                  </button>
                </div>
              </div>
          </div>
          <div id="PostitNaming" v-if="addMarkerMode
                  && markerSelection.includes('tooltip')">
            <div class="row">
              <div class="column" style="width: 150px;">
                <h6> Enter node & <br>click on the map.</h6>
              </div>
              <div v-if="markerSelection == 'tooltip-text-green'"
              class="column" style="width: 50px;">
                <v-icon large color="green" > mdi-tooltip-text </v-icon>
              </div>
              <div v-if="markerSelection == 'tooltip-text-blue'"
              class="column" style="width: 50px;">
                <v-icon large color="blue" > mdi-tooltip-text </v-icon>
              </div>
              <div v-if="markerSelection == 'tooltip-text-yellow'"
              class="column" style="width: 50px;">
                <v-icon large color="yellow" > mdi-tooltip-text </v-icon>
              </div>
              <div class="column" style="width: 150px; font-size: 1.4em">
                <input id="InputMarkerName"  v-model="newPostItNode"
                    placeholder="Enter your Post-it note here"
                >
              </div>
            </div>
          </div>
        </div>
        <span id="mapstatus" :class="{ loaded: isMapLoaded, waiting: !isMapLoaded }"></span>
      </v-container>

      <v-btn
        v-if="hash && !screenshotIsThumbnail"
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

#map .mapbox-improve-map {
  display: none;
}

#mapinfo {
  position: absolute;
  bottom: 2em;
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

.mapbox-improve-map {
  display: none;
}

#MarkerButtonsHolder {
  position: relative;
  margin: auto;
  top: 5px;
  width: 400px;
  height: 40px;
  border-radius: 20px;
  background-color: hsla(0, 0%, 100%, 0.356);
  text-align: right;
  z-index: 300;
}
#PostitNaming {
  position: relative;
  margin: auto;
  top: 5px;
  width: 400px;
  height: 40px;
  border-radius: 20px;
  background-color: hsla(0, 0%, 100%, 0.356);
  text-align: right;
  z-index: 300;
}
.leaflet-tooltip-yellow{
  font-size: medium;
  background-color: rgb(255, 230, 6);
}
.leaflet-tooltip-green{
  font-size: small;
  color: rgb(255, 255, 255);
  background-color: rgb(25, 158, 21);
}
.leaflet-tooltip-blue{
  font-size: small;
  color: rgb(255, 255, 255);
  background-color: rgb(37, 24, 230);
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
      isMapLoaded: false,
      addMarkerMode: false,
      newPostItNode: '',
      markerSelection: '',
      markers: [],
      markerLocalStorage: []
    };
  },

  props: {
    snapshot: Object,
    geojson: Object,
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

  async mounted() {
    if (localStorage.getItem('PostIts')) {
      try {
        this.markerLocalStorage = JSON.parse(localStorage.getItem('PostIts'));
      } catch (err) {
        localStorage.removeItem('PostIts');
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
        if (process.env.VUE_APP_MAPBOX_DEFAULT_STYLES) {
          this.layerContainer.addLayer(L.mapbox.styleLayer(
            process.env.VUE_APP_MAPBOX_DEFAULT_STYLES
          ));
        }
      }
      this.layerContainer.addTo(this.map);
      L.control.scale({
        metric: true,
        imperial: false
      }).addTo(this.map);

      for (let x = 0; x < this.markerLocalStorage.length; x += 1) {
        this.markerSelection = this.markerLocalStorage[x].markerSelection;
        this.newPostItNode = this.markerLocalStorage[x].newPostItNode;
        this.setMarker(this.markerLocalStorage[x].markerGeoCoordinates);
      }

      this.map.on('click', (event) => {
        if (event.containerPoint.y >= 50) {
          if (this.addMarkerMode) {
            const markerGeoCoordinates = event.latlng;
            const markerInfoToStore = {
              markerSelection: this.markerSelection,
              newPostItNode: this.newPostItNode,
              markerGeoCoordinates
            };
            this.markerLocalStorage.push(markerInfoToStore);
            this.saveMarkerLocalStorage();
            this.setMarker(markerGeoCoordinates);
          }
        }
      });

      if (this.screenshotMode) {
        // no zoom controls in screenshot mode
        document.querySelector('.leaflet-control-zoom').style.display = 'none';
      } else {
        // no attribution in normal mode
        document.querySelector('.leaflet-control-attribution').style.display = 'none';
      }
      if (this.screenshotIsThumbnail) {
        document.querySelector('#mapinfo').style.visibility = 'hidden';
      }
      // L.control.zoom({ position: 'bottomleft' }).addTo(this.map);
      // this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    },

    setMarker(markerGeoCoordinates) {
      if (this.markerSelection === 'thumbs-up') {
        const thumbUp = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0V0z"/><path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z" fill="green"/></svg>';
        this.newMarker = L.marker(markerGeoCoordinates, {
          icon: L.icon({
            iconUrl: encodeURI(`data:image/svg+xml,${thumbUp}`),
            iconSize: [30, 30]
          })
        });
      } else if (this.markerSelection === 'thumbs-down') {
        const thumbDown = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="24" height="24" viewBox="0 0 24 24"><path d="M19,15H23V3H19M15,3H6C5.17,3 4.46,3.5 4.16,4.22L1.14,11.27C1.05,11.5 1,11.74 1,12V14A2,2 0 0,0 3,16H9.31L8.36,20.57C8.34,20.67 8.33,20.77 8.33,20.88C8.33,21.3 8.5,21.67 8.77,21.94L9.83,23L16.41,16.41C16.78,16.05 17,15.55 17,15V5C17,3.89 16.1,3 15,3Z" fill="red"/></svg>';
        this.newMarker = L.marker(markerGeoCoordinates, {
          icon: L.icon({
            iconUrl: encodeURI(`data:image/svg+xml,${thumbDown}`),
            iconSize: [30, 30]
          })
        });
      } else if (this.markerSelection.includes('tooltip')) {
        this.newMarker = L.marker(markerGeoCoordinates, {
          icon: L.icon({
            iconUrl: 'my-icon.png',
            iconSize: [0, 0]
          })
        });
        if (this.markerSelection === 'tooltip-text-green') {
          this.newMarker.bindTooltip(this.newPostItNode, {
            permanent: true,
            interactive: true,
            className: 'leaflet-tooltip-green'
          });
        } else if (this.markerSelection === 'tooltip-text-yellow') {
          this.newMarker.bindTooltip(this.newPostItNode, {
            permanent: true,
            interactive: true,
            className: 'leaflet-tooltip-yellow'
          });
        } else if (this.markerSelection === 'tooltip-text-blue') {
          this.newMarker.bindTooltip(this.newPostItNode, {
            permanent: true,
            interactive: true,
            className: 'leaflet-tooltip-blue'
          });
        }
      }
      this.newMarker.on('contextmenu', this.deleteMarker, this);
      this.newMarker.addTo(this.map);
      this.markers.push(this.newMarker);
      this.addMarkerMode = false;
      this.newPostItNode = '';
      this.markerSelection = '';
    },

    deleteMarker(event) {
      for (let x = 0; x < this.markers.length; x += 1) {
        if (event.latlng === this.markers[x].getLatLng()) {
          this.map.removeLayer(this.markers[x]);
        }
      }
    },

    saveMarkerLocalStorage() {
      const parsed = JSON.stringify(this.markerLocalStorage);
      localStorage.setItem('PostIts', parsed);
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
