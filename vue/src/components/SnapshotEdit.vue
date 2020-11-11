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
import gql from 'graphql-tag';

export default {
  name: 'SnapshotEdit',
  data() {
    return {
      select: null,
      search: null,
      municipalities: [],
      inidone: false
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

    saveSnapshot() {
      console.log('saveSnapshot');
    }
  },
  watch: {
    async search(val) {
      if (this.inidone) {
        console.log(`search${val}`);
        const result = await this.queryMunicipalities(val);
        this.municipalities = result.data.municipalities.edges;
      }
    }
  }
};
</script>