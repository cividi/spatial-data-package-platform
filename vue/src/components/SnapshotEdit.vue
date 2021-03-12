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
    "saveinfo": "Speichere Angaben",
    "savefile": "Sende Datei",
    "processing": "Processiere Snapshot",
    "mandatory": "Dies ist ein Pflichtfeld",
    "predecessor": "Vorgänerversion",
    "municipalityMandatory": "Bitte wählen Sie eine Gemeinde aus",
    "noMatches": "Keine Ergebnisse",
    "status": {
      "savingInfo": "Speichere Angaben",
      "sendingFile": "Sende Datei",
      "done": "Fertig"
    }
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
    "mandatory": "Dies ist ein Pflichtfeld",
    "saveinfo": "Speichere Angaben",
    "processing": "Processiere Snapshot",
    "savefile": "Sende Datei",
    "predecessor": "version prédécesseuse",
    "municipalityMandatory": "Veuillez sélectionner une municipalité",
    "noMatches": "Aucun résultat"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-card id="snapshotedit" light width="400" class="pa-4">
    <h3 v-if="isNew">{{ $t('newsnapshot') }}</h3>
    <h3 v-else>{{ $t('editsnapshot') }}</h3>
    <v-form
      v-if="!saving"
      class="pt-4"
      ref="snapshotform"
      v-model="valid"
      lazy-validation
      @submit="saveSnapshot"
    >
      <v-text-field
        v-model="selected.title"
        :label="$t('title')"
        :rules="[v => !!v || $t('mandatory')]"
        required
      />
      <v-text-field
        v-model="selected.topic"
        :label="$t('topic')"
        :rules="[v => !!v || $t('mandatory')]"
        required
      />

      <v-combobox
        class="gemeindesuche"
        :placeholder="$t('municipality')"
        append-icon="mdi-magnify"
        v-model="selected.municipality"
        :items="municipalities"
        item-text="fullname"
        item-value="bfsNumber"
        return-object
        required
        @update:search-input="queryAndSetMunicipalities"
        :rules="[
          (municipality) => municipality && municipality.bfsNumber || $t('municipalityMandatory')
        ]"
        :hide-no-data="!municipalities.length"
      >
        <v-list-item slot="no-data">
          <v-list-item-content>
            <v-list-item-title>{{ $t('noMatches') }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-combobox>

      <v-file-input
        accept=".json"
        :label="$t('file')"
        truncate-length="20"
        :rules="[
          file => !!snapshot.datafile ||
            !!(file && file.name && file.type === 'application/json') ||
            $t('mandatory')
        ]"
        :required="isNew"
        @change="selectFile"
      >
        <v-icon
          slot="append-outer"
          tag="a"
          href="https://github.com/cividi/spatial-data-package-spec"
          target="_blank"
          rel="noreferrer"
        >
          mdi-help-circle-outline
        </v-icon>
      </v-file-input>
      <p class="small mb-0" v-if="datafile">
        <strong>{{ $t('currentfile') }}:</strong>
        {{ datafile }}
      </p>
      <div class="d-flex justify-space-between mt-4">
        <v-btn
        @click="$emit('cancel')">
          {{ $t('cancel') }}
        </v-btn>
        <v-btn
          type="submit"
          color="primary"
        >
          {{ $t('save') }}
        </v-btn>
      </div>
    </v-form>
    <div v-else>
      <p>{{status}}</p>
      <v-progress-linear
        v-model="progress"
        color="primary"
        reactive
        v-if="progress"
      />
    </div>
  </v-card>
</template>

<style>
</style>

<script>
import gql from 'graphql-tag';

export default {
  name: 'SnapshotEdit',
  data() {
    return {
      valid: true,
      municipalities: [],
      saving: false,
      status: '',
      progress: 0,
      selected: {
        title: this.title,
        topic: this.topic,
        municipality: this.municipality,
        file: undefined
      },
      wshash: btoa(`WorkspaceNode:${this.$route.params.wshash}`)
    };
  },

  props: {
    isNew: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      default: undefined
    },
    topic: {
      type: String,
      default: undefined
    },
    municipality: {
      type: Object,
      default: () => undefined
    },
    datafile: {
      type: String,
      default: undefined
    },
    id: {
      type: String,
      default: undefined
    },
    pk: {
      type: String,
      default: undefined
    }
  },
  methods: {
    async queryMunicipalities(val) { // event
      const { data } = await this.$apollo.query({
        query: gql`query getmunicipalities($q: String!){
          municipalities(name_Icontains: $q) {
            edges {
              node {
                bfsNumber
                fullname
              }
            }
          }
        }`,
        variables: {
          q: val
        }
      });
      return data.municipalities.edges.map(({ node }) => node);
    },
    async saveSnapshot(event) {
      event.preventDefault();
      if (!this.$refs.snapshotform.validate()) {
        return;
      }

      this.saving = true;
      this.status = this.$t('status.savingInfo');

      try {
        const { data } = await this.$apollo.mutate({
          mutation: gql`mutation updatesnapshot($data: SnapshotMutationInput!){
            snapshotmutation(input: $data) {
              snapshot {
                id
                pk
                title
                topic
                municipality {
                  bfsNumber
                }
                datafile
              }
            }
          }`,
          variables: {
            data: {
              title: this.selected.title,
              topic: this.selected.topic,
              bfsNumber: this.selected.municipality.bfsNumber,
              wshash: this.wshash,
              clientMutationId: this.id
            }
          }
        });

        if (this.selected.file && this.selected.file.name) {
          // a file is selected an actual file, upload it
          this.status = this.$t('status.sendingFile');
          await this.httpupload(this.selected.file, data.snapshotmutation.snapshot.pk);
        }

        this.$emit('saved', { isNew: this.isNew, snapshot: data.snapshotmutation.snapshot });
        this.status = this.$t('status.done');
      } catch (error) {
        // TODO: show error
        this.progress = 0;
        this.selected.file = undefined;
      } finally {
        this.saving = false;
        this.status = undefined;
      }
    },
    selectFile(file) {
      this.progress = 0;
      this.selected.file = file;
    },
    async httpupload(file, snapshotPk) {
      const csrftoken = this.$cookies.get('csrftoken', '');
      const formData = new FormData();

      formData.append('data_file', file);

      await this.$restApi.patch(`snapshots/${snapshotPk}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': csrftoken
        },
        onUploadProgress: (event) => {
          this.progress = Math.floor(100 * event.loaded / event.total);
        }
      });
    },
    async queryAndSetMunicipalities(searchInput) {
      if (searchInput) {
        const municipalities = await this.queryMunicipalities(searchInput);
        this.municipalities = municipalities;
      }
    }
  }
};
</script>
