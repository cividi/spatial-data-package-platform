<template>
  <div>
    <div class="smaller">
      <h3>{{ title }}</h3>
      <p >
        <a class="legend--hash" :href="'https://gemeindescan.ch/' + hash" target="_blank">
        gemeindescan.ch/{{ hash }}
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
            :color="item.color" :style="{ fontSize: item.size + 'em'}">mdi-circle</v-icon>
          <v-icon v-else-if="item.shape === 'square'"
            :color="item.color" :style="{ fontSize: item.size + 'em'}">mdi-square</v-icon>
          <span v-else-if="item.shape === 'line'" class="legend--line"
            :style="{ backgroundColor: item.color, height: 0.5 * item.size + 'em'}">&nbsp;
          </span>
        </v-list-item-icon>
        <v-list-item-content class="py-0">
          <v-list-item-title>
            {{ item.label }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

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
.legend--hash,
.legend--hash:visited {
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
