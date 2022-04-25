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
  <div
    id="objectDetail"
    v-if="curObj"
    transition="slide-x-transition"
  >
    <b>{{curObj.data.properties.title}}</b><br>
    <v-carousel
      v-if="curObj.attachements.length > 0"
      height="auto"
      hide-delimiters
      class="my-1">
      <v-carousel-item
        v-for="(item,i) in curObj.attachements"
        :key="i"
        :src="djangobaseurl + '/media/' + item.document"
      ></v-carousel-item>
    </v-carousel>
    <div>
      Kategorie:
      <span>
        {{curObj.category.name}}
      </span><br>
    </div>
    <div
      v-if="curObj.state">
      Status:
      <span>
        {{curObj.state.name}}
      </span><br>
    </div>
    {{curObj.data.properties.description}}<br>

    <div
      v-if="enableLikes"
      class="d-flex align-center justify-end primary--text">
      <p class="rating">
        <v-icon color="primary" small>mdi-heart-outline</v-icon>
        <b
          style="vertical-align: middle;"
        > {{curObj.rating}}</b>
      </p>
      <v-btn
        fab x-small color="white"
        :disabled="ratingpause"
        class="primary--text"
        ref="rateupBtn"
        @click="rateUp(curObj.pk)"
        ><v-icon small>mdi-heart-plus</v-icon></v-btn>
      <v-icon
        id="addHeart"
        v-if="ratingpause"
        small
        color="primary"
        :style="cssVars"
        >mdi-heart</v-icon>
    </div>
    <div v-if="curObj.category.commentsEnabled">
      <h3>Kommentare</h3>
      <div id="commento"></div>
    </div>
  </div>
</template>

<style>

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
