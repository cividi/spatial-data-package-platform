<template>
  <v-container>
      <v-layout
        text-center
        wrap
      >
        <v-flex>
          <img alt="gemeindescan logo" height="400" src="@/assets/images/gmdscn-ch-map.svg">
          <v-autocomplete
          class="d-inline-flex pa-2"
          v-model="select"
          :items="municipalities"
          :search-input.sync="search"
          :menu-props="menuProps"
          item-text="node.name"
          item-value="node.name"
          placeholder="Suche"
          append-icon="mdi-magnify"
          hide-no-data
          return-object
          ></v-autocomplete>
          <h1>Entdecke das Lebensraum-Potential deiner Gemeinde.</h1>
          <p>At delicatissimi pro affert iuvaret ex qui vulputate id cu altera
            eu philosophia lorem rebum nibh adhuc. Et persequeris tantas
            theophrastus saperet ne ex instructior doctus altera.</p>
        </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import gql from 'graphql-tag';

export default {
  data() {
    return {
      select: null,
      search: null,
      municipalities: [],
      isLoading: false
    };
  },

  methods: {
    async queryMunicipalities(val) { // event
      const result = await this.$apollo.query({
        query: gql`query getmunicipalities($q: String!){
          municipalities(name_Icontains: $q) {
            edges {
              node {
                name
              }
            }
          }
        }`,
        variables: {
          q: val
        }
      });
      return result;
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
