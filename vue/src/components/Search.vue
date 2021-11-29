<!-- eslint-disable -->
<i18n>
{
  "de": {
    "placeholder": "Suche",
    "label": "Gemeinde"
  },
  "fr": {
    "placeholder": "Recherche",
    "label": "Communauté"
  },
  "en": {
    "placeholder": "Search",
    "label": "Municipality"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-autocomplete
  ref="search"
  class="gemeindesuche"
  outlined
  :placeholder="placeholdertext"
  append-icon="mdi-magnify"
  background-color="white"
  v-model="select"
  :items="municipalities"
  :search-input.sync="search"
  :menu-props="menuProps"
  item-text="node.fullnameWithSnapshots"
  item-value="node.bfsNumber"
  hide-no-data
  return-object
  v-on:change="submitMunicipality()"
  :dense="dense"
  ></v-autocomplete>
</template>

<style>
.gemeindesuche.v-select {
  width: 100%;
  max-width: 420px;
}
.gemeindesuche.v-select.v-select--is-menu-active
  .v-input__icon--append
  .v-icon {
  transform: rotate(0);
}
</style>

<script>
import gql from 'graphql-tag';
import _ from 'lodash';

export default {
  name: 'Search',
  data() {
    return {
      select: null,
      search: null,
      municipalities: [],
      isLoading: false
    };
  },

  props: {
    term: String,
    autofocus: Boolean,
    dense: Boolean
  },

  mounted() {
    if (this.autofocus) {
      this.$refs.search.focus();
    }
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
                snapshots {
                  pk
                }
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

    submitMunicipality() {
      if (this.select.node.bfsNumber) {
        if (this.select.node.snapshots.length === 0) {
          this.$router.push({
            name: 'snapshotNew',
            params: {
              hash: null,
              bfsNumber: this.select.node.bfsNumber
            }
          });
        } else {
          this.$router.push({
            name: 'snapshot',
            params: {
              hash: this.select.node.snapshots[0].pk
            }
          });
        }
      }
    },
    debouncedQuery: _.debounce(async (val, self) => {
      const result = await self.queryMunicipalities(val);
      self.municipalities = result.data.municipalities.edges;
      self.municipalities.forEach((item) => {
        const nrScans = item.node.snapshots.length;
        if (nrScans === 0) {
          item.node.fullnameWithSnapshots = `${item.node.fullname}`;
        } else {
          item.node.fullnameWithSnapshots = `${item.node.fullname} •`;
        }
      });
    }, 500)
  },

  computed: {
    menuProps() {
      return !this.search ? { value: false } : {};
    },
    placeholdertext() {
      return this.term ? this.term : this.$t('placeholder');
    }
  },

  watch: {
    async search(val) {
      this.debouncedQuery(val, this);
    }
  }
};
</script>
