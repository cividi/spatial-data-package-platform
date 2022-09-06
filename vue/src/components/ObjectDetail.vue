<!-- eslint-disable -->
<i18n>
{
  "de": {
    "category":"Kategorie",
    "state": "Status",
    "constructed": "Erbaut",
    "demolished": "Abgerissen",
    "description": "Architektur",
    "moreinfo": "Abrissgrund",
    "comment": "Geschichten und Erinnerungen"
  },
  "fr": {
    "category":"Catégorie",
    "state": "Statut",
    "constructed": "Construit",
    "demolished": "Arraché",
    "description": "Architecture",
    "moreinfo": "Cause de la démolition",
    "comment": "Histoires et souvenirs"
  },
  "en": {
    "category":"Category",
    "state": "Status",
    "constructed": "Built",
    "demolished": "Demolished",
    "description": "Architecture",
    "moreinfo": "Demolition reason",
    "comment": "Stories and memories"
  },
  "it": {
    "category":"Categoria",
    "state": "Stato",
    "constructed": "Costruito",
    "demolished": "Abbattuto",
    "description": "Architettura",
    "moreinfo": "Motivo della demolizione",
    "comment": "Storie e ricordi"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <v-fade-transition>
      <v-overlay v-if="curObj !== null" z-index="505">
        <div
          @click="$emit('close')"
          style="width: 100vw; height: 100vh; cursor: pointer;"
        ></div>
      </v-overlay>
    </v-fade-transition>
    <v-slide-x-transition>
      <div
        v-if="curObj !== null"
        id="objectDetail"
        class="pa-4 elevation-6"
      >
        <div class="smaller">
          <div class="topContainer">
            <v-carousel v-if="curObj.attachements.length > 0"
              height="400px"
              hide-delimiters
              :show-arrows="curObj.attachements.length > 1"
              class="my-1"
              >
              <v-carousel-item eager v-for="(item, i) in curObj.attachements" :key="i"
                :src="djangobaseurl + '/media/' + item.document"
                class="requestable-filter"
                contain></v-carousel-item>
            </v-carousel>

            <div class="objectTitle">
              <h3>{{ curObj.data.properties.title }}</h3>
              <h4>{{ curObj.data.properties.subtitle }}</h4>
            </div>
          </div>

          <v-container class="body-1 mainDetails">
            <v-row class="objectData" v-if="curObj.category.name">
              <v-col class="px-0 py-0">
                <span>{{ $t('category') }}</span> {{ curObj.category.name }}
              </v-col>
            </v-row>
            <v-row class="objectData" v-if="curObj.data.properties.constructionYear">
              <v-col class="px-0 py-1">
                <span>{{ $t('constructed') }}</span> {{ curObj.data.properties.constructionYear }}
              </v-col>
            </v-row>
            <v-row class="objectData" v-if="curObj.data.properties.demolitionYear">
              <v-col class="px-0 py-1">
                <span>{{ $t('demolished') }}</span> {{ curObj.data.properties.demolitionYear }}
              </v-col>
            </v-row>
            <v-row class="objectData" v-if="curObj.data.properties.description">
              <v-col class="px-0 py-1">
                <span>{{ $t('description') }}</span> {{ curObj.data.properties.description }}
              </v-col>
            </v-row>
            <v-row class="objectData" v-if="curObj.data.properties.moreinfo">
              <v-col class="px-0 py-1">
                <span>{{ $t('moreinfo') }}</span> {{ curObj.data.properties.moreinfo }}
              </v-col>
            </v-row>
            <v-row v-if="curObj.category.commentsEnabled || curObj.data.properties.comment">
              <v-col class="px-0 py-0">
                <span>{{ $t('comment') }}</span>
              </v-col>
            </v-row>
            <v-row class="objectData" v-if="curObj.data.properties.comment">
              <v-col class="px-0 py-0">
                <span v-if="curObj.data.properties.commentAuthor">
                  {{ curObj.data.properties.commentAuthor }}
                </span> {{ curObj.data.properties.comment }}
              </v-col>
            </v-row>
            <v-row v-if="curObj.category.commentsEnabled">
              <v-col class="px-0 py-0">
                <div id="commento"></div>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </div>
    </v-slide-x-transition>
  </div>
</template>

<style>
#objectDetail {
  position: fixed;
  top: 0em;
  left: 0;
  width: 48em;
  height: 100vh;
  background: #fff;
  z-index: 1100;
  overflow: auto;
}

.topContainer h3, h4 {
  font-size: 3.5em;
  width: fit-content;
  line-height: 1em;
  text-transform: uppercase;
  border-bottom: 8px solid #000;
  margin-bottom: 0.4em;
}

.v-image__image {
    background-color: transparent !important;
    border: 0 !important;
}

.objectTitle {
  text-transform: uppercase;
  z-index: 1;
}

.topContainer {
  display: grid;
  align-items: start;
  justify-items: left;
}
.topContainer > * {
  grid-area: 1/1/1/1;
}
.requestable-filter {
  filter: grayscale(100%) brightness(110%);
  opacity: 1 !important;
}
.v-application .body-1 {
  font-family: 'Queue', sans-serif !important;
  font-weight: bold;
  line-height: 1.5em;
}
.body-1 span {
  font-family: 'Helvetica Neue LT W05 75 Bold', 'Arial', sans-serif !important;
}
.body-1 span::after {
  content: ":";
}
.row.objectData {
  border-top: 2px solid black;
}
.mainDetails {
  border-bottom: 2px solid black;
}

#commento {
  margin-top: 12px;
}

@media (max-width: 500px) {
  #objectDetail {
    width: calc(100vw - 7em);
  }
}
</style>

<script>
// import Vue from 'vue';

export default {
  name: 'ObjectDetail',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      commentoUrl: process.env.VUE_APP_COMMENTO_URL || null
    };
  },

  props: {
    object: Object,
    enableLikes: Boolean
  },

  updated() {
    if (this.commentoUrl !== null && this.curObj.category.commentsEnabled) {
      if (typeof window !== 'undefined' && window.commento.main === undefined) {
        const commentoScript = document.createElement('script');
        commentoScript.setAttribute('src', `${this.commentoUrl}/js/commento.js`);
        commentoScript.setAttribute('data-auto-init', false);
        commentoScript.setAttribute('data-no-fonts', true);
        commentoScript.setAttribute('data-locale', this.$route.params.lang);
        commentoScript.setAttribute('data-page-id', `/${this.$route.params.wshash}/${this.curObj.pk}/`);
        commentoScript.setAttribute('data-css-override', '/commento.css');
        commentoScript.setAttribute('data-hide-deleted', true);
        commentoScript.setAttribute('defer', true);
        document.head.appendChild(commentoScript);
        window.setTimeout(() => {
          window.commento.main();
        }, 700);
      } else if (typeof window !== 'undefined' && window.commento) {
        window.commento.reInit({
          pageId: `/${this.$route.params.wshash}/${this.curObj.pk}/`
        });
      }
    }
  },

  computed: {
    djangobaseurlDisplay() {
      return this.djangobaseurl.replace('https://', '').replace('http://', '');
    },
    curObj() {
      if (this.object) {
        return this.object;
      }
      return null;
    }
  }
};
</script>
