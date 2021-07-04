<!-- eslint-disable -->
<i18n>
{
  "de": {
    "tooltip.marker": "Marker auf der Karte setzen",
    "tooltip.polygonStart": "Klicken um Markiermodus zu starten ",
    "tooltip.polygonEnd": "Klick um Markiermodus zu verlassen",
    "tooltip.postIt": "Post-it auf der Karte setzen",
    "tooltip.deactivateAnnotation": "Anmerkungen verbergen",
    "tooltip.postItEditorTextInput": "Kommentar:",
    "tooltip.markerEditorSave": "Speichern",
    "tooltip.markerEditorDelete": "Löschen"
  },
  "fr": {
    "tooltip.marker": "Définir un marqueur sur la carte",
    "tooltip.polygonStart": "Cliquez pour démarrer le mode marqueur",
    "tooltip.polygonEnd": "Cliquez pour quitter le mode marqueur",
    "tooltip.postIt": "Mettre un post-it sur la carte",
    "tooltip.deactivateAnnotation": "Masquer les annotations",
    "tooltip.postItEditorTextInput": "Annotations",
    "tooltip.markerEditorSave": "Save",
    "tooltip.markerEditorDelete": "Delete"
  }
}
</i18n>
<!-- eslint-enable -->
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
          v-show="!screenshotMode"
          v-on:click="markerTools=!markerTools; showAnnotations(); map.closePopup()">
          <v-icon large color="white"> mdi-brush </v-icon>
        </button>
        <v-card v-if="markerTools" style="position: absolute; width: 36px">
            <v-row>
              <v-col >
                <v-tooltip v-model="this.markerSelectionMarker" left>
                  <template v-slot:activator="{}">
                    <v-btn icon @click="toggelMarkerSelection('marker')">
                      <v-icon large color="black"> mdi-map-marker </v-icon>
                    </v-btn>
                  </template>
                  {{ $t("tooltip.marker")}}
                </v-tooltip>
              </v-col>
              <v-col >
                <v-tooltip v-model="this.markerSelectionPolygon" left>
                  <template v-slot:activator="{}">
                    <v-btn icon @click="toggelMarkerSelection('polygon')">
                      <v-icon large color="black"> mdi-vector-polygon </v-icon>
                    </v-btn>
                  </template>
                  <span v-if="!paintNow">{{ $t("tooltip.polygonStart")}}</span>
                  <span v-else>{{ $t("tooltip.polygonEnd")}}</span>
                </v-tooltip>
              </v-col>
              <v-col >
                <v-tooltip v-model="this.markerSelectionNote" left>
                  <template v-slot:activator="{}">
                    <v-btn icon @click="toggelMarkerSelection('note')">
                      <v-icon large color="black"> mdi-note-outline </v-icon>
                    </v-btn>
                  </template>
                  {{ $t("tooltip.postIt")}}
                </v-tooltip>
              </v-col>
              <v-col >
                <v-tooltip left>
                  <template v-slot:activator="{on}">
                    <v-btn icon v-on="on"
                       @click="toggelMarkerSelection(''); hideAnnotations();
                      markerTools=!markerTools;">
                      <v-icon large color="black"> mdi-eye-off </v-icon>
                    </v-btn>
                  </template>
                  {{ $t("tooltip.deactivateAnnotation")}}
                </v-tooltip>
              </v-col>
            </v-row>
        </v-card>
      </div>
    </v-main>
    <v-main fluid class="pa-0" ref="mapbox">
        <div id="map" v-bind:style="{ cursor: computedCursor }"></div>
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

.leaflet-tooltip-left:before {
  right: 0;
  margin-right: -12px;
  border-left-color: rgba(0, 0, 0, 0.4);
}

.leaflet-tooltip-right:before {
  left: 0;
  margin-left: -12px;
  border-right-color: rgba(0, 0, 0, 0.4);
}

