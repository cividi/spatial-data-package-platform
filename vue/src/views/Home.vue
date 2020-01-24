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
      <v-row justify="center">
        <v-col sm="12" md="8" lg="6">
        <div class="typeform-widget" data-url="https://cividi.typeform.com/to/vjVoPr"
          data-transparency="50" style="width: 100%; height: 100%;"></div>
          <div style="font-family: Sans-Serif;font-size: 12px;color: #999;opacity: 0.5; padding-top: 5px;">
          powered by
          <!-- eslint-disable-next-line max-len -->
          <a href="https://admin.typeform.com/signup?utm_campaign=vjVoPr&amp;.utm_source=typeform.com-01DH3Y9W4K4NQZANA3FZ4EVVMZ-essentials&amp;.utm_medium=typeform&amp;.utm_content=typeform-embedded-poweredbytypeform&amp;.utm_term=EN"
            style="color: #999" target="_blank">Typeform</a>
          </div>
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
