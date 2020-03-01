<!-- eslint-disable -->
<i18n>
{
  "de": {
    "placeholder.autocomplete": "Suche"
  },
  "fr": {
    "placeholder.autocomplete": "Recherche"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-autocomplete
  ref="search"
  class="gemeindesuche"
  outlined
  :placeholder="$t('placeholder.autocomplete')"
  append-icon="mdi-magnify"
  background-color="white"
  v-model="select"
  :items="municipalities"
  :search-input.sync="search"
  :menu-props="menuProps"
  item-text="node.fullname"
  item-value="node.bfsNumber"
  hide-no-data
  return-object
  v-on:change="submitMunicipality()"
></v-autocomplete>
</template>

<style>
.gemeindesuche.v-select {
  position: absolute;
  top: calc(50% - 30px);
  left: 50%;
  width: 100%;
  max-width: 420px;
  transform: translateX(-50%);
}
.gemeindesuche.v-select.v-select--is-menu-active
  .v-input__icon--append
  .v-icon {
  transform: rotate(0);
}
</style>

<script>
import gql from 'graphql-tag';

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

  mounted() {
    this.$refs.search.focus();
  },

  methods: {
    async queryMunicipalities(val) { // event
      const result = await this.$apollo.query({
        query: gql`query getmunicipalities($q: String!){
          municipalities(name_Icontains: $q) {
            edges {
              node {
                bfsNumber, fullname
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
        this.$router.push({
          name: 'signup',
          params: {
            bfsnumber: this.select.node.bfsNumber,
            bfsname: this.select.node.fullname
          }
        });
      }
    }
  },

  computed: {
    menuProps() {
      return !this.search ? { value: false } : {};
    }
  },

  watch: {
    async search(val) {
      const result = await this.queryMunicipalities(val);
      this.municipalities = result.data.municipalities.edges;
    }
  }
};
</script>
