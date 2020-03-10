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
          <v-icon v-if="item.shape === 'circle'"
            :color="item.color"
            :style="{ fontSize: 1.6 * item.size + 'em', opacity: item.opacity}">mdi-circle</v-icon>
          <v-icon v-else-if="item.shape === 'square'"
            :color="item.color"
            :style="{ fontSize: 1.6 * item.size + 'em', opacity: item.opacity}">mdi-square</v-icon>
          <span v-else-if="item.shape === 'line'" class="legend--line"
            :style="{
              backgroundColor: item.color,
              height: 0.5 * item.size + 'em',
              opacity: item.opacity}">&nbsp;
          </span>
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
.legend.v-list--dense .v-list-item {
  min-height: 24px;
}
.v-list-item__icon {
  min-width: auto;
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