.leaflet-tooltip {
  position: absolute;
  padding: 4px;
  background-color: rgba(0, 0, 0, 0.4);
  border: 0px solid #000;
  color: #000;
  white-space: nowrap;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
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
      markerSelection: '',
      markerTools: false,
      editMode: false,
      cursorType: '',
      popupForm: '',
      paintNow: false,
      markerSelectionMarker: false,
      markerSelectionPolygon: false,
      markerSelectionNote: false
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

  methods: {
    changeCursor() {
      if (this.paintNow) {
        this.cursorType = 'pointer';
      }
      if (this.markerSelectionMarker) {
        this.cursorType = 'url("data:image/svg+xml,<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z\' /></svg>"), pointer';
      } else if (this.markerSelectionPolygon) {
        this.cursorType = 'url("data:image/svg+xml,<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M2,2V8H4.28L5.57,16H4V22H10V20.06L15,20.05V22H21V16H19.17L20,9H22V3H16V6.53L14.8,8H9.59L8,5.82V2M4,4H6V6H4M18,5H20V7H18M6.31,8H7.11L9,10.59V14H15V10.91L16.57,9H18L17.16,16H15V18.06H10V16H7.6M11,10H13V12H11M6,18H8V20H6M17,18H19V20H17\' /></svg>"), pointer';
      } else if (this.markerSelectionNote) {
        this.cursorType = 'url("data:image/svg+xml,<?xml version=\'1.0\' encoding=\'UTF-8\'?><!DOCTYPE svg PUBLIC \'-//W3C//DTD SVG 1.1//EN\' \'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\'><svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' version=\'1.1\' width=\'60\' height=\'60\' viewBox=\'0 0 24 24\'><path d=\'M14,10H19.5L14,4.5V10M5,3H15L21,9V19A2,2 0 0,1 19,21H5C3.89,21 3,20.1 3,19V5C3,3.89 3.89,3 5,3M5,5V19H19V12H12V5H5Z\' /></svg>"), pointer';
      } else { this.cursorType = 'auto'; }
    },
    toggelMarkerSelection(newMode) {
      if (newMode === 'marker') {
        this.markerSelectionMarker = !this.markerSelectionMarker;
        this.markerSelectionPolygon = false;
        this.markerSelectionNote = false;
      } else if (newMode === 'polygon') {
        this.markerSelectionMarker = false;
        this.markerSelectionPolygon = !this.markerSelectionPolygon;
        this.markerSelectionNote = false;
      } else if (newMode === 'note') {
        this.markerSelectionMarker = false;
        this.markerSelectionPolygon = false;
        this.markerSelectionNote = !this.markerSelectionNote;
      } else {
        this.markerSelectionMarker = false;
        this.markerSelectionPolygon = false;
        this.markerSelectionNote = false;
      }
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

        this.myPolyline = [];
        this.annotationMarkers = new L.FeatureGroup();
        this.map.addLayer(this.annotationMarkers);
        this.map.on('click', (event) => {
          if (this.markerTools) {
            if (this.markerSelectionMarker) {
              this.markerTools = false;
              this.toggelMarkerSelection('');
              const pathFillColor = this.hexToRgb('#0000ff');
              const markerSVG = `<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'><svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' width='60' height='60' viewBox='0 0 24 24'><path fill="${pathFillColor}" d='M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z' /></svg>`;
              this.newMarker = L.marker(event.latlng, {
                icon: L.icon({
                  iconUrl: encodeURI(`data:image/svg+xml,${markerSVG}`),
                  iconSize: [30, 30]
                })
              });
              this.newMarker.on('contextmenu', this.deleteMarker, this);
              this.newMarker.on('click', this.editMarker, this);
              this.annotationMarkers.addLayer(this.newMarker);
            }
            if (this.markerSelectionPolygon) {
              this.paintNow = !this.paintNow;
              if (this.paintNow) {
                this.myPolyline = L.polyline([], { color: '#008000', weight: 15, opacity: 0.5 },).addTo(this.annotationMarkers);
              } else {
                this.markerTools = false;
                this.toggelMarkerSelection('');
                this.myPolyline.on('click', this.editPolyline, this.myPolyline);
              }
            }
            if (this.markerSelectionNote) {
              this.markerTools = false;
              this.toggelMarkerSelection('');
              const newMarker = L.marker(event.latlng, {
                icon: L.icon({
                  iconUrl: 'my-icon.png',
                  iconSize: [0, 0]
                })
              });
              newMarker.bindTooltip('', {
                permanent: true,
                interactive: true,
                className: 'leaflet-tooltip'
              });
              this.annotationMarkers.addLayer(newMarker);
              newMarker.on('click', this.editPostIt, newMarker);
              newMarker.fire('click');
            }
          }
        });
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

    hideAnnotations() {
      this.map.removeLayer(this.annotationMarkers);
    },
    showAnnotations() {
      this.map.addLayer(this.annotationMarkers);
    },

    editMarker(e) {
      this.map.closePopup();
      const marker = e.target;
      this.popupForm = ` 
        <div style="width: 15em; text-align: center">
          <button id="button-save" style="padding: 0px 4px 0px 4px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px"></button>
          <div style=" display: inline-block; margin: 0px 6px 0px 6px; width: 15px; height: 15px; border-radius: 15px; overflow: hidden">
            <input id="pathFillColor" type="color" value="#0000ff" 
            style="width: 200%; height: 200%; transform: translate(-25%, -25%);
            cursor: url(data:image/x-icon;base64,AAABAAEAEBAAAAAAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAAAAD///8BAAAAfwAAAIH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAcQAAAN8AAADTAAAArwAAAE8AAAAJ////Af///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAJEAAADLAAAAEwAAAHsAAADDAAAA3wAAADP///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAuQAAAHX///8B////AQAAAF0AAADtAAAAOf///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAFMAAAC/////Af///wH///8BAAAAUQAAAO0AAAA5////Af///wH///8B////Af///wH///8B////Af///wEAAAANAAAA5wAAAFH///8B////Af///wEAAABRAAAA7QAAADn///8B////Af///wH///8B////Af///wH///8B////AQAAAD0AAADtAAAARf///wH///8B////AQAAAFEAAADtAAAAOQAAACP///8B////Af///wH///8B////Af///wH///8BAAAARQAAAO0AAABF////Af///wH///8BAAAAUQAAAO0AAADvAAAAmf///wH///8B////Af///wH///8B////Af///wEAAABFAAAA7QAAAEX///8B////AQAAADUAAADxAAAA/wAAAPcAAAAr////Af///wH///8B////Af///wH///8B////AQAAAEUAAADtAAAARQAAADUAAADvAAAA/wAAAPcAAABFAAAALf///wH///8B////Af///wH///8B////Af///wH///8BAAAARQAAAO0AAADvAAAA/wAAAPcAAABFAAAAgwAAAPsAAABX////Af///wH///8B////Af///wH///8B////AQAAACUAAADvAAAA/wAAAPcAAABFAAAAgwAAAP8AAAD/AAAA+wAAAE////8B////Af///wH///8B////Af///wEAAAADAAAAoQAAAPcAAABFAAAAgwAAAP8AAAD/AAAA/wAAAP8AAADf////Af///wH///8B////Af///wH///8B////AQAAAAMAAAAvAAAALQAAAPsAAAD/AAAA/wAAAP8AAAD/AAAA+////wH///8B////Af///wH///8B////Af///wH///8B////Af///wEAAABXAAAA+wAAAP8AAAD/AAAA/wAAALX///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAE8AAADfAAAA+wAAALUAAAAXAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//w==), default;">
          </div>
          <button id="button-delete" style="padding: 0px 4px 0px 4px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px"></button>
        </div> `;

      if (marker.hasOwnProperty('_popup')) {
        marker.unbindPopup();
      }
      marker.bindPopup(this.popupForm);
      marker.openPopup();

      L.DomUtil.get('button-save').innerText = this.$i18n.t('tooltip.markerEditorSave');
      L.DomUtil.get('button-delete').innerText = this.$i18n.t('tooltip.markerEditorDelete');

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
        this.annotationMarkers.removeLayer(marker);
        marker.closePopup();
      });
    },

    editPolyline(e) {
      this.map.closePopup();
      const marker = e.target;
      this.popupForm = ` 
        <div style="width: 15em; text-align: center">
          <button id="button-save" style="padding: 0px 4px 0px 4px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px"></button>
          <div style=" display: inline-block; margin: 0px 6px 0px 6px; width: 15px; height: 15px; border-radius: 15px; overflow: hidden">
            <input id="pathFillColor" type="color" value="#008000" 
            style="width: 200%; height: 200%; transform: translate(-25%, -25%);
            cursor: url(data:image/x-icon;base64,AAABAAEAEBAAAAAAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAAAAD///8BAAAAfwAAAIH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAcQAAAN8AAADTAAAArwAAAE8AAAAJ////Af///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAJEAAADLAAAAEwAAAHsAAADDAAAA3wAAADP///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAuQAAAHX///8B////AQAAAF0AAADtAAAAOf///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAFMAAAC/////Af///wH///8BAAAAUQAAAO0AAAA5////Af///wH///8B////Af///wH///8B////Af///wEAAAANAAAA5wAAAFH///8B////Af///wEAAABRAAAA7QAAADn///8B////Af///wH///8B////Af///wH///8B////AQAAAD0AAADtAAAARf///wH///8B////AQAAAFEAAADtAAAAOQAAACP///8B////Af///wH///8B////Af///wH///8BAAAARQAAAO0AAABF////Af///wH///8BAAAAUQAAAO0AAADvAAAAmf///wH///8B////Af///wH///8B////Af///wEAAABFAAAA7QAAAEX///8B////AQAAADUAAADxAAAA/wAAAPcAAAAr////Af///wH///8B////Af///wH///8B////AQAAAEUAAADtAAAARQAAADUAAADvAAAA/wAAAPcAAABFAAAALf///wH///8B////Af///wH///8B////Af///wH///8BAAAARQAAAO0AAADvAAAA/wAAAPcAAABFAAAAgwAAAPsAAABX////Af///wH///8B////Af///wH///8B////AQAAACUAAADvAAAA/wAAAPcAAABFAAAAgwAAAP8AAAD/AAAA+wAAAE////8B////Af///wH///8B////Af///wEAAAADAAAAoQAAAPcAAABFAAAAgwAAAP8AAAD/AAAA/wAAAP8AAADf////Af///wH///8B////Af///wH///8B////AQAAAAMAAAAvAAAALQAAAPsAAAD/AAAA/wAAAP8AAAD/AAAA+////wH///8B////Af///wH///8B////Af///wH///8B////Af///wEAAABXAAAA+wAAAP8AAAD/AAAA/wAAALX///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAE8AAADfAAAA+wAAALUAAAAXAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//w==), default;">
          </div>
          <button id="button-delete" style="padding: 0px 4px 0px 4px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px"></button>
        </div> `;

      if (marker.hasOwnProperty('_popup')) {
        marker.unbindPopup();
      }

      marker.bindPopup(this.popupForm);
      marker.openPopup();

      L.DomUtil.get('button-save').innerText = this.$i18n.t('tooltip.markerEditorSave');
      L.DomUtil.get('button-delete').innerText = this.$i18n.t('tooltip.markerEditorDelete');

      L.DomEvent.addListener(L.DomUtil.get('button-save'), 'click', () => {
        const pathFillColor = this.hexToRgb(L.DomUtil.get('pathFillColor').value);
        marker.setStyle({ color: pathFillColor, weight: 15, opacity: 0.4 });
        marker.closePopup();
      });
      L.DomEvent.addListener(L.DomUtil.get('button-delete'), 'click', () => {
        this.annotationMarkers.removeLayer(marker);
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
      this.popupForm = ` 
        <div style="width: 18em; text-align: center">
        <label id="PostItTextHeader" for="PostItText"></label><br>
        <input style="margin:5px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px;" 
                type="text" id="PostItText" name="PostItText" value=""><br>
          <button id="button-save" style="padding: 0px 4px 0px 4px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px"></button>
          <div style=" display: inline-block; margin: 0px 6px 0px 6px; width: 15px; height: 15px; border-radius: 15px; overflow: hidden">
            <input id="backgroundColor" type="color" value="#0000ff" 
            style="width: 200%; height: 200%; transform: translate(-25%, -25%);
            cursor: url(data:image/x-icon;base64,AAABAAEAEBAAAAAAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAAAAD///8BAAAAfwAAAIH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAcQAAAN8AAADTAAAArwAAAE8AAAAJ////Af///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAJEAAADLAAAAEwAAAHsAAADDAAAA3wAAADP///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAuQAAAHX///8B////AQAAAF0AAADtAAAAOf///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAFMAAAC/////Af///wH///8BAAAAUQAAAO0AAAA5////Af///wH///8B////Af///wH///8B////Af///wEAAAANAAAA5wAAAFH///8B////Af///wEAAABRAAAA7QAAADn///8B////Af///wH///8B////Af///wH///8B////AQAAAD0AAADtAAAARf///wH///8B////AQAAAFEAAADtAAAAOQAAACP///8B////Af///wH///8B////Af///wH///8BAAAARQAAAO0AAABF////Af///wH///8BAAAAUQAAAO0AAADvAAAAmf///wH///8B////Af///wH///8B////Af///wEAAABFAAAA7QAAAEX///8B////AQAAADUAAADxAAAA/wAAAPcAAAAr////Af///wH///8B////Af///wH///8B////AQAAAEUAAADtAAAARQAAADUAAADvAAAA/wAAAPcAAABFAAAALf///wH///8B////Af///wH///8B////Af///wH///8BAAAARQAAAO0AAADvAAAA/wAAAPcAAABFAAAAgwAAAPsAAABX////Af///wH///8B////Af///wH///8B////AQAAACUAAADvAAAA/wAAAPcAAABFAAAAgwAAAP8AAAD/AAAA+wAAAE////8B////Af///wH///8B////Af///wEAAAADAAAAoQAAAPcAAABFAAAAgwAAAP8AAAD/AAAA/wAAAP8AAADf////Af///wH///8B////Af///wH///8B////AQAAAAMAAAAvAAAALQAAAPsAAAD/AAAA/wAAAP8AAAD/AAAA+////wH///8B////Af///wH///8B////Af///wH///8B////Af///wEAAABXAAAA+wAAAP8AAAD/AAAA/wAAALX///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AQAAAE8AAADfAAAA+wAAALUAAAAXAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//w==), default;">
          </div>
          <button id="button-delete" style="padding: 0px 4px 0px 4px; border: 1px solid rgba(0,0,0,0.3); border-radius: 2px"></button>
        </div> `;
      if (marker.hasOwnProperty('_popup')) {
        marker.unbindPopup();
      }

      marker.bindPopup(this.popupForm, {
        autoClose: false,
        closeOnClick: false,
        closeButton: false
      });
      marker.openPopup();

      const TooltipSnippet = marker.getTooltip().getContent();
      const oldPostItText = TooltipSnippet.slice(60, -10);
      const oldPostItColor = TooltipSnippet.slice(23, 30);
      L.DomUtil.get('button-save').innerText = this.$i18n.t('tooltip.markerEditorSave');
      L.DomUtil.get('button-delete').innerText = this.$i18n.t('tooltip.markerEditorDelete');
      L.DomUtil.get('PostItTextHeader').innerText = this.$i18n.t('tooltip.postItEditorTextInput');

      L.DomUtil.get('PostItText').value = oldPostItText.replaceAll('<br>', ' ');
      if (oldPostItColor.length === 0) {
        L.DomUtil.get('backgroundColor').value = '#ffff00';
      } else {
        L.DomUtil.get('backgroundColor').value = oldPostItColor;
      }
      L.DomEvent.addListener(L.DomUtil.get('button-save'), 'click', () => {
        const postItText = this.formatLongPostItNotes(L.DomUtil.get('PostItText').value);
        const postItColor = L.DomUtil.get('backgroundColor').value;
        const TooltipSnippet = `<div style='background:${postItColor}; padding:1px 3px 1px 3px'><b>${postItText}</b></div>`;
        marker.setTooltipContent(TooltipSnippet);
        marker.closePopup();
        marker.openTooltip();
      });
      L.DomEvent.addListener(L.DomUtil.get('button-delete'), 'click', () => {
        this.annotationMarkers.removeLayer(marker);
      });
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
