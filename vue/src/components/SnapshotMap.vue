<!-- eslint-disable -->
<i18n>
{
  "de": {
    "participation": {
      "categoryLabel": "Kategorie",
      "annotation": {
        "add": "Klicken Sie auf die Stelle in Karte an der Sie einen Kommentar hinzufügen möchten.",
        "new": "Neuer Kommentar",
        "emailhint": "Um Ihren Kommentar freizuschalten, schicken wir Ihnen eine Email mit einem Aktivierungslink. Bitte geben Sie Ihre Email Adresse an:",
        "commentSaved": "Ihr Kommentar wurde gespeichert. Klicken Sie den Link in der Email um ihn freizuschalten."
      },
       "polygon": {
        "add": "Klicken Sie auf die Stelle in Karte an der Sie einen Kommentar hinzufügen möchten.",
        "editing": {
          "invalid": "Ungültige Geometrie, hinzufügen dieses Punktes möglich.",
          "unfinished": "Klicken Sie erneut auf den Startpunkt, um den Kommentar abzuschliessen",
          "closable": "Klicken Sie hier, um den Kommentar abzuschliessen."
        }
      }
    },
    "areamanagement": {
      "categoryLabel": "Status",
      "note": {
        "add": "Klicken Sie auf die Stelle in Karte an der Sie eine Notiz hinzufügen möchten.",
        "new": "Neue Notiz",
        "emailhint": "Um Ihren Notiz freizuschalten, schicken wir Ihnen eine Email mit einem Aktivierungslink. Bitte geben Sie Ihre Email Adresse an:",
        "commentSaved": "Ihre Notiz wurde gespeichert. Klicken Sie den Link in der Email um ihn freizuschalten."
      },
      "polygon": {
        "add": "Klicken Sie auf die Stelle in Karte an der Sie eine Fläche hinzufügen möchten.",
        "editing": {
          "invalid": "Ungültige Geometrie, hinzufügen dieses Punktes möglich.",
          "unfinished": "Klicken Sie erneut auf den Startpunkt, um die Fläche abzuschliessen",
          "closable": "Klicken Sie hier, um die Fläche abzuschliessen."
        },
        "new": "Neue Fläche",
        "emailhint": "Um Ihren Fläche freizuschalten, schicken wir Ihnen eine Email mit einem Aktivierungslink. Bitte geben Sie Ihre Email Adresse an:",
        "commentSaved": "Ihre Fläche wurde gespeichert. Klicken Sie den Link in der Email um ihn freizuschalten."
      }
    },
    "title": "Titel",
    "text":"Text",
    "cancel": "abbrechen",
    "next": "weiter",
    "prev": "zurück",
    "save": "speichern",
    "saveinfo": "Speichere Angaben",
    "mandatory": "Dies ist ein Pflichtfeld",
    "email": "E-Mail",
    "inv": "Dies ist keine gültige E-Mail Adresse",
    "notpublic":"Diese Informationen werden nicht veröffentlicht oder an Dritte weitergegeben",
    "failed": "Speichern fehlgeschlagen",
    "failedText": "Bitte prüfen Sie Ihre Eingaben oder versuchen Sie es später nochmals.",
    "saved": "Speichern erfolgreich"
  },
  "fr": {
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

      <v-container fluid class="pa-0" ref="mapbox" @mousemove="onMouseMove">
        <span id="mapstatus" :class="{
          loaded: isMapLoaded,
          waiting: !isMapLoaded,
          addingAnnotation: addingAnnotation!==null
        }"></span>
        <div id="map"></div>
      </v-container>

      <v-slide-y-transition>
        <p class="addHint elevation-6" v-if="addingAnnotation">
          <span v-if="annotations.mode == 'PAR'">
            <span v-if="polygonEditingState.invalid">
              {{ $t('participation.polygon.editing.invalid') }}</span>
            <span v-else-if="polygonEditingState.closable">
              {{ $t('participation.polygon.editing.closable') }}</span>
            <span v-else-if="polygonEditingState.active">
              {{ $t('participation.polygon.editing.unfinished') }}</span>
            <span v-else>
              {{ $t('participation.annotation.add') }}</span>
          </span>
          <span v-else-if="annotations.mode == 'MGT' && addingAnnotation == 'PLY'">
            <span v-if="polygonEditingState.invalid">
              {{ $t('areamanagement.polygon.editing.invalid') }}</span>
            <span v-else-if="polygonEditingState.closable">
              {{ $t('areamanagement.polygon.editing.closable') }}</span>
            <span v-else-if="polygonEditingState.active">
              {{ $t('areamanagement.polygon.editing.unfinished') }}</span>
            <span v-else>
              {{ $t('areamanagement.polygon.add') }}</span>
          </span>
          <span v-else-if="annotations.mode == 'MGT' && addingAnnotation == 'COM'">
            {{ $t('areamanagement.note.add') }}</span>
        </p>
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
          :legendAnnotations="legendAnnotations"
          :sources="sources"
        />
      </v-card>

      <v-btn
        v-if="!screenshotMode && annotations.findme"
        fab absolute small
        id="myLocation"
        color="primary"
        @click="myLocation">
        <v-icon>mdi-crosshairs-gps</v-icon>
      </v-btn>

      <div v-if="wshash && !screenshotMode">

        <v-btn
          fab absolute small
          id="addingAnnotationPt"
          color="primary"
          v-if="annotations.marker.open"
          @click="addingAnnotation ? addingAnnotation=null : addingAnnotation='COM';">
          <v-icon v-if="!addingAnnotation || addingAnnotation != 'COM'">
            mdi-comment-plus-outline
          </v-icon>
          <v-icon v-if="addingAnnotation && addingAnnotation == 'COM'">mdi-close-thick</v-icon>
        </v-btn>

        <v-btn
          fab absolute small
          id="addingAnnotationPly"
          color="primary"
          v-if="annotations.polygon.open"
          @click="addingAnnotation ? addingAnnotation = null : addingAnnotation = 'PLY';">
          <v-icon v-if="!addingAnnotation || addingAnnotation != 'PLY'">
            mdi-shape-polygon-plus
          </v-icon>
          <v-icon v-if="addingAnnotation && addingAnnotation == 'PLY'">mdi-close-thick</v-icon>
        </v-btn>

        <v-scale-transition origin="center">
          <div class="commentanimation" v-if="newAnnotation">
            <v-card
              id="commentedit"
              light width="400" class="pa-4 elevation-6"
            >
              <h3>
                <span v-if="annotations.mode == 'PAR'">
                  {{ $t('participation.annotation.new') }}</span>
                <span v-else-if="annotations.mode == 'MGT' && newAnnotation.kind == 'PLY'">
                  {{ $t('areamanagement.polygon.new') }}</span>
                <span v-else-if="annotations.mode == 'MGT' && newAnnotation.kind == 'COM'">
                  {{ $t('areamanagement.note.new') }}</span>
              </h3>
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
                        :items="categoriesList"
                        item-text="name"
                        item-value="pk"
                        v-model="newAnnotation.category"
                        :label="formLabel('categoryLabel')"
                        :rules="[v => !!v || $t('mandatory')]"
                        required
                      >
                        <template slot="item" slot-scope="data">
                          <img
                            v-if="annotations.mode === 'PAR'"
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
                    <v-stepper-content
                      step="2"
                      class="pa-0">
                      <p v-if="annotations.mode == 'PAR'">
                        {{ $t('participation.annotation.emailhint') }}</p>
                      <p v-else-if="annotations.mode == 'MGT' && newAnnotation.kind == 'PLY'">
                        {{ $t('areamanagement.polygon.emailhint') }}</p>
                      <p v-else-if="annotations.mode == 'MGT' && newAnnotation.kind == 'COM'">
                        {{ $t('areamanagement.note.emailhint') }}</p>
                      <v-text-field
                        v-model="newAnnotation.email"
                        :label="$t('email')"
                        :rules="[
                          v => !!v || $t('mandatory'),
                          v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,4})+$/.test(v) || $t('inv')]"
                        required
                      />
                      <v-select
                        :items="annotations.usergroups"
                        item-text="name"
                        item-value="key"
                        v-model="newAnnotation.usergroup"
                        label="Personengruppe"
                        :rules="[v => !!v || $t('mandatory')]"
                        required
                      ></v-select>
                      <p class="small">{{ $t('notpublic')}}</p>
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

      <div id="polygonstatisticsholder" v-if="statisticPanelOpen">
        <div v-for="(statistic, key) in spatialData" :key="key">
          <h2>{{ queriesData[key].title }}</h2>
          <div>
            <h3>Polygon</h3>
            <div class="progress-container">
              <div class="progress-indicator"
                :style="{ width: statistic.polygon.progress + '%'
                  }">
                {{ statistic.polygon.label }}</div>
            </div>
          </div>
          <!-- <div>
            <h3>Quartier</h3>
            <div class="progress-container">
              <div class="progress-indicator"
                :style="{ width:
                  statistic.neighbourhood.progress + '%'
                  }">
                {{ statistic.neighbourhood.label }}</div>
            </div>
          </div> -->
          <div>
            <h3>Stadt</h3>
            <div class="progress-container">
              <div class="progress-indicator"
                :style="{ width:
                  statistic.all.progress + '%'
                  }">
                {{ statistic.all.label }}</div>
            </div>
          </div>
        </div>
      </div>

      <div id="commentholder">
        <div id="currentComment" :class="{withComments: withComments}">
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
            <div
              v-if="annotations.mode == 'MGT' && currentComment.kind == 'PLY'">
              Status:
              <span
                class="statusLabel"
                :style="{ 'background-color': currentComment.category.color }">
                {{currentComment.category.name}}
              </span><br>
              Fläche: ca. {{currentComment.data.properties.area}}
            </div>
            {{currentComment.data.properties.description}}<br>

            <div
              v-if="(annotations.marker.likes && currentComment.kind == 'COM') ||
                (annotations.polygon.likes && currentComment.kind == 'PLY')"
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
              <div v-if="currentComment.category.commentsEnabled">
                <h3>Kommentare</h3>
                <div id="commento"></div>
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
#addingAnnotationPt,
#addingAnnotationPly {
  top: 5.6em;
  right: 1.3em;
  transition: top 0.3s;
  transition-timing-function: ease-in-out;
}
#myLocation {
  transition-delay: 0.1s;
}
#addingAnnotationPt {
  top: 10em;
}
#addingAnnotationPly {
  top: 14.4em;
}

