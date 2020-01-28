<template>
  <!-- eslint-disable max-len -->
  <v-container my-12>
      <div class="gmdscn">
          <v-img alt="Gemeindescan Schweiz" class="" width="100%" contain src="@/assets/images/gmdscn-ch-map.svg"></v-img>
          <v-autocomplete
            class="gemeindesuche"
            outlined
            placeholder="Suche"
            append-icon="mdi-magnify"
            background-color="white"
            v-model="select"
            :items="municipalities"
            :search-input.sync="search"
            :menu-props="menuProps"
            item-text="node.name"
            item-value="node.name"
            hide-no-data
            return-object
            v-on:keyup.enter="submitMunicipality()"
          ></v-autocomplete>
      </div>
      <v-row justify="center">
        <v-col class="introtxt text-center py-12">
          <h1>Entdecke das Lebensraum-Potential deiner Gemeinde.</h1>
          <p>Der Gemeindescan ermöglicht Gemeindeverwaltungen auf einfache und
          kosteneffiziente Weise ein Bild von Nutzungen und Nutzern in Ihrer Gemeinde
          zu erhalten. Flächennutzung, Verkehr oder Struktur werden an einer Stelle
          evidenzbasiert zusammengeführt.</p>
          <p>Die Darstellungen dienen der Vorbereitung von Planungsaufgaben,
          der Kommunikation mit Politik, Bürgern oder Entwicklern und Investoren.</p>
        </v-col>
      </v-row>
  </v-container>
</template>
<style>
.gmdscn {
  position: relative;
  max-width: 720px;
  margin: 0 auto;
}
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
.introtxt {
  max-width: 660px;
}
</style>
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
    },

    submitMunicipality() {
      this.$router.push({ name: 'signup', params: { gemeinde: this.search } });
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
