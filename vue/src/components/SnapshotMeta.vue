<template>
  <div>
    <div class="smaller">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
    <v-list
    dense
    class="legend">
      <v-list-item
        v-for="(legend, i) in legends"
        :key="i"
        class="pa-0 mb-1"
        >
        <v-list-item-icon class="my-0 mr-4">
          <v-icon :color="legend.color">mdi-circle</v-icon>
        </v-list-item-icon>
        <v-list-item-content class="py-0">
          <v-list-item-title>
            {{legend.title}}
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
</style>

<script>
export default {
  name: 'SnapshotMeta',
  data() {
    return {
      legends: [
        { title: 'Legende 1', color: '#9CF' },
        { title: '', color: '#69C' },
        { title: 'Letzte Legende', color: '#369' }
      ]
    };
  },
  props: {
    title: String,
    description: String
  }
};
</script>
