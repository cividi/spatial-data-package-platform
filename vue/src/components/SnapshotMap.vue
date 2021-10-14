<!-- eslint-disable -->
<i18n>
{
  "de": {
    "addComment": "Klicken Sie auf die Stelle in Karte an der Sie einen Kommentar hinzufügen möchten.",
    "newComment": "Neuer Kommentar",
    "title": "Titel",
    "text":"Text",
    "cancel": "abbrechen",
    "next": "weiter",
    "prev": "zurück",
    "save": "speichern",
    "saveinfo": "Speichere Angaben",
    "mandatory": "Dies ist ein Pflichtfeld",
    "email": "E-Mail",
    "emailhint": "Um Ihren Kommentar freizuschalten, schicken wir Ihnen eine Email mit einem Aktivierungslink. Bitte geben Sie Ihre Email Adresse an:",
    "notpublic":"Diese Informationen werden nicht veröffentlicht oder an Dritte weitergegeben"
  },
  "fr": {
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

      <v-container fluid class="pa-0" ref="mapbox">
        <div id="map"></div>
        <span id="mapstatus" :class="{ loaded: isMapLoaded, waiting: !isMapLoaded }"></span>
      </v-container>

      <p class="addHint" v-if="addingAnnotation">{{ $t('addComment') }}</p>

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

      <v-btn
        v-if="wshash && annotationsOpen && !screenshotMode"
        fab absolute small
        id="addingAnnotation"
        color="primary"
        @click="addingAnnotation ? addingAnnotation=null : addingAnnotation='COM'">
        <v-icon v-if="!addingAnnotation">mdi-comment-plus-outline</v-icon>
        <v-icon v-if="addingAnnotation">mdi-close-thick</v-icon>
      </v-btn>

      <v-card v-if="newAnnotation" id="commentedit" light width="400" class="pa-4">
        <h3>{{ $t('newComment') }}</h3>
        <v-form
          class="pt-4"
          ref="commentform"
          lazy-validation
          @submit.prevent="saveAnnotation"
        >
          <v-stepper v-model="commentstepper" class="elevation-0">
            <v-stepper-items>
              <v-stepper-content step="1" class="pa-0">
                <v-select
                  :items="categories"
                  item-text="name"
                  item-value="pk"
                  v-model="newAnnotation.category"
                  label="Kategorie"
                  :rules="[v => !!v || $t('mandatory')]"
                  required
                >
                  <template slot="item" slot-scope="data">
                    <img
                      :src="djangobaseurl + '/media/' + data.item.icon"
                      height="24px"
                    /><p>{{data.item.name}}</p>
                  </template>
                </v-select>
                <v-text-field
                  v-model="newAnnotation.title"
                  :label="$t('title')"
                  :rules="[v => !!v || $t('mandatory')]"
                  required
                />
                <v-textarea
                  outlined
                  v-model="newAnnotation.text"
                  :label="$t('text')"
                  :rules="[v => !!v || $t('mandatory')]"
                  required
                />
                <div class="d-flex justify-space-between">
                  <v-btn
                  @click="cancelAnnotation">
                    {{ $t('cancel') }}
                  </v-btn>
                  <v-btn
                    color="primary"
                    @click="validateStepOne"
                  >
                    {{ $t('next') }}
                  </v-btn>
                </div>
              </v-stepper-content>
              <v-stepper-content step="2" class="pa-0">
                <p>{{ $t('emailhint') }}</p>
                <v-text-field
                  v-model="newAnnotation.email"
                  :label="$t('email')"
                  :rules="[v => !!v || $t('mandatory')]"
                  required
                />
                <v-select
                  :items="usergroups"
                  v-model="newAnnotation.usergroup"
                  label="Personengruppe"
                  :rules="[v => !!v || $t('mandatory')]"
                  required
                ></v-select>
                <div class="d-flex justify-space-between">
                  <v-btn
                  @click="commentstepper = 1">
                    {{ $t('prev') }}
                  </v-btn>
                  <v-btn
                    type="submit"
                    color="primary"
                  >
                    {{ $t('save') }}
                  </v-btn>
                </div>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-form>
      </v-card>

      <div id="commentholder">
        <div id="currentComment">
          <div v-if="currentComment"
            :class="currentComment.attachements.length ? 'maxW': ''">
            <b>{{currentComment.data.properties.title}}</b><br>
            <v-carousel
              v-if="currentComment.attachements.length > 0"
              height="auto"
              hide-delimiters
              class="my-1">
              <v-carousel-item
                v-for="(item,i) in currentComment.attachements"
                :key="i"
                :src="djangobaseurl + '/media/' + item.document"
              ></v-carousel-item>
            </v-carousel>
            {{currentComment.data.properties.description}}<br>

            <div class="d-flex align-center justify-space-between">
                <p class="rating">
                  <v-icon color="primary">mdi-heart-outline</v-icon>
                  <b
                    style="vertical-align: middle;"
                  > {{currentComment.rating}}</b>
                </p>
              <v-btn
                fab small color="primary"
                @click="rateUp(currentComment.pk)"
                ><v-icon small>mdi-heart-plus-outline</v-icon></v-btn>
            </div>
          </div>
        </div>
      </div>
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
.leaflet-popup-content {
  padding: 10px;
}
.leaflet-popup-content img {
  max-width: 100%;
  min-width: 260px;
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

#addingAnnotation {
  top: 5.6em;
  right: 1.3em;
  transition: top 0.3s;
  transition-timing-function: ease-in-out;
}
@media (min-width: 1264px) {
  #addingAnnotation {
    top: 1.2em;
    transition-delay: 0.4s;
  }
}

.addHint {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  text-align: center;
  text-shadow: 0 0 2px #fff, 0 0 5px #fff;
  background: #ffffff66;
  padding: 5px 3em;
}
#commentholder {
  position: absolute;
  display: none;
}

