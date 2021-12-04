<!-- eslint-disable -->
<i18n>
{
  "de": {
    "label": {
      "addComment": "Klicken Sie auf die Stelle in Karte an der Sie einen Kommentar hinzufügen möchten.",
      "newComment": "Neuer Kommentar",
      "title": "Title",
      "category": "Kategorie",
      "price":"Preis (in lokaler Währung) oder Beschreibung",
      "group": "Personengruppe",
      "groups": {
        "resident": "Einwohner:in",
        "tourist": "Tourist:in"
      },
      "emailhint": "Um Ihren Kommentar freizuschalten, schicken wir Ihnen eine Email mit einem Aktivierungslink. Bitte geben Sie Ihre Email Adresse an:",
      "notpublic":"Diese Informationen werden nicht veröffentlicht oder an Dritte weitergegeben",
      "saveinfo": "Speichere Angaben"
    },
    "btn": {
      "cancel": "abbrechen",
      "next": "weiter",
      "prev": "zurück",
      "save": "speichern"
    },
    "validationError": {
      "mandatory": "Dies ist ein Pflichtfeld",
      "nan": "Bitte eine Zahl eingeben",
      "email": "E-Mail",
      "inv": "Dies ist keine gültige E-Mail Adresse",
      "toolong": "Zu lange Eingabe, bitte ein wenig kürzer halten."
    },
    "error": {
      "failed": "Speichern fehlgeschlagen",
      "failedText": "Bitte prüfen Sie Ihre Eingaben oder versuchen Sie es später nochmals."
    },
    "success": {
      "saved": "Speichern erfolgreich",
      "commentSaved": "Ihr Kommentar wurde gespeichert. Klicken Sie den Link in der Email um ihn freizuschalten."
    }
  },
  "fr": {
  },
  "en": {
    "label": {
      "addComment": "Please click on the place in the map where you want to add a comment.",
      "newComment": "New annotation",
      "category": "Category",
      "title": "Title",
      "group": "I am a",
      "groups": {
        "resident": "Resident",
        "tourist": "Tourist"
      },
      "price":"Price (in local currency) or description",
      "saveinfo": "Saving",
      "email": "E-mail",
      "emailhint": "In order to publish your input, you will receive an e-mail with an activation link. Please share your address:",
      "notpublic":"This information will not be published or forwarded to 3rd parties"
    },
    "btn": {
      "cancel": "cancel",
      "next": "next",
      "prev": "back",
      "save": "save"
    },
    "validationError": {
      "mandatory": "This field is mandatory",
      "nan": "Please enter a valid number",
      "inv": "Please enter a valid e-mail address",
      "toolong": "Too long, please keep it shorter."
    },
    "error": {
      "failed": "Save failed",
      "failedText": "Please check your entries or try again later."
    },
    "success": {
      "saved": "Save successful",
      "commentSaved": "Your comment has been saved. Click the link in the email to activate it."
    }
  }
}
</i18n>
<!-- eslint-enable -->

