<template>
  <!-- eslint-disable max-len -->
  <v-container>
      <v-layout
        text-center
        wrap
      >
        <v-flex>
          <img alt="gemeindescan logo" height="400" src="@/assets/images/gmdscn-ch-map.svg">
          <v-autocomplete
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
          <p>Der Gemeindescan ermöglicht Gemeindeverwaltungen auf einfache und
          kosteneffiziente Weise ein Bild von Nutzungen und Nutzern in Ihrer Gemeinde
          zu erhalten. Flächennutzung, Verkehr oder Struktur werden an einer Stelle
          evidenzbasiert zusammengeführt.</p>
          <p>Die Darstellungen dienen der Vorbereitung von Planungsaufgaben,
          der Kommunikation mit Politik, Bürgern oder Entwicklern und Investoren.</p>
        </v-flex>
        <v-flex>
        <div class="typeform-widget" data-url="https://cividi.typeform.com/to/vjVoPr"
          data-transparency="50" style="width: 100%; height: 100%;"></div>
          <div style="font-family: Sans-Serif;font-size: 12px;color: #999;opacity: 0.5; padding-top: 5px;">
          powered by
          <!-- eslint-disable-next-line max-len -->
          <a href="https://admin.typeform.com/signup?utm_campaign=vjVoPr&amp;.utm_source=typeform.com-01DH3Y9W4K4NQZANA3FZ4EVVMZ-essentials&amp;.utm_medium=typeform&amp;.utm_content=typeform-embedded-poweredbytypeform&amp;.utm_term=EN"
            style="color: #999" target="_blank">Typeform</a>
          </div>
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

  mounted() {
    // eslint-disable-next-line
    (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm", b="https://embed.typeform.com/"; if(!gi.call(d,id)) { js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })()
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
