<!-- eslint-disable -->
<i18n>
{
  "de": {
    "editsnapshot": "Kartenlayer bearbeiten",
    "newsnapshot": "Kartenlayer hochladen",
    "newsnapshot.info": "Um einen Kartenlayer hochzuladen, muss dieser als Data Package im JSON Format gemäss der Spatial Data Package Spezifikation exportiert werden. Zum Beispiel mittels des QGIS Plugins.",
    "title": "Titel",
    "topic": "Thema",
    "municipality": "Gemeinde",
    "currentfile": "Aktuelle Datei",
    "file": "Datei (JSON)",
    "help": "Hilfe",
    "cancel": "abbrechen",
    "save": "speichern",
    "saveinfo": "Speichere Angaben",
    "savefile": "Sende Datei",
    "processing": "Daten werden verarbeitet",
    "mandatory": "Dies ist ein Pflichtfeld",
    "predecessor": "Vorgänerversion",
    "municipalityMandatory": "Bitte wählen Sie eine Gemeinde aus",
    "noMatches": "Keine Ergebnisse",
    "status": {
      "savingInfo": "Speichere Angaben",
      "sendingFile": "Sende Datei",
      "done": "Fertig"
    },
    "error": {
      "unspecified": "Etwas ist schiefgelaufen. Stellen Sie sicher, dass Sie eingeloggt sind und alle Daten korrekt eingegeben haben."
    }
  },
  "fr": {
    "editsnapshot": "Editer l'couche de données",
    "newsnapshot": "Télécharger l'couche de données",
    "newsnapshot.info": "Um einen Kartenlayer hochzuladen, muss dieser als Data Package im JSON Format gemäss der Spatial Data Package Spezifikation exportiert werden. Zum Beispiel mittels des QGIS Plugins.",
    "title": "Titre",
    "topic": "Sujet",
    "municipality": "Municipalité",
    "currentfile": "Fichier actuel",
    "file": "Fichier (JSON)",
    "help": "Aide",
    "cancel": "annuler",
    "save": "magasin",
    "mandatory": "Ce champ est obligatoire",
    "saveinfo": "Enregistrer les détails",
    "processing": "La couche de données est traitée",
    "savefile": "Télécharger le fichier",
    "predecessor": "version prédécesseuse",
    "municipalityMandatory": "Veuillez sélectionner une municipalité",
    "noMatches": "Aucun résultat",
    "status": {
      "savingInfo": "Enregistrer les détails",
      "sendingFile": "Télécharger le fichier",
      "done": "Prêt"
    },
    "error": {
      "unspecified": "Quelque chose a mal tourné. Assurez-vous que vous êtes connecté et que vous avez saisi toutes les données correctement."
    }
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <!-- <v-card id="snapshotedit" light width="400" class="pa-4"> -->
  <div>
    <h3 v-if="isNew">
      <v-icon
        class="pa-2"
        @click="$emit('back')">mdi-chevron-left
      </v-icon>
      {{ $t('newsnapshot') }}
    </h3>
    <h3 v-else>{{ $t('editsnapshot') }}</h3>
    <v-alert
      v-for="(error, errorIndex) in errors"
      :key="errorIndex"
      type="error"
      class="mt-2 mb-0"
    >
      {{ $t(`error.${error.code || 'unspecified'}`) }}
    </v-alert>
    <v-form
      v-if="!saving"
      class="pt-4"
      ref="snapshotform"
      v-model="valid"
      lazy-validation
      @submit="saveSnapshot"
    >
      <v-alert v-if="isNew"
        icon="mdi-lightbulb-outline"
        type="info" dense outlined dismissible
        class="body-2" color="primary">
        {{ $t('newsnapshot.info') }}
      </v-alert>
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
          (municipality) =>
            !!(municipality && municipality.bfsNumber) ||
            $t('municipalityMandatory')
        ]"
        :hide-no-data="!municipalities.length"
      >
        <v-list-item slot="no-data">
          <v-list-item-content>
            <v-list-item-title>{{ $t('noMatches') }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-combobox>
      <v-tooltip right>
        <template v-slot:activator="{ on, attrs }">
          <v-file-input
            accept=".json"
            :label="$t('file')"
            truncate-length="20"
            :rules="[
              file => !!datafile ||
                !!(file && file.name && file.type === 'application/json') ||
                $t('mandatory')
            ]"
            :required="isNew"
            @change="selectFile"
          >
            <v-icon
              slot="append-outer"
              tag="a"
              v-bind="attrs" v-on="on"
              href="https://github.com/cividi/spatial-data-package-spec"
              target="_blank"
              rel="noreferrer"
            >
              mdi-help-circle-outline
            </v-icon>
          </v-file-input>
        </template>
        <span>{{ $t('help') }}</span>
      </v-tooltip>
      <p class="small mb-0" v-if="datafile">
        <strong>{{ $t('currentfile') }}:</strong>
        {{ datafile }}
      </p>
      <div class="d-flex justify-space-between mt-4">
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
  </div>
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
      wshash: btoa(`WorkspaceNode:${this.$route.params.wshash}`),
      selectedMunicipality: undefined,
      errors: []
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

      this.errors = [];
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
        // apollo's errors are a bit strange
        if (error.graphQLErrors && error.networkError) {
          this.showErrors(...error.graphQLErrors, ...error.networkError.result.errors);
        } else {
          this.showErrors(error);
        }
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
    },
    showErrors(...errors) {
      this.errors = [...this.errors, ...errors];
    }
  }
};
</script>
