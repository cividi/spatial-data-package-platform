<!-- eslint-disable -->
<i18n>
{
  "de": {
    "addSnapshot": "Kartenlayer hinzufügen",
    "addSnapshot.order": "Kartenlayer bestellen",
    "addSnapshot.upload": "Kartenlayer hochladen"
  },
  "fr": {
    "addSnapshot": "Kartenlayer hinzufügen",
    "addSnapshot.order": "Données de la commande",
    "addSnapshot.upload": "Télécharger les données"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <h3>{{ $t("addSnapshot") }}</h3>

    <v-btn color="primary" icon fab tile text class="addSnapshotButton" @click="$emit('order')">
      <div class="choice-btn__content">
        <v-icon class="choice"> mdi-store </v-icon>
        <p>
          {{ $t("addSnapshot.order") }}
        </p>
      </div>
    </v-btn>

    <v-btn color="primary" icon fab tile class="addSnapshotButton" @click="$emit('new')">
      <div class="choice-btn__content">
        <v-icon class="choice"> mdi-progress-upload </v-icon>
        <p>
          {{ $t("addSnapshot.upload") }}
        </p>
      </div>
    </v-btn>
  </div>
</template>

<style></style>

<script>
export default {
  name: 'SnapshotAdd'
};
</script>
