<!-- eslint-disable -->
<i18n>
{
  "de": {
    "editsnapshot": "Snapshot bearbeiten",
    "newsnapshot": "Neuer Snapshot anlegen",
    "title": "Titel",
    "topic": "Thema",
    "municipality": "Gemeinde",
    "file": "Datei (JSON)",
    "cancel": "abbrechen",
    "save": "speichern",
    "predecessor": "Vorgänerversion"
  },
  "fr": {
    "editsnapshot": "Snapshot bearbeiten",
    "newsnapshot": "Neuer Snapshot anlegen",
    "title": "Titre",
    "topic": "Sujet",
    "municipality": "Municipalité",
    "file": "Fichier (JSON)",
    "cancel": "abbrechen",
    "save": "speichern",
    "predecessor": "version prédécesseuse"
  }
}
</i18n>
<!-- eslint-enable -->

<template>

  <v-card id="snapshotedit" light width="400" class="pa-4">
    <h3 v-if="isNew">{{ $t('newsnapshot') }}</h3>
    <h3 v-else>{{ $t('editsnapshot') }}</h3>
    <v-form>
      <!--
                   :rules="rules"
            counter="25"
            hint="This field uses counter prop"
          -->
        <v-text-field
            v-model="snapshot.title"
            :label="$t('title')"
          ></v-text-field>
                  <v-text-field
            v-model="snapshot.topic"
            :label="$t('topic')"
          ></v-text-field>

          <v-file-input
            v-model="snapshot.datafile"
            accept=".json"
            :label="$t('file')"
            truncate-length="20"
          ></v-file-input>
          <v-btn
          @click="$emit('cancel')">
            {{ $t('cancel') }}
          </v-btn>
          <v-btn
          color="primary"
          @click="saveSnapshot"
          >
            {{ $t('save') }}
          </v-btn>
    </v-form>
  </v-card>
</template>

<style>
</style>

<script>
export default {
  name: 'SnapshotEdit',
  data() {
    return {
      isNew: false
    };
  },

  props: {
    snapshot: Object
  },

  computed: {

  },
  methods: {
    saveSnapshot() {
      console.log('saveSnapshot');
    }
  }
};
</script>