<template>
    <v-main :class="{navopen : snapshotnav}">
      <v-slide-x-reverse-transition>
        <v-btn fab absolute small
          style="top:1.2em; right:1.3em;"
          color="primary"
          v-if="!snapshotnav"
          @click="snapshotnav=!snapshotnav;">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </v-slide-x-reverse-transition>

      <v-container fluid class="pa-0" ref="mapbox">
        <span id="mapstatus" :class="{
          loaded: isMapLoaded,
          waiting: !isMapLoaded,
          addingAnnotation: addingAnnotation!==null
        }"></span>
        <div id="map"></div>
      </v-container>

      <v-slide-y-transition>
        <p class="addHint elevation-6" v-if="addingAnnotation">{{ $t('label.addComment') }}</p>
      </v-slide-y-transition>

      <v-btn
        v-if="hash && !screenshotIsThumbnail"
        fab absolute small
        style="bottom:2.2em; right:1.3em;"
        :elevation="mapinfoopen ? 0 : 6"
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
          @click="mapinfoopen=!mapinfoopen">
          mdi-close-circle-outline
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
        v-if="!screenshotMode"
        fab absolute small
        id="myLocation"
        color="primary"
        @click="myLocation">
        <v-icon>mdi-crosshairs-gps</v-icon>
      </v-btn>

      <div v-if="wshash && annotations.open && !screenshotMode">

        <v-btn
          fab absolute small
          id="addingAnnotation"
          color="primary"
          @click="addingAnnotation ? addingAnnotation=null : addingAnnotation='COM'">
          <v-icon v-if="!addingAnnotation">mdi-comment-plus-outline</v-icon>
          <v-icon v-if="addingAnnotation">mdi-close-thick</v-icon>
        </v-btn>

        <v-scale-transition origin="center">
          <div class="commentanimation" v-if="newAnnotation">
            <v-card
              id="commentedit"
              light width="400" class="pa-4 elevation-6"
            >
              <h3>{{ $t('label.newComment') }}</h3>
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
                        :items="annotations.categories"
                        item-text="name"
                        item-value="pk"
                        v-model="newAnnotation.category"
                        :label="$t('label.category')"
                        :rules="[rules.required]"
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
                        :label="$t('label.title')"
                        :rules="[rules.required,rules.maxlength]"
                        counter=30
                        maxlength=35
                        required
                      />
                      <v-text-field
                        v-model="newAnnotation.price"
                        :label="$t('label.price')"
                        :rules="[rules.maxlength]"
                        counter=30
                        maxlength=35
                      />
                      <div class="d-flex justify-space-between">
                        <v-btn
                        @click="cancelAnnotation">
                          {{ $t('btn.cancel') }}
                        </v-btn>
                        <v-btn
                          color="primary"
                          @click="validateStepOne"
                        >
                          {{ $t('btn.next') }}
                        </v-btn>
                      </div>
                    </v-stepper-content>
                    <v-stepper-content
                      step="2"
                      class="pa-0">
                      <p>{{ $t('label.emailhint') }}</p>
                      <v-text-field
                        v-model="newAnnotation.email"
                        :label="$t('label.email')"
                        :rules="[rules.required,rules.email]"
                        maxlength=100
                        required
                      />
                      <v-select
                        :items="usergroups"
                        v-model="newAnnotation.usergroup"
                        :label="$t('label.group')"
                        :rules="[rules.required]"
                        required
                      ></v-select>
                      <p class="small">{{ $t('label.notpublic')}}</p>
                      <div class="d-flex justify-space-between">
                        <v-btn
                        @click="commentstepper = 1">
                          {{ $t('btn.prev') }}
                        </v-btn>
                        <v-btn
                          type="submit"
                          color="primary"
                        >
                          {{ $t('btn.save') }}
                        </v-btn>
                      </div>
                    </v-stepper-content>
                  </v-stepper-items>
                </v-stepper>
              </v-form>
            </v-card>
          </div>
        </v-scale-transition>

        <v-dialog
          v-model="dialog"
          :hide-overlay="true"
          width="320"
        >
          <v-card>
            <v-card-title class="smalltitle">
              {{ dialogcontent.title }}
            </v-card-title>

            <v-card-text>
              {{ dialogcontent.text }}
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                @click="dialog = false"
              >
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>

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
            {{ currentComment.data.properties.price }}
            {{ currentComment.data.properties.description }}
            <br>

            <div
              v-if="annotations.likes"
              class="d-flex align-center justify-end primary--text">
              <p class="rating">
                <v-icon color="primary" small>mdi-heart-outline</v-icon>
                <b
                  style="vertical-align: middle;"
                > {{currentComment.rating}}</b>
              </p>
              <v-btn
                fab x-small color="white"
                :disabled="ratingpause"
                class="primary--text"
                ref="rateupBtn"
                @click="rateUp(currentComment.pk)"
                ><v-icon small>mdi-heart-plus</v-icon></v-btn>
              <v-icon
                id="addHeart"
                v-if="ratingpause"
                small
                color="primary"
                :style="cssVars"
                >mdi-heart</v-icon>
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
.addingAnnotation + #map {
  cursor: crosshair;
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
  right: 1.6em;
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

