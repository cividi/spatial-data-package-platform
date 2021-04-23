<!-- eslint-disable -->
<i18n>
{
  "de": {
    "newstore": "Neuen Snapshot bestellen",
    "cancel": "schliessen"
  },
  "fr": {
    "newstore": "Neuen Snapshot bestellen",
    "cancel": "schliessen"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <!-- <v-card id="snapshotorder" light class="pa-4"> -->
  <div id="snapshotstore">
    <h3>
      <v-icon
          class="pa-2"
          @click="$emit('back')">mdi-chevron-left
        </v-icon>
        {{ $t('newstore') }}
      </h3>

    <iframe src="https://stage.store.cividi.ch" id="snapshotstore"></iframe>

  </div>
</template>

<style>
#snapshotstore {
  width: 100%;
  height: 95%;
}
</style>

<script>
export default {
  name: 'SnapshotOrder'
};
</script>
