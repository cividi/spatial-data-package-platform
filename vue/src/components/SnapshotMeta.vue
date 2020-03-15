<template>
  <div>
    <div class="smaller">
      <h3>{{ title }}</h3>
      <p >
        <a class="legend--hash" :href="'https://gemeindescan.ch/' + hash + '/'" target="_blank">
        gemeindescan.ch/{{ hash }}/
        </a>
      </p>
      <p>{{ description }}</p>
    </div>
    <v-list
      dense
      class="legend">
      <v-list-item
        v-for="(item, i) in legend"
        :key="i"
        class="pa-0 mb-1"
        >
        <v-list-item-icon class="my-0 mr-2">
          <legend-icon :shape="item.shape" :isPrimary="item.primary" :attr="item" />
        </v-list-item-icon>
        <v-list-item-content class="py-0">
          <v-list-item-title>
            {{ item.label }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <img alt="gemeindescan logo" height="35" src="@/assets/images/gemeindescan-logo.svg">
  </div>
</template>

<style>
.legend .v-list-item--dense,
.legend.v-list--dense .v-list-item,
.legend .v-list-item__content {
  min-height: 24px;
}

.v-list-item__icon {
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
</style>

<script>
import Vue from 'vue';
import LegendIcon from './LegendIcon.vue';

Vue.component('legend-icon', LegendIcon);

export default {
  name: 'SnapshotMeta',
  data() {
    return {};
  },
  props: {
    hash: String,
    title: String,
    description: String,
    legend: Array
  }
};
</script>