#myLocation,
#addingAnnotation {
  top: 5.6em;
  right: 1.3em;
  transition: top 0.3s;
  transition-timing-function: ease-in-out;
}
#myLocation {
  transition-delay: 0.1s;
}
#addingAnnotation {
  top: 10em;
}
.navopen #myLocation {
  top: 1.2em;
  transition-delay: 0.3s;
}
.navopen #addingAnnotation {
  top: 5.6em;
  transition-delay: 0.4s;
}

.addHint {
  position: absolute;
  top: -4px;
  left: 50%;
  width: 680px;
  margin-left: -340px;
  text-align: center;
  text-shadow: 0 0 2px #fff, 0 0 5px #fff;
  background: #ffffff;
  padding: 14px 1em 10px 1em;
  border-radius: 4px;
  font-size: 16px;
  line-height: 1.2em;
  z-index: 1001; /* above [+/-] map zoom button */
}

@media (max-width: 700px) {
  .addHint {
    width: 90%;
    left: 5%;
    margin-left: 0;
  }
}
#commentholder {
  position: absolute;
  display: none;
}
.commentanimation {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  height: 400px;
  max-width: 90vw;
  margin: -200px 0 0 -200px;
}
@media (max-width: 420px) {
  .commentanimation {
    width: 90vw;
    margin: -200px 0 0 -45vw;
  }
}
@keyframes fromcircle {
  0% {
    border-radius: 30em;
  }
  100% {
    border-radius: 0;
  }
}
.scale-transition-enter-active #commentedit {
  animation: fromcircle 0.3s 0.1s ease-out;
  animation-fill-mode: both;
}
.scale-transition-leave-active #commentedit {
  animation: fromcircle reverse 0.2s ease-out;
  animation-fill-mode: both;
}

#commentedit {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 510;
  overflow: hidden;
  max-width: 90vw;
}

#currentComment {
  min-width: 200px;
  max-width: calc(90vw - 20px);
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
  font-size: 13px;
  margin-bottom: 0;
  padding-right: 1em;
  user-select: none;
}
#addHeart {
  position: absolute;
  right: 1.2em;
  animation: addHeart 1.2s 0.4s ease-in-out both;
}
@keyframes addHeart {
  0% {
    right: 1.2em;
    scale: 0.6;
    opacity: 0;
  }
  13% {
    opacity: 1;
    scale: 2;
  }
  25% {
    scale: 1.6;
    right: 1.2em;
  }
  70% {
    scale: 1.6;
    right: var(--endpos);
    opacity: 1;
  }
  95% {
    scale: 0.3;
    right: var(--endpos);
  }
  100% {
    opacity: 0;
  }
}

.smalltitle {
  font-size: 16px !important;
}