span.statusLabel {
  padding: 1px 4px;
  border: 1px solid #000;
  border-radius: 4px;
}

.navopen #myLocation {
  top: 1.2em;
  transition-delay: 0.3s;
}
.navopen #addingAnnotationPt {
  top: 5.6em;
  transition-delay: 0.4s;
}
.navopen #addingAnnotationPly {
  top: 10em;
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
  width: 200px;
  max-width: calc(90vw - 20px);
  overflow: scroll;
}
#currentComment.withComments {
  width: 380px !important;
  max-height: 40vh;
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

#polygonstatisticsholder {
  width: 320px;
  height: 96vh;
  z-index: 500;
  display: block;
  top: 15px;
  right: 15px;
  position: fixed;
  background: white;
  border-radius: 4px;
  padding: 10px 8px;
  box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2),
    0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);
  overflow-y: scroll;
}

#polygonstatisticsholder h2 {
  font-size: 2.2em;
  padding-top: 5px;
  padding-bottom: 5px;
}

#polygonstatisticsholder h3 {
  font-size: 1.5em;
}

.progress-container {
  width: 100%;
  max-width: 300px;
  border: 1px solid #ccc;
  border-radius: 10px;
}

.progress-indicator {
  background: black;
  border-radius: 10px;
  min-height: 20px;
  text-align: center;
  color: white;
  font-size: 12px;
  padding: 1px 0;
  min-width: 50px;
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
      polygonEditingState: {
        active: false,
        invalid: false,
        closable: false
      },
      polygonString: [],
      drawnItems: null,
      spatialData: {},
      statisticPanelOpen: false,
      tooltipContainer: null,
      timeout: null,
      guides: null,
      commentstepper: 1,
      currentCommentIndex: null,
      ratingpause: false,
      dialog: false,
      dialogcontent: {},
      title: '',
      description: '',
      legend: [],
      legendAnnotations: [],
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
      escListener: null,
      commentoUrl: process.env.VUE_APP_COMMENTO_URL || null
    };
  },

  props: {
    snapshot: Object,
    geojson: Object,
    annotations: Object,
    spatialDatasettes: Array,
    geoboundsIn: Array,
    predecessor: Object
  },

  created() {
    this.geobounds = this.geoboundsIn;
    this.escListener = document.addEventListener('keyup', (e) => {
      if (e.key === 'Escape') {
        this.cancelAnnotation();
      }
    });
  },

  destroy() {
    this.destroyMap();
    document.removeEventListener(this.escListener);
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

    withComments() {
      if (this.currentComment) {
        return this.currentComment.category.commentsEnabled;
      }
      return false;
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
    },

    categoriesList() {
      if (this.$store.state.isUserLoggedIn) {
        return this.annotations.categories;
      }
      return this.annotations.categories.filter(a => !a.hideInList);
    },

    queries() {
      return this.spatialDatasettes[0].queries.map(
        item => item.name
      );
    },

    queriesData() {
      const qd = {};
      this.spatialDatasettes[0].queries.forEach((i) => {
        qd[i.name] = { ...i };
      });
      return qd;
    },

    token() {
      return `${process.env.VUE_APP_SPATIALDATASETTE_TOKEN}` || null;
    }
  },

  methods: {
    createFeatureLayer(geojson, attribution, points = true) {
      let features;
      if (points) {
        features = L.geoJson(geojson, {
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
      } else {
        features = L.featureGroup(
          geojson.map((polygon) => {
            const poly = new L.Polygon(
              polygon.geometry.coordinates[0].map(
                c => [c[1], c[0]]
              ),
              {
                ...polygon.properties
              }
            );
            poly.feature = polygon;
            if (polygon.properties.title || polygon.properties.description) {
              poly.on('click', this.showPopup);
            }
            return poly;
          })
        );
        console.log(features); // eslint-disable-line no-console
      }
      return features;
    },

    showPopup(e) {
      let content;
      let latlng;
      if (e.target.feature.kind === 'COM') {
        this.currentCommentIndex = e.target.feature.index;
        content = document.getElementById('currentComment');
        latlng = e.target._latlng; // eslint-disable-line no-underscore-dangle
      } else if (e.target.feature.kind === 'PLY') {
        this.currentCommentIndex = e.target.feature.index;
        content = document.getElementById('currentComment');
        latlng = e.target.getCenter(); // eslint-disable-line no-underscore-dangle
        // content = e.target.feature.properties.description;
        // if (e.target.feature.properties.title) {
        //   content = `<b>${e.target.feature.properties.title}</b><br />${content}`;
        // }
      } else {
        content = e.target.feature.properties.description;
        if (e.target.feature.properties.title) {
          content = `<b>${e.target.feature.properties.title}</b><br />${content}`;
        }
        latlng = e.target._latlng; // eslint-disable-line no-underscore-dangle
      }
      const myPopup = new L.Popup({ maxWidth: 450, maxHeight: 600 })
        .setLatLng(latlng)
        .setContent(content);

      myPopup.on('remove', (e) => {
        // console.log('remove'); // eslint-disable-line no-console
        document.head.getElementsByTagName('script').forEach((el) => {
          if (el.hasAttribute('data-page-id')) {
            document.head.removeChild(el);
          }
        });
        document.getElementById('commentholder').append(e.target.getContent());
        this.statisticPanelOpen = false;
        this.resetSpatialData();
      });
      this.mapinfoopen = false;
      window.setTimeout(() => {
        myPopup.openOn(this.map);
        if (this.commentoUrl !== null && this.currentComment.category.commentsEnabled) {
          console.log(window); // eslint-disable-line no-console
          console.log(window.commento); // eslint-disable-line no-console
          console.log(window.commento.main); // eslint-disable-line no-console
          if (typeof window !== 'undefined' && window.commento.main === undefined) {
            const commentoScript = document.createElement('script');
            commentoScript.setAttribute('src', `${this.commentoUrl}/js/commento.js`);
            commentoScript.setAttribute('data-auto-init', false);
            commentoScript.setAttribute('data-page-id', `${this.currentComment.pk}-${this.currentComment.id}`);
            commentoScript.setAttribute('defer', true);
            document.head.appendChild(commentoScript);
            window.setTimeout(() => {
              window.commento.main();
            }, 100);
          } else if (typeof window !== 'undefined' && window.commento) {
            window.commento.reInit({
              pageId: `${this.currentComment.pk}-${this.currentComment.id}`
            });
          }
        }
      }, 100);

      if (this.spatialDatasettes && e.target.feature.kind === 'PLY') {
        this.statisticPanelOpen = true;
        const coordinates = this.currentComment.data.geometry.coordinates[0].map(i => `${i[0]} ${i[1]}`).join(', ');
        const wkt = `Polygon ((${coordinates}))`;
        this.queries.forEach((q) => {
          this.fetchPolygonStats(
            this.spatialDatasettes[0], q,
            wkt, '', 'all'
          );
          this.fetchPolygonStats(
            this.spatialDatasettes[0], q,
            wkt, '', 'polygon'
          );
        });
      }
    },

    setupEmpty() {
      this.geobounds = this.geoboundsIn;
    },

    setupMeta() {
      this.title = this.geojson.views[0].spec.title;
      this.description = this.geojson.views[0].spec.description;
      this.legend = this.geojson.views[0].spec.legend;
      if (this.annotations.mode !== 'OFF') {
        const extraItems = this.annotations.categories
          .filter(c => !c.hideInLegend)
          .map((c) => {
            if (c.icon !== '') {
              return {
                svg: `/media/${c.icon}`,
                label: c.name,
                primary: !c.hideInList
              };
            }
            return {
              label: c.name,
              primary: !c.hideInList,
              shape: 'circle',
              size: 1.0,
              fillColor: c.color,
              fillOpacity: 0.4,
              strokeColor: c.color,
              strokeOpacity: 0.9,
              strokeWidth: 2
            };
          });
        this.legendAnnotations = [...extraItems];
      }
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
              a.data.properties.icon = { iconUrl: `/media/${a.category.icon}`, iconSize: [36, 36], popupAnchor: [0, -16] };
              if (a.kind === 'PLY') {
                const area = this.geodesicArea(
                  a.data.geometry.coordinates[0].map(
                    c => L.latLng([c[1], c[0]])
                  )
                );
                a.data.properties = {
                  ...a.data.properties,
                  color: a.category.color,
                  opacity: 0.9,
                  weight: 3,
                  dashArray: '8 6',
                  dashOffset: '8',
                  fillColor: a.category.color,
                  fillOpacity: 0.4,
                  area
                };
              }
            }
            return a;
          });
          const annotationsdata = this.annotations.items.map(a => a.data);
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata.filter(a => a.kind === 'COM'), ''
          ));
          this.layerContainer.addLayer(this.createFeatureLayer(
            annotationsdata.filter(a => a.kind === 'PLY'), '', false
          ));
        }
        this.layerContainer.addTo(this.map);

        this.drawnItems = new L.FeatureGroup();
        this.drawnItems.addTo(this.map);

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
                this.addingAnnotation = null;
                break;
              }
              case 'PLY': {
                this.polygonEditingState.active = true;
                // 1.
                // On each click while in Polygon mode
                // record click series
                const newMarker = event.latlng;
                this.polygonString = [...this.polygonString, [newMarker.lat, newMarker.lng]];

                // 2.
                // Update Marker / Polygon rendering
                // from curent list of points
                if (this.polygonString.length === 1) {
                  L.polyline(
                    this.polygonString,
                    {
                      stroke: true,
                      color: '#543076',
                      weight: 3,
                      opacity: 0.9,
                      lineCap: 'round',
                      lineJoin: 'round',
                      dashArray: '8 6',
                      dashOffset: '8',
                      fill: true,
                      fillColor: '#543076',
                      fillOpacity: 0.4
                    }
                  ).addTo(this.drawnItems);
                } else if (this.polygonString.length >= 2) {
                  // calculate distance to starting point
                  const distanceToStart = this.map.latLngToLayerPoint(
                    event.latlng
                  ).distanceTo(
                    this.map.latLngToLayerPoint(this.polygonString[0])
                  );

                  // check if point is close to starting point
                  if (Math.abs(distanceToStart) < 9 * (window.devicePixelRatio || 1)) {
                    // set new point exactly to starting point
                    this.polygonString[this.polygonString.length - 1] = this.polygonString[0];
                    // add new marker
                    const newMarker = L.polyline(
                      this.polygonString,
                      {
                        stroke: true,
                        color: '#543076',
                        weight: 3,
                        opacity: 0.9,
                        lineCap: 'round',
                        lineJoin: 'round',
                        dashArray: '8 6',
                        dashOffset: '8',
                        fill: true,
                        fillColor: '#543076',
                        fillOpacity: 0.4
                      }
                    );
                    newMarker.on('click', this.newPolygon);
                    newMarker.addTo(this.map);
                    // this.map.setView(event.latlng);
                    window.setTimeout(() => { newMarker.fire('click'); }, 500);
                    this.cancelAnnotation();
                    this.polygonEditingState.active = false;
                  } else {
                    const drawingLayer = this.drawnItems.getLayers();
                    const layer = drawingLayer[0];
                    layer.addLatLng(
                      this.polygonString[this.polygonString.length - 1]
                    );
                    layer.redraw();
                  }
                }

                // todo: implement invisible marker to avoid collisions

                break;
              }
              default: {
                this.addingAnnotation = null;
                console.log('Error - Annotation type not supported'); // eslint-disable-line no-console
              }
            }
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

    geodesicArea(latLngs) {
      // ported from https://github.com/Leaflet/Leaflet.draw/blob/develop/src/ext/GeometryUtil.js

      const pointsCount = latLngs.length;
      const d2r = Math.PI / 180;
      let p1 = [];
      let p2 = [];
      let area = 0.0;

      if (pointsCount > 2) {
        for (let i = 0; i < pointsCount; i += 1) {
          p1 = latLngs[i];
          p2 = latLngs[(i + 1) % pointsCount];
          area += ((p2.lng - p1.lng) * d2r)
            * (2 + Math.sin(p1.lat * d2r) + Math.sin(p2.lat * d2r));
        }
        area = area * 6378137.0 * 6378137.0 / 2.0;
      }

      area = Math.round(Math.abs(area));
      let areaStr = '';

      if (area >= 1000000) {
        areaStr = `${area * 0.000001} km²`;
      } else {
        areaStr = `${area} m²`;
      }

      return areaStr;
    },

    onMouseMove(e) {
      if (this.addingAnnotation) {
        const newPos = this.map.mouseEventToLayerPoint(e);
        const latlng = this.map.layerPointToLatLng(newPos);
        const pos = this.map.latLngToLayerPoint(latlng);

        if (this.polygonString.length > 0) {
          const distanceToStart = pos.distanceTo(
            this.map.latLngToLayerPoint({
              lat: this.polygonString[0][0],
              lng: this.polygonString[0][1]
            })
          );
          const withinReach = Math.abs(distanceToStart) < 9 * (window.devicePixelRatio || 1);

          this.polygonEditingState.closable = this.polygonString.length > 1 ? withinReach : false;

          // todo: detect invalid, e.g. self-intersecting geomtries and set flag

          // this.updateTooltip(pos, `
          //   Position: ${latlng} / ${pos}<br>
          //   Distance: ${distanceToStart}<br>Within reach: ${withinReach}
          // `);
          this.updateGuideline(latlng);
        }
      }
    },

    updateGuideline(pos) {
      if (this.timeout) clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        this.drawGuideline(pos);
      }, 5);
    },

    updateTooltip(pos, text) {
      if (this.tooltipContainer === null) {
        this.tooltipContainer = L.DomUtil.create(
          // eslint-disable-next-line no-underscore-dangle
          'div', 'leaflet-draw-tooltip', this.map._panes.popupPane
        );
      }

      if (pos) {
        const tooltipContainer = this.tooltipContainer;
        L.DomUtil.setPosition(tooltipContainer, pos);
      }

      this.tooltipContainer.innerHTML = text;
    },

    drawGuideline(latlng) {
      if (this.polygonString.length >= 1 && this.addingAnnotation) {
        const endPoint = latlng;

        const drawingLayer = this.drawnItems.getLayers();
        const layer = drawingLayer[0];

        let currentPolylineString = [];
        if (!layer.isEmpty()) {
          currentPolylineString = layer.getLatLngs();
        } else {
          currentPolylineString = this.polygonString;
        }

        if (currentPolylineString.length > this.polygonString.length) {
          // update
          currentPolylineString[currentPolylineString.length - 1] = endPoint;
          layer.setLatLngs(
            currentPolylineString
          );
        } else {
          // add
          layer.addLatLng(endPoint);
        }
        layer.redraw();
      }
      // console.log(e); // eslint-disable-line no-console
    },

    newComment(e) {
      this.commentstepper = 1;
      this.newAnnotation = {
        kind: 'COM',
        title: '',
        text: '',
        marker: e.target
      };
    },

    newPolygon(e) {
      this.commentstepper = 1;
      this.newAnnotation = {
        kind: 'PLY',
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
      if (this.newAnnotation && this.newAnnotation.marker) {
        this.newAnnotation.marker.removeFrom(this.map);
        this.newAnnotation = null;
      }
      this.polygonString = [];
      this.drawnItems.clearLayers();
      this.addingAnnotation = null;
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
          const data = {
            type: 'Feature',
            geometry: {
              type: 'Point',
              coordinates: [latlng.lng, latlng.lat]
            },
            properties: {
              fill: true,
              title: this.newAnnotation.title,
              description: this.newAnnotation.text
            }
          };
          formData.append('category', this.newAnnotation.category);
          formData.append('author_email', this.newAnnotation.email);
          formData.append('usergroup', this.newAnnotation.usergroup);
          formData.append('data', JSON.stringify(data));
          break;
        }
        case 'PLY': {
          const data = {
            type: 'Feature',
            geometry: {
              type: 'Polygon',
              coordinates: [[
                ...this.newAnnotation.marker.getLatLngs().map(
                  latlng => [latlng.lng, latlng.lat]
                )
              ]]
            },
            properties: {
              title: this.newAnnotation.title,
              description: this.newAnnotation.text
            }
          };
          formData.append('category', this.newAnnotation.category);
          formData.append('author_email', this.newAnnotation.email);
          formData.append('usergroup', this.newAnnotation.usergroup);
          formData.append('data', JSON.stringify(data));
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
          let labelPath = 'participation.annotation';
          if (this.newAnnotation.kind === 'COM') {
            marker.setIcon(
              new L.Icon({
                iconUrl: this.commentLockedIconUrl,
                iconSize: [36, 36],
                popupAnchor: [0, -16]
              })
            );
            marker.off();
            labelPath = this.annotations.mode === 'MGT' ? 'areamanagement.note' : labelPath;
          } else if (this.newAnnotation.kind === 'PLY') {
            marker.setStyle({
              opacity: 0.6,
              fillOpacity: 0.2
            });
            marker.off();
            labelPath = this.annotations.mode === 'MGT' ? 'areamanagement.polygon' : labelPath;
          }
          marker.bindPopup(this.$t('commentSaved'));
          this.newAnnotation = null;

          this.dialogcontent = {
            title: this.$t('saved'),
            text: this.$t(`${labelPath}.commentSaved`)
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
          title: this.$t('failed'),
          text: this.$t('failedText')
        };
        this.dialog = true;
      }
      return true;
    },

    async rateUp(annotationPk) {
      this.ratingpause = true;

      if (this.annotations.polygon.likes || this.annotations.marker.likes) {
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
    },

    fetchPolygonStats(db, query, polygon, neighbourhood, scope) {
      if (scope === 'all') {
        polygon = '';
        neighbourhood = '';
      } else if (scope === 'neighbourhood') {
        polygon = '';
      } else {
        neighbourhood = '';
      }
      return fetch(`${db.baseUrl}/${query}.json?_shape=objects&polygon=${polygon}&neighbourhood=${neighbourhood}`, {
        method: 'get',
        headers: {
          'content-type': 'application/json',
          Authorization: `Bearer ${this.token}`
        }
      })
        .then((res) => {
          // a non-200 response code
          if (!res.ok) {
            // create error instance with HTTP status text
            const error = new Error(res.statusText);
            error.json = res.json();
            throw error;
          }
          return res.json();
        })
        .then((json) => {
          // set the response data
          this.spatialData[query][scope] = json.rows[0];
          this.spatialData[query][scope].progress = Math.round(
            this.spatialData[query][scope][
              this.queriesData[
                query
              ].summary_stat
            ] / this.queriesData[query].summary_compare * 100
          );
          this.spatialData[query][scope].label = Math.round(
            this.spatialData[query][scope][
              this.queriesData[
                query
              ].summary_stat
            ] * 100
          ) / 100;
        })
        .catch((err) => {
          // error.value = err;
          if (err.json) {
            return err.json; // .then((json) => {
            // error.value.message = json.message;
            // });
          }
          return null;
        });
    },

    resetSpatialData() {
      const facets = { all: {}, neighbourhood: {}, polygon: {} };
      // eslint-disable-next-line no-return-assign
      const filled = {};
      this.queries.forEach((q) => {
        filled[q] = { ...facets };
      });
      this.spatialData = filled;
    },

    formLabel(label) {
      return this.annotations.mode === 'PAR' ? this.$t(`participation.${label}`) : this.$t(`areamanagement.${label}`);
    }
  },

  watch: {
    spatialDatasettes() {
      this.resetSpatialData();
    }
  }
};
</script>
