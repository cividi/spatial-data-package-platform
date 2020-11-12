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

          <v-autocomplete
            class="gemeindesuche"
            :placeholder="$t('municipality')"
            append-icon="mdi-magnify"
            v-model="select[0]"
            :items="municipalities"
            :search-input.sync="search"
            :menu-props="menuProps"
            item-text="node.fullname"
            item-value="node.bfsNumber"
            hide-no-data
            return-object
            ></v-autocomplete>
  <!--  hide-no-data -->


          <div v-if="!isNew">
            <p class="small mb-0">
              <strong>{{ $t('currentfile') }}:</strong> {{snapshot.datafile}}
            </p>
          </div>
          <v-progress-linear
            v-model="progress"
            color="light-blue"
            height="25"
            reactive
          >
            <strong>{{ progress }} %</strong>
          </v-progress-linear>
          <v-file-input
            accept=".json"
            :label="$t('file')"
            truncate-length="20"
            @change="selectFile"
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
import gql from 'graphql-tag';

export default {
  name: 'SnapshotEdit',
  data() {
    return {
      select: null,
      search: null,
      municipalities: [],
      inidone: false,
      currentFile: undefined,
      progress: 0
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
    },
    menuProps() {
      return !this.search ? { value: false } : {};
    }
  },
  mounted() {
    this.municipalities.push({ node: this.snapshot.municipality });
    this.select = [{ node: this.snapshot.municipality }];

    setTimeout(() => { this.inidone = true; }, 500);
  },
  methods: {
    async queryMunicipalities(val) { // event
      const result = await this.$apollo.query({
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
      return result;
    },

    async saveSnapshot() {
      this.snapshot.municipality = this.select[0].node;
      const data = {
        title: this.snapshot.title,
        topic: this.snapshot.topic,
        bfsNumber: this.select[0].node.bfsNumber,
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
        this.uploadDataJson();
        this.$emit('saved');
      }
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

    async uploadDataJson() {
      if (!this.currentFile) {
        return;
      }

      this.httpupload(this.currentFile, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          console.log('response', response);
          // return UploadService.getFiles();
        })
        .then((files) => {
          // this.fileInfos = files.data;
          console.log(files);
        })
        .catch(() => {
          this.progress = 0;
          this.currentFile = undefined;
          console.log('upload failed');
        });
    }
  },
  watch: {
    async search(val) {
      if (this.inidone) {
        const result = await this.queryMunicipalities(val);
        this.municipalities = result.data.municipalities.edges;
      }
    }
  }
};
</script>
