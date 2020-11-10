<!-- eslint-disable -->
<i18n>
{
  "de": {
    "editsnapshot": "Snapshot bearbeiten",
    "newsnapshot": "Neuen Snapshot anlegen",
    "title": "Titel",
    "topic": "Thema",
    "municipality": "Gemeinde",
    "currentfile": "Aktuelle Datei",
    "file": "Datei (JSON)",
    "cancel": "abbrechen",
    "save": "speichern",
    "predecessor": "Vorgänerversion"
  },
  "fr": {
    "editsnapshot": "Snapshot bearbeiten",
    "newsnapshot": "Neuen Snapshot anlegen",
    "title": "Titre",
    "topic": "Sujet",
    "municipality": "Municipalité",
    "currentfile": "Aktuelle Datei",
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
    <v-form class="pt-4">
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

          <div v-if="!isNew">
            <p class="small">  {{ $t('currentfile') }}:   {{snapshot.datafile}}</p>
          </div>
          <v-file-input
            accept=".json"
            :label="$t('file')"
            truncate-length="20"
          ></v-file-input>
          <div class="d-flex justify-space-between mt-4">
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
          </div>
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

    };
  },

  props: {
    snapshot: Object
  },

  computed: {
    isNew() {
      if (this.snapshot.pk) {
        return false;
      }
      return true;
    }
  },
  methods: {
    saveSnapshot() {
      console.log('saveSnapshot');
    }
  }
};
</script>
