<!-- eslint-disable -->
<i18n>
{
  "de": {
    "addSnapshot.order": "Kartenlayer bestellen",
    "placeholder": "Suche",
    "label": "Gemeinde"
  },
  "fr": {
    "addSnapshot.order": "Données de la commande",
    "placeholder": "Recherche",
    "label": "Communauté"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <!-- <v-card id="snapshotorder" light class="pa-4"> -->
  <div id="snapshotstore">
    <h3>
      <v-icon
          class="pa-2"
          @click="$emit('back')">mdi-chevron-left
        </v-icon>
        {{ $t('addSnapshot.order') }}
      </h3>

      <p>&nbsp;</p>

      <v-stepper
        v-model="cart"
        vertical
      >

        <v-stepper-step
          :complete="cart > 1"
          editable
          step="1"
        >
          {{ municipalityText }}
        </v-stepper-step>

        <v-stepper-content step="1">
          <template>
            <v-autocomplete
              ref="perimeterSearch"
              class="gemeindesuche"
              outlined
              :placeholder="placeholdertext"
              append-icon="mdi-magnify"
              background-color="white"
              v-model="select"
              :items="municipalities"
              :search-input.sync="perimeterSearch"
              :menu-props="menuProps"
              item-text="node.fullname"
              item-value="node.bfsNumber"
              hide-no-data
              return-object
              v-on:change="submitMunicipality()"
              dense
              ></v-autocomplete>
            </template>

        </v-stepper-content>

        <v-stepper-step
          :complete="cart > 2"
          editable
          step="2"
        >
          Daten
          <small></small>
        </v-stepper-step>

        <v-stepper-content step="2">
          <snapshot-order-item />
          <v-btn
            color="primary"
            @click="cart = 3"
          >
            Auswählen
          </v-btn>
        </v-stepper-content>

        <v-stepper-step
          :complete="cart > 3"
          step="3"
        >
          Rechnungsdaten
          <small></small>
        </v-stepper-step>

        <v-stepper-content step="3">
          <v-container fluid>
            <v-row>
              <v-col>
                <v-text-field
                    v-model="form.first"
                    color="primary"
                    label="Vorname"
                    required
                  ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                    v-model="form.last"
                    color="primary"
                    label="Nachname"
                    required
                  ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="form.email"
                  color="primary"
                  label="E-Mail"
                  required
                ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="form.company"
                  color="primary"
                  label="Organization"
                  required
                ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="form.phone"
                  color="primary"
                  label="Telefon"
                  required
                ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
                  v-model="form.address"
                  color="primary"
                  label="Rechnungsadresse"
                  required
                ></v-text-field>
            </v-row>
            <v-row>
              <v-textarea
                  v-model="form.comment"
                  color="primary"
                  label="Kommentar"
                  required
                ></v-textarea>
            </v-row>
          </v-container>
          <v-btn
            color="primary"
            @click="cart = 4"
          >
            Bestellen
          </v-btn>
        </v-stepper-content>

      </v-stepper>

  </div>
</template>

<style>
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import _ from 'lodash';
import SnapshotOrderItem from './SnapshotOrderItem.vue';

Vue.component('snapshot-order-item', SnapshotOrderItem);

export default {
  name: 'SnapshotOrder',
  data() {
    const defaultForm = Object.freeze({
      gender: 'Frau',
      first: '',
      last: '',
      email: '',
      company: '',
      phone: '',
      address: '',
      comment: ''
    });

    return {
      cart: 1,
      form: Object.assign({}, defaultForm),
      snapshotStoreUrl: process.env.VUE_APP_SNAPSHOTSTOREURL,
      snapshotsStore: [],
      select: null,
      perimeterSearch: null,
      municipalities: [],
      municipality: null,
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

    submitMunicipality() {
      if (this.select.node.bfsNumber) {
        this.municipality = this.select.node;
        this.cart = 2;
        console.log('hurray', this.select.node);
      }
    },
    debouncedQuery: _.debounce(async (val, self) => {
      const result = await self.queryMunicipalities(val);
      self.municipalities = result.data.municipalities.edges;
      // self.municipalities.forEach((item) => {
      //   const nrScans = item.node.snapshots.length;
      //   if (nrScans === 0) {
      //     item.node.fullnameWithSnapshots = `${item.node.fullname}`;
      //   } else {
      //     item.node.fullnameWithSnapshots = `${item.node.fullname} •`;
      //   }
      // });
    }, 500)
  },

  async mounted() {
    fetch(`${this.snapshotStoreUrl}/pipelines.${this.$i18n.locale}.json`)
      .then(response => response.json())
      .then((data) => {
        data.forEach((el, i) => {
          data[i].thumbnail = `${this.snapshotStoreUrl}/${el.thumbnail}`;
        });

        this.snapshotsStore = data;
      });
  },

  computed: {
    menuProps() {
      return !this.perimeterSearch ? { value: false } : {};
    },
    placeholdertext() {
      return this.$t('placeholder');
    },
    municipalityText() {
      return this.municipality ? this.municipality.fullname : 'Perimeter';
    }
  },

  watch: {
    async perimeterSearch(val) {
      this.debouncedQuery(val, this);
    }
  }
};
</script>
