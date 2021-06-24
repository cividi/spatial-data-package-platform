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
      <v-main class="pa-0" ref="mapbox">
      <div
        id="MarkerButtons"
        style="position: absolute; top: 6em; right: 1.8em; z-index: 500"
      >
        <button
          style="background-color: #543076; border-radius: 50px"
          v-on:click="markerTools=!markerTools"
        >
          <v-icon large color="white"> mdi-brush </v-icon>
        </button>
        <v-card v-if="markerTools" style="position:absolute: ;width: 36px">
          <button v-on:click="toggelMarkerSelection('marker')">
            <v-icon large color="black"> mdi-map-marker </v-icon>
          </button>
          <button v-on:click="toggelMarkerSelection('polygon')">
            <v-icon large color="black"> mdi-vector-polygon </v-icon>
          </button>
          <button v-on:click="toggelMarkerSelection('note')">
            <v-icon large color="black"> mdi-note-outline </v-icon>
          </button>
          <button v-on:click="toggelMarkerSelection('');
          markerTools = !markerTools" v-if="!hideMarker">
            <v-icon large color="black"> mdi-eye-off </v-icon>
          </button>
          <button v-on:click="toggelMarkerSelection('');
          markerTools = !markerTools" v-if="hideMarker">
            <v-icon large color="black"> mdi-eye </v-icon>
          </button>
        </v-card>
        <div v-if="markerTools" >
          <v-card v-if="markerSelection == 'marker'"
          style="position:absolute; top:3.8em; right:3.7em; min-width:16em"
          color="rgba(255, 255, 255, 0.7)"
          >Klicken Sie auf die Karte, um eine Markierung zu platzieren </v-card>
          <v-card v-if="markerSelection == 'polygon' && !paintNow"
          style="position:absolute; top:7.5em; right:3.7em; min-width:16em"
          color="rgba(255, 255, 255, 0.7)"
          >Klicken Sie auf die Karte, um ein Polygon zu beginnen </v-card>
          <v-card v-if="markerSelection == 'polygon' && paintNow"
          style="position:absolute; top:7.5em; right:3.7em; min-width:16em"
          color="rgba(255, 255, 255, 0.7)"
          >Klicken Sie erneut, um das Polygon zu beenden </v-card>
          <v-card v-if="markerSelection == 'note'"
          style="position:absolute; top:11.3em; right:3.7em; min-width:16em"
          color="rgba(255, 255, 255, 0.7)"
          >Klicken Sie auf die Karte, um die Post-it zu setzten </v-card>
        </div>
      </div>
    </v-main>
      <v-main fluid class="pa-0" ref="mapbox">
        <div id="map" v-bind:style="{ cursor: computedCursor }">
          <div id="MarkerButtonsHolder"
            v-if="!markerSelection.includes('tooltip') && !screenshotMode && false">
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
                  <button v-if ="!addMarkerMode || markerSelection == 'brush'"
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'brush'">
                    <v-icon large color="blue" > mdi-brush </v-icon>
                  </button>
                  <button v-else
                     v-on:click="addMarkerMode = !addMarkerMode;
                      markerSelection = 'brush'">
                    <v-icon large color="blue" style='opacity:0.1'> mdi-brush </v-icon>
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
                     v-on:click="addMarkerMode = !addMarkerMode;
                     markerSelection = 'tooltip-text-yellow'">
                    <v-icon large color="yellow" > mdi-tooltip-text </v-icon>
                  </button>
                  <button v-else
                     v-on:click="addMarkerMode = !addMarkerMode;
                     markerSelection = 'tooltip-text-yellow'">
                    <v-icon large color="yellow" style='opacity:0.1'> mdi-tooltip-text </v-icon>
                  </button>
                </div>
                <div style="width: 50px;" v-if ="!addMarkerMode">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-icon large
                      v-on="on"
                      v-on:click="deleteAllMarkers();"
                      > mdi-delete-forever
                      </v-icon>
                    </template>
                    <span>Click to delete all markers</span>
                  </v-tooltip>
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
              class="column" style="width: 50px;"
              v-on:click="addMarkerMode = !addMarkerMode;
              markerSelection = ''">
                <v-icon large color="green" > mdi-tooltip-text </v-icon>
              </div>
              <div v-if="markerSelection == 'tooltip-text-blue'"
              class="column" style="width: 50px;"
              v-on:click="addMarkerMode = !addMarkerMode;
              markerSelection = ''">
                <v-icon large color="blue" > mdi-tooltip-text </v-icon>
              </div>
              <div v-if="markerSelection == 'tooltip-text-yellow'"
              class="column" style="width: 50px;"
              v-on:click="addMarkerMode = !addMarkerMode;
              markerSelection = ''">
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
      </v-main>

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
  width: 500px;
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
.leaflet-tooltip {
  font-size: small;
  background-color: rgb(255, 230, 6);
}
.leaflet-tooltip-yellow {
  font-size: small;
  background-color: rgb(255, 230, 6);
}
.leaflet-tooltip-green {
  font-size: small;
  color: rgb(255, 255, 255);
  background-color: rgb(25, 158, 21);
}
.leaflet-tooltip-blue {
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
      markerLocalStorage: [],
      markerTools: false,
      hideMarker: false,
      editMode: false,
      cursorType: '',
      popupForm: '',
      paintNow: false
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
    computedCursor() {
      return this.cursorType;
    },
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
    changeCursor() {
      if (this.paintNow) {
        this.cursorType = 'pointer';
      }
      if (this.markerSelection === 'marker') {
        this.cursorType = 'url("data:image/svg+xml,<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z\' /></svg>"), pointer';
      } else if (this.markerSelection === 'note') {
        this.cursorType = 'url("data:image/svg+xml,<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M14,10H19.5L14,4.5V10M5,3H15L21,9V19A2,2 0 0,1 19,21H5C3.89,21 3,20.1 3,19V5C3,3.89 3.89,3 5,3M5,5V19H19V12H12V5H5Z\' /></svg>"), pointer';
      } else if (this.markerSelection === 'polygon') {
        this.cursorType = 'url("data:image/svg+xml,<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M2,2V8H4.28L5.57,16H4V22H10V20.06L15,20.05V22H21V16H19.17L20,9H22V3H16V6.53L14.8,8H9.59L8,5.82V2M4,4H6V6H4M18,5H20V7H18M6.31,8H7.11L9,10.59V14H15V10.91L16.57,9H18L17.16,16H15V18.06H10V16H7.6M11,10H13V12H11M6,18H8V20H6M17,18H19V20H17\' /></svg>"), pointer';
      } else { this.cursorType = 'auto'; }
    },
    toggelMarkerSelection(newMode) {
      if (this.markerSelection !== newMode) {
        this.markerSelection = newMode;
      } else { this.markerSelection = ''; }
      this.changeCursor();
    },
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
        this.layerContainer.addTo(this.map);
        L.control.scale({
          metric: true,
          imperial: false
        }).addTo(this.map);

        if (!this.screenshotMode) {
          for (let x = 0; x < this.markerLocalStorage.length; x += 1) {
            this.markerSelection = this.markerLocalStorage[x].markerSelection;
            this.newPostItNode = this.markerLocalStorage[x].newPostItNode;
            this.setMarker(this.markerLocalStorage[x].markerGeoCoordinates);
          }
        }

        this.myPolyline = [];
        this.map.on('click', (event) => {
          if (this.markerTools) {
            if (this.markerSelection === 'marker') {
              this.markerTools = false;
              this.toggelMarkerSelection('');
              const markerGeoCoordinates = event.latlng;
              const markerSVG = '<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z\' /></svg>';
              this.newMarker = L.marker(markerGeoCoordinates, {
                icon: L.icon({
                  iconUrl: encodeURI(`data:image/svg+xml,${markerSVG}`),
                  iconSize: [30, 30]
                })
              });
              this.newMarker.on('contextmenu', this.deleteMarker, this);
              this.newMarker.on('click', this.editMarker, this);
              this.newMarker.addTo(this.map);
              this.markers.push(this.newMarker);
            }
            if (this.markerSelection === 'note') {
              this.markerTools = false;
              this.toggelMarkerSelection('');
              this.newMarker = L.marker(event.latlng, {
                icon: L.icon({
                  iconUrl: 'my-icon.png',
                  iconSize: [0, 0]
                })
              });
              this.newMarker.bindTooltip('', {
                permanent: true,
                interactive: true,
                className: 'leaflet-tooltip'
              });
              this.newMarker.on('click', this.editPostIt, this.newMarker);
              this.newMarker.addTo(this.map);
              this.newMarker.fire('click');
              this.markers.push(this.newMarker);
            }
            if (this.markerSelection === 'polygon') {
              // eslint-disable-next-line no-const-assign
              this.paintNow = !this.paintNow;
              if (this.paintNow) {
                this.myPolyline = L.polyline([], { color: '#008000', weight: 10, opacity: 0.5 },).addTo(this.map);
              } else {
                this.markerTools = false;
                this.toggelMarkerSelection('');
                this.myPolyline.on('click', this.editPolyline, this.myPolyline);
                this.markers.push(this.myPolyline);
              }
            }
            // this.markerLocalStorage.push(markerInfoToStore);
            // this.saveMarkerLocalStorage();
            // this.setMarker(markerGeoCoordinates);
          }

          /*           if (event.containerPoint.y >= 50) {
            if (this.addMarkerMode) {
              if (this.markerSelection !== 'brush') {
                this.newPostItNode = this.formatLongPostItNotes(this.newPostItNode);
                const markerGeoCoordinates = event.latlng;
                const markerInfoToStore = {
                  markerSelection: this.markerSelection,
                  newPostItNode: this.newPostItNode,
                  markerGeoCoordinates
                };
                this.markerLocalStorage.push(markerInfoToStore);
                this.saveMarkerLocalStorage();
                this.setMarker(markerGeoCoordinates);
              } else if (this.markerSelection === 'brush') {
                paintNow = !paintNow;
                if (paintNow) {
                  this.myPolyline = L.polyline([]).addTo(this.map);
                  this.markers.push(this.myPolyline);
                } else {
                  this.addMarkerMode = false;
                  const brushInfoToStore = {
                    markerSelection: 'brush',
                    newPostItNode: this.newPostItNode,
                    markerGeoCoordinates: this.myPolyline.getLatLngs()
                  };
                  this.markerLocalStorage.push(brushInfoToStore);
                  this.saveMarkerLocalStorage();
                }
              }
            }
          } */
        });

        /* this.map.on('mousemove', (event) => {
          if (this.addMarkerMode && (this.markerSelection === 'brush')) {
            if (paintNow) {
              this.myPolyline.addLatLng(event.latlng);
            }
          }
        }); */
        this.map.on('mousemove', (event) => {
          if (this.paintNow) {
            this.myPolyline.addLatLng(event.latlng);
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
      } catch (error) {
        console.log(error); // eslint-disable-line no-console
        this.isMapLoaded = true;
      }
      // L.control.zoom({ position: 'bottomleft' }).addTo(this.map);
      // this.map.addLayer(L.rectangle(this.geobounds, { color: 'red', weight: 1 }));
    },
    makeNewPostIt(event) {
      const markerGeoCoordinates = event.latlng;
      this.editPostIt(event);
      console.log(markerGeoCoordinates);
    },

    editPolyline(e) {
      const marker = e.target;
      // eslint-disable-next-line no-multi-str
      const popupForm = '<form id="popup-form" onkeypress="return event.keyCode != 13;" style="width: 150px;">\
            <button id="button-save" \
                style="padding: 5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" type="button">Save </button>\
            <input type="color" id="pathFillColor" name="pathFillColor" value="#008000"\
              style="float: center;width: 30px; height: 30px;">\
            <button id="button-delete" \
                style="float: right; padding: 5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" \
                type="button">Delete </button>\
          </form>';
      if (marker.hasOwnProperty('_popup')) {
        marker.unbindPopup();
      }
      marker.closeTooltip();
      marker.bindPopup(popupForm);
      marker.openPopup();
      const buttonSave = L.DomUtil.get('button-save');
      L.DomEvent.addListener(buttonSave, 'click', () => {
        const pathFillColor = this.hexToRgb(L.DomUtil.get('pathFillColor').value);
        marker.setStyle({ color: pathFillColor, weight: 10, opacity: 0.5 });
        marker.closePopup();
      });
      const buttonDelete = L.DomUtil.get('button-delete');
      L.DomEvent.addListener(buttonDelete, 'click', () => {
        marker.setStyle({ color: '#000000', weight: 0, opacity: 0.0 });
        marker.closePopup();
      });
    },
    editMarker(e) {
      const marker = e.target;
      // eslint-disable-next-line no-multi-str
      const popupForm = '<form id="popup-form" onkeypress="return event.keyCode != 13;" style="width: 150px;">\
            <button id="button-save" \
                style="padding: 5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" type="button">Save </button>\
            <input type="color" id="pathFillColor" name="pathFillColor" value="#00000"\
              style="float: center;width: 30px; height: 30px; ">\
            <button id="button-delete" \
                style="float: right; padding: 5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" \
                type="button">Delete </button>\
          </form>';
      if (marker.hasOwnProperty('_popup')) {
        marker.unbindPopup();
      }
      marker.closeTooltip();
      marker.bindPopup(popupForm);
      marker.openPopup();

      L.DomEvent.addListener(L.DomUtil.get('button-save'), 'click', () => {
        const pathFillColor = this.hexToRgb(L.DomUtil.get('pathFillColor').value);
        const newMarkerSVG = `<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'><svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' width='60' height='60' viewBox='0 0 24 24'><path fill="${pathFillColor}" d='M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z' /></svg>`;
        marker.setIcon(L.icon({
          iconUrl: encodeURI(`data:image/svg+xml,${newMarkerSVG}`),
          iconSize: [30, 30]
        }));
        marker.closePopup();
      });

      L.DomEvent.addListener(L.DomUtil.get('button-delete'), 'click', () => {
        marker.setIcon(L.icon({
          iconUrl: 'my-icon.png',
          iconSize: [0, 0]
        }));
        marker.closePopup();
      });
    },
    hexToRgb(hex) {
      const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
      hex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);

      const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
      return result ? `rgb(${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)})`
        : null;
    },

    editPostIt(e) {
      const marker = e.target;
      const oldPostItText = marker.getTooltip().getContent();
      // eslint-disable-next-line no-multi-str
      const popupForm = '<form id="popup-form" onkeypress="return event.keyCode != 13;">\
            <label for="PostItText">Enter your Post-it note here:</label><br>\
            <input style="margin:5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" \
                type="text" id="PostItText" name="PostItText" value=""><br>\
            <button id="button-save" \
                style="padding: 5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" type="button">Save </button>\
            <input type="color" id="backgroundColor" name="backgroundColor" value="#FFFF00"\
              style="width: 30px; height: 30px; " >\
            <button id="button-delete" \
                style="float: right; padding: 5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" \
                type="button">Delete </button>\
          </form>';
      if (marker.hasOwnProperty('_popup')) {
        marker.unbindPopup();
      }
      marker.closeTooltip();
      marker.bindPopup(popupForm);
      marker.openPopup();

      L.DomUtil.get('PostItText').value = oldPostItText;

      const temp = document.querySelector('.leaflet-tooltip');
      L.DomEvent.addListener(L.DomUtil.get('button-save'), 'click', () => {
        marker.setTooltipContent(this.formatLongPostItNotes(L.DomUtil.get('PostItText').value));
        temp.setAttribute('style', `background:${L.DomUtil.get('backgroundColor').value}`);
        marker.closePopup();
        marker.openTooltip();
      });
      L.DomEvent.addListener(L.DomUtil.get('button-delete'), 'click', () => {
        marker.closePopup();
      });
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
      } else if (this.markerSelection === 'brush') {
        this.newMarker = L.polyline(markerGeoCoordinates);
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
        try {
          if (event.latlng === this.markers[x].getLatLng()) {
            this.map.removeLayer(this.markers[x]);
          }
        } catch {
          // continue regardless of error
        }
      }
    },

    saveMarkerLocalStorage() {
      const parsed = JSON.stringify(this.markerLocalStorage);
      localStorage.setItem('PostIts', parsed);
    },

    formatLongPostItNotes(text) {
      const words = text.split(' ');
      let str = '';
      let lettersSinceBR = 0;
      for (let i = 0; i < words.length; i += 1) {
        const nextWord = words[i];
        if (nextWord.length >= 15) {
          if (lettersSinceBR !== 0) {
            str += '<br>';
          }
          let nextWordLeft = nextWord.length;
          while (nextWordLeft > 0) {
            str += nextWord.slice(nextWord.length - nextWordLeft,
              nextWord.length - nextWordLeft + 15);
            str += '<br>';
            lettersSinceBR = 0;
            nextWordLeft -= 15;
          }
        } else if (lettersSinceBR + nextWord.length <= 10) {
          str += nextWord;
          str += ' ';
          lettersSinceBR += nextWord.length;
        } else {
          if (lettersSinceBR !== 0) {
            str += '<br>';
          }
          lettersSinceBR = nextWord.length;
          str += nextWord;
        }
      }

      return str;
    },

    deleteAllMarkers() {
      for (let x = 0; x < this.markers.length; x += 1) {
        this.markers[x].remove();
      }
      while (this.markers.length > 0) {
        this.markers.pop();
      }
      while (this.markerLocalStorage.length > 0) {
        this.markerLocalStorage.pop();
      }
      localStorage.removeItem('PostIts');
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
