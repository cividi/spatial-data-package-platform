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
          @click="cancelOrder">mdi-chevron-left
        </v-icon>
        {{ $t('addSnapshot.order') }}
      </h3>

      <p>&nbsp;</p>

      <v-stepper
        v-model="cart"
        vertical
        v-if="!ordered"
      >

        <v-stepper-step
          :complete="cart > 1"
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
          step="2"
        >
          Daten
          <small></small>
        </v-stepper-step>

        <v-stepper-content step="2">
          <v-list class="snapshotlist shop"
            three-line>
            <div v-for="(snapshot, index) in groupedsnapshots" :key="snapshot.id">
              <v-subheader
                v-if="showTopic(index)"
                class="px-0">{{ snapshot.topic }}</v-subheader>
              <snapshot-order-item
                :data="snapshot"
                v-on:toggle="toggleItemOrder"
                />
              </div>
          </v-list>
          <p>&nbsp;</p>
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
          Zusatz
          <small></small>
        </v-stepper-step>

        <v-stepper-content step="3">
            <v-textarea
              placeholder="Ich benötige zusätzlich folgende Grundlagen oder Analysen..."
              v-on:keyup="updateCommentData">
            </v-textarea>
          <v-btn
            color="primary"
            @click="submitRequest"
          >
            Anfragen
          </v-btn>
        </v-stepper-content>

      </v-stepper>
      <div class="successMessage" v-else>
        <h1 class="text-xl uppercase">Vielen Dank.</h1>
        <p>Die Bestellung wurde erfolgreich erfasst 🎉<br>
        Wir melden uns baldmöglichst bei Ihnen.</p>
        <v-btn color="primary" @click="resetForm">Neu starten</v-btn>
      </div>

  </div>
</template>

<style>
.shop {
  height: 40vh;
  overflow-y: scroll;
}
.successMessage {
  height: 20vh;
  align-content: center;
  text-align: center;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import _ from 'lodash';
import { mapActions, mapGetters } from 'vuex';
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
      ordered: false
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
        this.setPerimeter(this.municipality);
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
    }, 500),

    showTopic(curindex) {
      if (curindex > 0) {
        if (this.groupedsnapshots[curindex - 1].topic !== this.groupedsnapshots[curindex].topic) {
          return true;
        }
        return false;
      }
      return true;
    },

    ...mapActions('snapshotStore', [
      'updateComment', 'toggleItem', 'setPerimeter', 'resetCart', 'saveCart', 'updateStoreUrl'
    ]),

    updateCommentData(e) {
      if (e.srcElement) {
        this.updateComment(e.srcElement.value);
      }
    },

    toggleItemOrder(snapshot) {
      this.toggleItem(snapshot);
    },

    async submitRequest() {
      this.cart = 4;
      // commit('SET_LOADING', true);

      const headers = {
        'Content-Type': 'application/json'
      };

      await this.$storeApi.post('', JSON.stringify(this.getCart), { headers })
        .then((res) => {
          if (res.data.status === 'success') {
            this.ordered = true;
          }
        }).catch((err) => {
          console.log(err); // eslint-disable-line no-console
        });
    },

    cancelOrder() {
      this.resetForm();
      this.$emit('back');
    },

    resetForm() {
      this.cart = 1;
      this.resetCart();
      this.ordered = false;
    }
  },

  async mounted() {
    fetch(`${this.snapshotStoreUrl}?lang=${this.$i18n.locale}`)
      .then(response => response.json())
      .then((data) => {
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
    },
    groupedsnapshots() {
      const topicgroups = {};
      this.snapshotsStore.forEach((snapshot) => {
        if (typeof (topicgroups[snapshot.topic]) === 'undefined') {
          topicgroups[snapshot.topic] = [];
        }
        topicgroups[snapshot.topic].push(snapshot);
      });

      return Object.values(topicgroups).flat();
    },
    ...mapGetters('snapshotStore', [
      'getCart'
    ])
  },

  watch: {
    async perimeterSearch(val) {
      this.debouncedQuery(val, this);
    }
  }
};
</script>
