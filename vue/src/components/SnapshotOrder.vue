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
  <v-card id="snapshotorder" light class="pa-4">
    <h3>{{ $t('newstore') }}</h3>

    <iframe src="https://stage.store.cividi.ch" id="snapshotstore"></iframe>

    <div class="d-flex justify-space-between mt-4">
      <v-btn
      @click="$emit('cancel')">
        {{ $t('cancel') }}
      </v-btn>
    </div>
  </v-card>
</template>

<style>
#snapshotorder {
  width: 95vw;
  height: 80vh;
  max-width: 1100px;
}
#snapshotstore {
  width: 100%;
  height: 85%;
  margin-top: 30px;
}
</style>

<script>
export default {
  name: 'SnapshotOrder'
};
</script>
