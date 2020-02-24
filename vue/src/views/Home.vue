<!-- eslint-disable -->
<i18n>
{
  "de": {
    "placeholder.autocomplete": "Suche",
    "h1.1": "Entdecke das Lebensraum-Potential deiner Gemeinde.",
    "p.1":
      "Der Gemeindescan ermöglicht Gemeindeverwaltungen auf einfache und kosteneffiziente Weise ein Bild von Nutzungen und Nutzern in Ihrer Gemeinde zu erhalten. Flächennutzung, Verkehr oder Struktur werden an einer Stelle evidenzbasiert zusammengeführt.",
    "p.2":
      "Die Darstellungen dienen der Vorbereitung von Planungsaufgaben, der Kommunikation mit Politik, Bürgern oder Entwicklern und Investoren.",
    "img.1.alt":
      "Gemeindescan Schweiz"
  },
  "fr": {
    "placeholder.autocomplete": "Recherche",
    "h1.1": "Découvrez le potentiel en terme d'habitat de votre communauté.",
    "p.1":
      "Le Gemeindescan permet aux autorités locales de se faire une idée des utilisations et des utilisateurs de votre communauté de manière simple et économique. L'utilisation des sols, du trafic ou des structures est rassemblée sur un seul support basé sur des faits.",
    "p.2":
      "Les représentations servent à la préparation des tâches de planification, à la communication avec les politiciens, les citoyens ou les promoteurs et les investisseurs.",
    "img.1.alt":
      "Le Gemeindescan Suisse"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <!-- eslint-disable max-len -->
  <v-container my-12>
      <div class="gmdscn">
          <img :alt="$t('img.1.alt')" class="" width="100%"
            src="@/assets/images/gmdscn-ch-map.svg"/>
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
      </div>
      <v-row justify="center">
        <v-col class="introtxt text-center py-12">
          <h1>{{ $t('h1.1') }}</h1>
          <p>{{ $t('p.1') }}</p>
          <p>{{ $t('p.2') }}</p>
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
  },

  mounted() {
    this.$refs.search.focus();
  }
};
</script>