#commentedit {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 510;
}

#currentComment {
  min-width: 200px;
}
#currentComment .maxW {
  width: calc(100vw - 40px);
  max-width: 430px;
}
.v-list-item img {
  margin-right: 1em;
}
p.rating {
  color: primary;
  font-size: 16px;
  margin-bottom: 0;
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
      wshash: this.$route.params.wshash,
      bfsNumber: this.$route.params.bfsNumber,
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      map: null,
      layerContainer: null,
      mapinfoopen: true,
      addingAnnotation: null,
      newAnnotation: null,
      commentstepper: 1,
      currentCommentIndex: null,
      usergroups: ['Anwohner', 'Bürger', 'Beschäftigter', 'Student'],
      title: '',
      description: '',
      legend: [],
      sources: [],
      layers: [],
      geobounds: [],
      screenshotMode: this.$route.query.hasOwnProperty('screenshot'),
      screenshotIsThumbnail: this.$route.query.hasOwnProperty('thumbnail'),
      isMapLoaded: false,
      // eslint-disable-next-line global-require
      commentIconUrl: require('@/assets/images/icons/comment_36.svg'),
      // eslint-disable-next-line global-require
      commentLockedIconUrl: require('@/assets/images/icons/comment_locked_36.svg')
    };
  },

  props: {
    snapshot: Object,
    geojson: Object,
    annotations: Array,
    categories: Array,
    geoboundsIn: Array,
    predecessor: Object,
    annotationsOpen: Boolean
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
    },
    currentComment() {
      if (this.annotations) {
        return this.annotations[this.currentCommentIndex];
      }
      return null;
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
            // curfeature.bindPopup(() => {
            //   let content = feature.properties.description;
            //   if (feature.properties.title) {
            //     content = `<b>${feature.properties.title}</b><br />${content}`;
            //   }
            //   return content;
            // },
            // { maxWidth: 450, maxHeight: 600 });
            curfeature.on('click', this.showPopup);
          }
          return curfeature;
        }
      });
      return geoJsonExtended;
    },

    showPopup(e) {
      // console.log(e.target.feature);
      let content;
      if (e.target.feature.kind === 'COM') {
        this.currentCommentIndex = e.target.feature.index;
        content = document.getElementById('currentComment');
      } else {
        content = e.target.feature.properties.description;
        if (e.target.feature.properties.title) {
          content = `<b>${e.target.feature.properties.title}</b><br />${content}`;
        }
      }
      const myPopup = new L.Popup({ maxWidth: 450, maxHeight: 600 })
        .setLatLng(e.target._latlng) // eslint-disable-line no-underscore-dangle
        .setContent(content);

      myPopup.on('remove', (e) => {
        console.log('remove');
        document.getElementById('commentholder').append(e.target.getContent());
      });

      window.setTimeout(() => { myPopup.openOn(this.map); }, 100);
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
          this.annotations = this.annotations.map((a, i) => {
            a.data.kind = a.kind;
            a.data.index = i;
            if (a.category.length === 1) {
              a.data.properties.icon = { iconUrl: `/media/${a.category[0].icon}`, iconSize: [36, 36], popupAnchor: [0, -16] };
            }
            return a;
          });
          const annotationsdata = this.annotations.map(a => a.data);
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata, ''
          ));
        }
        this.layerContainer.addTo(this.map);

        this.map.on('click', (event) => {
          if (this.addingAnnotation !== null) {
            switch (this.addingAnnotation) {
              case 'COM': {
                const newMarker = L.marker(event.latlng, {
                  icon: new L.Icon({
                    iconUrl: this.commentIconUrl,
                    iconSize: [36, 36]
                  }),
                  draggable: true
                });
                newMarker.on('click', this.newComment);
                newMarker.addTo(this.map);
                this.map.setView(event.latlng);
                window.setTimeout(() => { newMarker.fire('click'); }, 500);
                break;
              }
              default: {
                console.log('Error - Annotation type not supported');
              }
            }

            this.addingAnnotation = null;
          }
        });

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

    newComment(e) {
      this.newAnnotation = {
        kind: 'COM',
        title: '',
        text: '',
        marker: e.target
      };
    },

    validateStepOne() {
      const myform = this.$refs.commentform;
      if (myform.inputs[0].validate()) {
        if (myform.inputs[1].validate()) {
          if (myform.inputs[2].validate()) {
            this.commentstepper = 2;
          } else {
            myform.inputs[2].focus();
          }
        } else {
          myform.inputs[1].focus();
        }
      } else {
        myform.inputs[0].focus();
      }
    },

    cancelAnnotation() {
      this.newAnnotation.marker.removeFrom(this.map);
      this.newAnnotation = null;
    },

    async saveAnnotation() {
      const myform = this.$refs.commentform;
      if (!myform.validate()) {
        return false;
      }
      const csrftoken = this.$cookies.get('csrftoken', '');
      const formData = new FormData();

      formData.append('kind', this.newAnnotation.kind);
      formData.append('workspace', this.wshash);
      switch (this.newAnnotation.kind) {
        case 'COM': {
          const latlng = this.newAnnotation.marker.getLatLng();
          formData.append('category', this.newAnnotation.category);
          formData.append('author_email', this.newAnnotation.email);
          formData.append('data', `{
            "type": "Feature", 
            "geometry": {
              "type": "Point",
              "coordinates": [${latlng.lng}, ${latlng.lat}]
            },
            "properties": {
              "fill": "true", 
              "title": "${this.newAnnotation.title}", 
              "description": "${this.newAnnotation.text}",
              "usergroup": "${this.newAnnotation.usergroup}"
            }
          }`);
          break;
        }
        default: {
          console.log('Saving this annotation type not supported');
          return false;
        }
      }

      const save = await this.$restApi.post('annotations/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': csrftoken
        }
      });
      if (save.status === 201) {
        this.newAnnotation.marker.setIcon(
          new L.Icon({
            iconUrl: this.commentLockedIconUrl,
            iconSize: [36, 36]
          })
        );
        this.newAnnotation = null;
        console.log('Kommentar gespeichert. Klicken Sie den Link in der Email um ihn freizuschalten.');
      } else {
        console.log('Speichern fehlgeschlagen');
      }
      return save;
    },

    async rateUp(annotationPk) {
      const csrftoken = this.$cookies.get('csrftoken', '');
      const formData = new FormData();

      const save = await this.$restApi.patch(`rateupannotation/${annotationPk}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': csrftoken
        }
      });
      if (save.status === 200) {
        this.currentComment.rating = parseInt(save.data.rating, 10);
      } else {
        console.log('Speichern fehlgeschlagen');
      }
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