.leaflet-control-attribution.leaflet-compact-attribution::after {
  content: none;
  display: none;
}
.leaflet-container .leaflet-control-attribution.leaflet-compact-attribution {
  margin: 0;
  visibility: visible;
  padding: 0;
  padding-right: 5px;
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
      usergroups: [this.$t('label.groups.resident'), this.$t('label.groups.tourist')],
      currentCommentIndex: null,
      ratingpause: false,
      dialog: false,
      dialogcontent: {},
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
      commentLockedIconUrl: require('@/assets/images/icons/comment_locked_36.svg'),
      // eslint-disable-next-line global-require
      locationIconUrl: require('@/assets/images/icons/location.svg'),
      setMapMyLocation: false,
      locationWatcher: null,
      myLocationMarker: null,
      rules: {
        required: v => !!v || this.$t('validationError.mandatory'),
        email: v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,4})+$/.test(v) || this.$t('validationError.inv'),
        number: v => /^\d+[.,]?\d{0,2}$/.test(v) || this.$t('validationError.nan'),
        maxlength: v => v.length <= 30 || this.$t('validationError.toolong') // eslint-disable-line no-console
      }
    };
  },

  props: {
    snapshot: Object,
    geojson: Object,
    annotations: Object,
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
    },
    currentComment() {
      if (this.annotations.items) {
        return this.annotations.items[this.currentCommentIndex];
      }
      return null;
    },

    cssVars() {
      let endpos = 4.1;
      if (this.currentComment.rating >= 10) {
        if (this.currentComment.rating >= 100) {
          if (this.currentComment.rating >= 1000) {
            endpos = 5.5;
          } else {
            endpos = 5.1;
          }
        } else {
          endpos = 4.6;
        }
      }
      return { '--endpos': `${endpos}em` };
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
        console.log('remove'); // eslint-disable-line no-console
        document.getElementById('commentholder').append(e.target.getContent());
      });
      this.mapinfoopen = false;
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
        if (this.annotations.items) {
          this.annotations.items = this.annotations.items.map((a, i) => {
            a.data.kind = a.kind;
            a.data.index = i;
            if (a.category) {
              a.data.properties.icon = { iconUrl: `/media/${a.category.icon}`, iconSize: [20, 20], popupAnchor: [0, -10] };
            }
            return a;
          });
          const annotationsdata = this.annotations.items.map(a => a.data);
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
                    iconSize: [20, 20]
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
                console.log('Error - Annotation type not supported'); // eslint-disable-line no-console
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
      this.commentstepper = 1;
      this.newAnnotation = {
        kind: 'COM',
        title: '',
        price: '',
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
              "price": "${this.newAnnotation.price}",
              "usergroup": "${this.newAnnotation.usergroup}"
            }
          }`);
          break;
        }
        default: {
          console.log('Saving this annotation type not supported'); // eslint-disable-line no-console
          return false;
        }
      }
      try {
        const save = await this.$restApi.post('annotations/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': csrftoken
          }
        });
        if (save.status === 201) {
          const marker = this.newAnnotation.marker;
          marker.setIcon(
            new L.Icon({
              iconUrl: this.commentLockedIconUrl,
              iconSize: [36, 36],
              popupAnchor: [0, -16]
            })
          );
          marker.off();
          marker.bindPopup(this.$t('success.commentSaved'));
          this.newAnnotation = null;

          this.dialogcontent = {
            title: this.$t('success.saved'),
            text: this.$t('success.commentSaved')
          };
          this.dialog = true;
        }
        // } else {
        //   console.log('save');
        //   console.log(save);
        //   console.log('Speichern fehlgeschlagen');
        // }
      } catch (error) {
        console.log(error); // eslint-disable-line no-console
        this.dialogcontent = {
          title: this.$t('error.failed'),
          text: this.$t('error.failedText')
        };
        this.dialog = true;
      }
      return true;
    },

    async rateUp(annotationPk) {
      this.ratingpause = true;

      if (this.annotations.open) {
        const csrftoken = this.$cookies.get('csrftoken', '');
        const formData = new FormData();

        const save = await this.$restApi.patch(`rateupannotation/${annotationPk}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': csrftoken
          }
        });
        if (save.status === 200) {
          window.setTimeout(() => {
            this.currentComment.rating = parseInt(save.data.rating, 10);
          }, 1400);
        } else {
          console.log('Speichern fehlgeschlagen'); // eslint-disable-line no-console
        }

        this.$refs.rateupBtn.$el.blur();
        window.setTimeout(() => { this.ratingpause = false; }, 1800);
      }
    },

    myLocation() {
      this.setMapMyLocation = true;
      if (this.locationWatcher === null) {
        this.myLocationMarker = L.marker([0, 0], {
          icon: new L.Icon({
            iconUrl: this.locationIconUrl,
            iconSize: [24, 24]
          }),
          interactive: false
        });
        this.myLocationMarker.addTo(this.map);
        this.locationWatcher = navigator.geolocation.watchPosition((position) => {
          const myLatlng = L.latLng(position.coords.latitude, position.coords.longitude);
          if (this.setMapMyLocation) {
            this.map.setView(myLatlng);
            this.setMapMyLocation = false;
          }
          this.myLocationMarker.setLatLng(myLatlng);
        });
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
