<!-- eslint-disable -->
<i18n>
{
  "de": {
  },
  "fr": {
  },
  "en": {
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <v-fade-transition>
    <v-overlay v-if="curObj !== null">
      <div
        @click="$emit('close')"
        style="width: 100vw; height: 100vh; cursor: pointer;"
      >close</div>
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
            Kategorie:
            <span>
              {{ curObj.category.name }}
            </span>
          </p>
          <p v-if="curObj.state">
            Status:
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
                  Erbaut:
                  <span>
                    {{ curObj.data.properties.constructionYear }}
                  </span>
                </p>
              </v-col>
              <v-col v-if="curObj.data.properties.demolitionYear">
                <p>
                  Abgerissen:
                  <span>
                    {{ curObj.data.properties.demolitionYear }}
                  </span>
                </p>
              </v-col>
            </v-row>
          </v-container>

          <p>{{ curObj.data.properties.description }}</p>
          <p>{{ curObj.data.properties.moreinfo }}</p>

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
            <h3>Kommentare</h3>
            <div id="commento"></div>
          </div>
        </div>
      </div>
    </v-slide-x-transition>
  </div>
</template>

<style>
#objectDetail {
  position: absolute;
  top: 0em;
  left: -32em;
  width: 48em;
  height: 100vh;
  background: #fff;
  z-index: 1100;
  overflow: auto;
}
</style>

<script>
// import Vue from 'vue';

export default {
  name: 'ObjectDetail',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL
    };
  },

  props: {
    object: Object,
    enableLikes: Boolean
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
