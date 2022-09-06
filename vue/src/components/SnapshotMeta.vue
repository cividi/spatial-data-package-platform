<!-- eslint-disable -->
<i18n>
{
  "de": {
    "sources": "Quellenangaben",
    "expandlegend": "mehr",
    "collapslegend": "weniger",
    "predecessor": "Vorgängerversion",
    "comments": "Kommentare",
    "categories": "Kategorien",
    "states": "Stati"
  },
  "fr": {
    "sources": "Source",
    "expandlegend": "plus",
    "collapslegend": "moin",
    "predecessor": "version prédécesseuse",
    "comments": "Commentaires"
  },
  "en": {
    "sources": "Sources",
    "expandlegend": "more",
    "collapslegend": "less",
    "predecessor": "Previous version",
    "comments": "Comments"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <div class="smaller">
      <h3 class="mr-4">{{ title }}</h3>
      <p>
        <!-- <a class="legend--hash" :href="djangobaseurl + '/' + hash + '/'" target="_blank">
        {{ djangobaseurlDisplay }}/{{ hash }}/
        </a> -->
      </p>
      <p>
        {{ description }}
        <router-link v-if="predecessor" class="legend--hash"
          :to="'/'+ $i18n.locale +'/'+ predecessor.pk + '/'">
          {{ $t('predecessor') }}: {{ predecessor.pk }}
        </router-link>
      </p>

    </div>
    <v-list
      dense
      class="legend pt-0"
      :class="{showAll: showWholeLegend}">
      <v-list-item
        v-for="(item, i) in legend"
        :key="i"
        class="pa-0"
        :class="{isPrimary: item.primary}"
        >
        <v-list-item-icon class="my-0 mr-2">
          <img
            width="20" height="20"
            v-if="item.svg"
            :src="item.svg">
          <legend-icon v-else
            :shape="item.shape"
            :isPrimary="item.primary"
            :attr="item" />
        </v-list-item-icon>
        <v-list-item-content class="py-0">
          <v-list-item-title>
            {{ item.label }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-btn
      v-if="hasSecondaryLegend"
      v-show="!screenshotMode"
      text x-small
      @click="showWholeLegend=!showWholeLegend"
      class="moreLegendToggle"
      :class="{legendsvisible: showWholeLegend}"
      style="margin:-1.5em 0 0 -8px; text-transform:none;">
        <v-icon small color="primary">mdi-chevron-right</v-icon>
        <template v-if="showWholeLegend">
          {{ $t('collapslegend') }}
        </template>
        <template v-else>
          {{ $t('expandlegend') }}
        </template>
    </v-btn>
    <div class="smaller" v-if="legendCategories.length > 0">
      <h5 class="mr-4">{{ $t('categories') }}</h5>
    </div>
    <v-list
      dense class="legend pt-0"
      v-if="legendCategories.length > 0"
      >
      <v-list-item
        v-for="(item, i) in legendCategories"
        :key="i"
        class="pa-0 isPrimary"
        @click="$emit('toggleCat', item.pk);item.hidden=!item.hidden;"
        >
        <v-list-item-icon class="ma-0">
          <img
            width="20" height="20"
            v-if="item.svg"
            :src="item.svg">
          <legend-icon v-else
            :shape="item.shape"
            :isPrimary="item.primary"
            :attr="item" />
        </v-list-item-icon>
        <v-list-item-content class="py-0" :class="{'grey--text': item.hidden}">
          <v-list-item-title>
            {{ item.label }}
          </v-list-item-title>
        </v-list-item-content>
        <v-list-item-action>
          <v-btn icon>
            <v-icon v-if="item.hidden" color="grey lighten-1">mdi-eye-off</v-icon>
            <v-icon v-else color="grey lighten-1">mdi-eye</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
    <div class="smaller" v-if="legendStates.length > 0">
      <h5 class="mr-4">{{ $t('states') }}</h5>
    </div>
    <v-list
      dense class="legend pt-0"
      v-if="legendStates.length > 0"
      >
      <v-list-item
        v-for="(item, i) in legendStates"
        :key="i"
        class="pa-0 isPrimary"
        @click="$emit('toggleState', item.pk);item.hidden=!item.hidden;"
        >
        <v-list-item-content class="py-0" :class="{'grey--text': item.hidden}">
          <v-list-item-title>
            {{ item.label }}
          </v-list-item-title>
        </v-list-item-content>
        <v-list-item-action>
          <v-btn icon>
            <v-icon v-if="item.hidden" color="grey lighten-1">mdi-eye-off</v-icon>
            <v-icon v-else color="grey lighten-1">mdi-eye</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
    <div class="smaller"
      style="margin: 5px 0 -10px 2px;">
      <v-expand-transition>
        <ul
          class="sources pl-0"
          v-show="showSources">
          <li
            v-for="(item, i) in sources"
            :key="i"
            class="pb-1">
              <a :href="item.url" target="blank">
                <v-icon x-small color="primary">mdi-open-in-new</v-icon> {{ item.title }}
              </a>
           </li>
        </ul>
      </v-expand-transition>
    </div>
    <v-btn
      v-show="!screenshotMode"
      text x-small
      class="sourcesToggle"
      :class="{sourcesvisible: showSources}"
      @click="showSources=!showSources"
      style="text-transform:none; float:left; margin: 8px 0px 0px -8px;">
        <v-icon small color="primary">mdi-chevron-right</v-icon>
        {{ $t('sources') }}
    </v-btn>
    <a href="https://dfour.space" target="_blank">
      <img alt="dføur logo" height="18" id="legendLogo"
        style="float:right; opacity:0.55;"
        src="@/assets/images/dfour-logo.svg">
      </a>
  </div>
</template>

<style>
#legendLogo {
  float: right;
  margin-right: -5px;
  margin-top: 5px;
  opacity: 0.45;
}
.legend.v-list--dense .v-list-item {
  min-height: 0;
  height: 0;
  margin-top: 0;
  overflow: hidden;
  transition: min-height 0.3s, height 0.3s, margin-top 0.3s;
}
.legend.v-list--dense .v-list-item.isPrimary,
.legend.v-list--dense.showAll .v-list-item,
.legend .v-list-item__content {
  min-height: 24px;
  height: 24px;
  margin-top: 4px;
}

.legend .v-list-item__icon {
  min-width: auto;
}

.legend .v-list-item__content {
  padding-bottom: 4px !important;
}

.legend--line {
  margin: auto 0;
  width: 2em;
}

a.legend--hash,
.legend--hash:visited,
.legend--hash:hover,
.legend--hash:active {
  color: gray;
  font-weight: bold;
}
.moreLegendToggle .v-icon {
  transform: rotateZ(90deg);
  transition: transform 0.3s;
}
.moreLegendToggle.legendsvisible .v-icon {
  transform: rotateZ(-90deg);
}
.sourcesToggle .v-icon {
  transform: rotateZ(-90deg);
  transition: transform 0.3s;
}
.sourcesToggle.sourcesvisible .v-icon {
  transform: rotateZ(90deg);
}
.sources {
  list-style: none;
}
.sources li {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
.sources .v-icon {
  vertical-align: initial;
}
</style>

<script>
import Vue from 'vue';
import LegendIcon from './LegendIcon.vue';

Vue.component('legend-icon', LegendIcon);

export default {
  name: 'SnapshotMeta',
  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      showWholeLegend: false,
      showSources: false,
      screenshotMode: this.$route.query.hasOwnProperty('screenshot')
    };
  },

  props: {
    hash: String,
    title: String,
    description: String,
    predecessor: Object,
    legend: Array,
    legendCategories: Array,
    legendStates: Array,
    sources: Array
  },

  computed: {
    hasSecondaryLegend() {
      if (this.legend) {
        return this.legend.some(item => item.primary === false);
      }
      return [];
    },

    djangobaseurlDisplay() {
      return this.djangobaseurl.replace('https://', '').replace('http://', '');
    }
  }
};
</script>
