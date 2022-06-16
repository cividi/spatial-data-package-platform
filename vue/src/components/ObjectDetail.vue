<!-- eslint-disable -->
<i18n>
{
  "de": {
    "category":"Kategorie:",
    "state": "Status:",
    "constructed": "Erbaut:",
    "demolished": "Abgerissen:",
    "description": "Architektur",
    "moreinfo": "Abrissgrund",
    "comment": "Geschichten und Erinnerungen"
  },
  "fr": {
    "category":"Catégorie:",
    "state": "Statut:",
    "constructed": "Construit:",
    "demolished": "Arraché:",
    "description": "Architecture",
    "moreinfo": "Cause de la démolition",
    "comment": "Histoires et souvenirs"
  },
  "en": {
    "category":"Category:",
    "state": "Status:",
    "constructed": "Built:",
    "demolished": "Demolished:",
    "description": "Architecture",
    "moreinfo": "Demolition reason",
    "comment": "Stories and memories"
  },
  "it": {
    "category":"Categoria:",
    "state": "Stato:",
    "constructed": "Costruito:",
    "demolished": "Abbattuto:",
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
          <v-carousel v-if="curObj.attachements.length > 0" height="auto" hide-delimiters
            :show-arrows="curObj.attachements.length > 1" class="my-1">
            <v-carousel-item eager v-for="(item, i) in curObj.attachements" :key="i"
              :src="djangobaseurl + '/media/' + item.document"></v-carousel-item>
          </v-carousel>

          <h3>{{ curObj.data.properties.title }}</h3>
          <h4>{{ curObj.data.properties.subtitle }}</h4>

          <p>
            {{ $t('category') }}
            <span>
              {{ curObj.category.name }}
            </span>
          </p>
          <p v-if="curObj.state">
            {{ $t('state') }}
            <span>
              {{ curObj.state.name }}
            </span>
          </p>
          <v-container v-if="
            curObj.data.properties.constructionYear ||
            curObj.data.properties.demolitionYear"
            class="pa-0"
          >
            <v-row>
              <v-col v-if="curObj.data.properties.constructionYear">
                <p>
                  {{ $t('constructed') }}
                  <span>
                    {{ curObj.data.properties.constructionYear }}
                  </span>
                </p>
              </v-col>
              <v-col v-if="curObj.data.properties.demolitionYear">
                <p>
                  {{ $t('demolished') }}
                  <span>
                    {{ curObj.data.properties.demolitionYear }}
                  </span>
                </p>
              </v-col>
            </v-row>
          </v-container>

          <div v-if="curObj.data.properties.description">
            <h5>{{ $t('description') }}</h5>
            <p>{{ curObj.data.properties.description }}</p>
          </div>
          <div v-if="curObj.data.properties.moreinfo">
            <h5>{{ $t('moreinfo') }}</h5>
            <p>{{ curObj.data.properties.moreinfo }}</p>
          </div>

          <div v-if="enableLikes" class="d-flex align-center justify-end primary--text">
            <p class="rating">
              <v-icon color="primary" small>mdi-heart-outline</v-icon>
              <b style="vertical-align: middle;"> {{ curObj.rating }}</b>
            </p>
            <v-btn fab x-small color="white" :disabled="ratingpause"
              class="primary--text" ref="rateupBtn"
              @click="rateUp(curObj.pk)">
              <v-icon small>mdi-heart-plus</v-icon>
            </v-btn>
            <v-icon id="addHeart" v-if="ratingpause" small color="primary"
              :style="cssVars">mdi-heart</v-icon>
          </div>
          <div v-if="curObj.category.commentsEnabled">
            <h3>{{ $t('comment') }}</h3>
            <div v-if="curObj.data.properties.comment">
              <p>
                <span v-if="curObj.data.properties.commentAuthor">
                  {{ curObj.data.properties.commentAuthor }}: </span>
                {{ curObj.data.properties.comment }}
              </p>
            </div>
            <div id="commento"></div>
          </div>
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
        commentoScript.setAttribute('data-page-id', `/${this.$route.params.wshash}/${this.curObj.pk}/`);
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
