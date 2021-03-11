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
    "noMatches": "Keine Ergebnisse"
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
    >
      <v-text-field
        v-model="snapshot.title"
        :label="$t('title')"
        :rules="[v => !!v || $t('mandatory')]"
        required
      />
      <v-text-field
        v-model="snapshot.topic"
        :label="$t('topic')"
        :rules="[v => !!v || $t('mandatory')]"
        required
      />

      <v-combobox
        class="gemeindesuche"
        :placeholder="$t('municipality')"
        append-icon="mdi-magnify"
        v-model="selectedMunicipality"
        :items="municipalities"
        item-text="fullname"
        item-value="bfsNumber"
        return-object
        required
        @update:search-input="queryAndSetMunicipalities"
        :rules="[(value) => value && value.bfsNumber ? true : $t('municipalityMandatory')]"
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
        @change="selectFile"
        :rules="[v => !!v || $t('mandatory')]"
        :required="isNew"
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
      <div v-if="!isNew">
        <p class="small mb-0">
          <strong>{{ $t('currentfile') }}:</strong> {{snapshot.datafile}}
        </p>
      </div>
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
      search: null,
      municipalities: [],
      currentFile: undefined,
      saving: false,
      status: '',
      progress: 0,
      selectedMunicipality: this.snapshot.municipality
    };
  },

  props: {
    snapshot: {
      type: Object,
      default: () => ({})
    },
    isNew: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    menuProps() {
      return !this.search ? { value: false } : {};
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
    async saveSnapshot() {
      if (!this.$refs.snapshotform.validate()) {
        // console.log('not valid');
        return false;
      }
      this.saving = true;
      this.status = this.$t('saveinfo');
      const data = {
        title: this.snapshot.title,
        topic: this.snapshot.topic,
        bfsNumber: this.selectedMunicipality.bfsNumber,
        wshash: btoa(`WorkspaceNode:${this.$route.params.wshash}`)
      };
      if (this.snapshot.id) {
        data.clientMutationId = this.snapshot.id;
      }
      const result = await this.$apollo.mutate({
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
          data
        }
      });
      if (result) {
        this.snapshot.id = result.data.snapshotmutation.snapshot.id;
        this.snapshot.pk = result.data.snapshotmutation.snapshot.pk;
        this.status = this.$t('savefile');
        this.uploadDataJson();
        return true;
      }
      // console.log('error saving snapshot info');
      return false;
    },

    selectFile(file) {
      this.progress = 0;
      this.currentFile = file;
    },

    httpupload(file, onUploadProgress) {
      const csrftoken = this.$cookies.get('csrftoken', '');
      const formData = new FormData();

      formData.append('data_file', file);

      return this.$restApi.patch(`snapshots/${this.snapshot.pk}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'X-CSRFToken': csrftoken
        },
        onUploadProgress
      });
    },

    uploadDataJson() {
      if (!this.currentFile) {
        this.saveDone();
        return;
      }
      this.httpupload(this.currentFile, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then(() => {
          // console.log('response', response);
          this.saveDone();
        })
        .catch(() => {
          this.progress = 0;
          this.currentFile = undefined;
          this.saving = false;
          // console.log('upload failed');
        });
    },
    saveDone() {
      this.saving = false;
      this.$emit('saved', { isNew: this.isNew, snapshot: this.snapshot });
      if (this.$route.params.hash === this.snapshot.pk) {
        this.$router.go();
      } else if (this.isNew) {
        // todo is never new at this point because of watch; change compute on mount
        this.status = this.$t('processing');
        window.setTimeout(this.goToEditedSnapshot, 2000);
      } else {
        this.goToEditedSnapshot();
      }
    },
    goToEditedSnapshot() {
      const wHash = this.$route.params.wshash;
      const curpk = this.snapshot.pk;
      const ln = this.$route.params.lang;
      this.$router.push(`/${ln}/${wHash}/${curpk}/`);
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
