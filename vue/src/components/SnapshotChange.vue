<!-- eslint-disable -->
<template>
  <div>
    <div class="smaller">
      <h3 class="mr-4">{{ title }}</h3>
    </div>
    <!-- <v-list
      dense
      class="legend pt-0"
    >
      <v-input id="inputExample" label="My Input Example"></v-input>
    </v-list> -->
  </div>
</template>

<style>
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

export default {
  name: 'SnapshotChange',
  data() {
    return {
      showWholeLegend: false,
      showSources: false
    };
  },

  props: {
    hash: String,
    title: String,
    topic: String
  }
};
</script>
