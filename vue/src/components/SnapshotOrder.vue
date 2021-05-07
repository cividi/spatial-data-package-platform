<!-- eslint-disable -->
<i18n>
{
  "de": {
    "addSnapshot.order": "Kartenlayer bestellen",
    "placeholder": "Gemeindename",
    "label": "Gemeinde",
    "name": "Vor- und Nachname",
    "name.invalid": "Bitte Vor- und Nachname eingeben",
    "email": "E-Mail Adresse",
    "email.invalid": "Ungültige E-Mail Adresse",
    "phone": "Telefon",
    "phone.invalid": "Ungültige Telefonnummer Adresse",
    "mandatory": "Dies ist ein Pflichtfeld",
    "comment": "Brauchen Sie zusätzliche Kartenlayer oder Analysen oder Perimeter?"
  },
  "fr": {
    "addSnapshot.order": "Données de la commande",
    "placeholder": "Recherche",
    "label": "Communauté",
    "name": "Vor- und Nachname",
    "name.invalid": "Bitte Vor- und Nachname eingeben",
    "email": "E-Mail Adresse",
    "email.invalid": "Ungültige E-Mail Adresse",
    "phone": "Telefon",
    "phone.invalid": "Ungültige Telefonnummer Adresse",
    "mandatory": "Ce champ est obligatoire",
    "comment": "Brauchen Sie zusätzliche Kartenlayer oder Analysen oder Perimeter?"
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
          <span v-if="cart > 1">{{ perimeter.bfsname }}</span>
        </v-stepper-step>

        <v-stepper-content step="1">
          <p class="body">Kartenlayer werden jeweils für die gesamte Gemeinde
              <b>{{ perimeter.bfsname }}</b>
              aufbereitet. Bitte fügen Sie eine Bemerkung hinzu, falls Sie einen anderen
              Perimeter oder gemeindeübergreifende Karten benötigen.</p>
          <v-btn
            color="primary"
            @click="cart = 2"
          >
            Weiter
          </v-btn>
          <!-- <template>
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
            </template> -->

        </v-stepper-content>

        <v-stepper-step
          :complete="cart > 2"
          step="2"
        >
          Daten
          <span v-if="cart > 2">{{ noPackages }}</span>
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
            :disabled="!form.packages.length"
            @click="cart = 3"
          >
            Auswählen
          </v-btn>
        </v-stepper-content>

        <v-stepper-step
          :complete="cart > 3"
          step="3"
        >
          Bermerkungen
          <small></small>
        </v-stepper-step>

        <v-stepper-content step="3">
            {{ $t('comment') }}
            <v-textarea
              v-model="form.comment">
            </v-textarea>
          <v-btn
            color="primary"
            @click="cart = 4"
          >
            Weiter
          </v-btn>
        </v-stepper-content>

        <v-stepper-step
          :complete="cart > 4"
          step="4"
        >
          Kontakt
          <small></small>
        </v-stepper-step>

        <v-stepper-content step="4">
          <v-text-field
            ref="formName"
            v-model="form.name"
            :label="$t('name')"
            :rules="[validate.required, validate.name]"
            required
          />
          <v-text-field
            ref="formEmail"
            v-model="form.email"
            :label="$t('email')"
            :rules="[validate.required, validate.email]"
            required
          />
          <v-text-field
            v-model="form.phone"
            :rules="[validate.phone]"
            :label="$t('phone')"
          />
          <v-btn
            color="primary"
            :disabled="$refs.formEmail ? $refs.formEmail.hasError || $refs.formName.hasError : true"
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
import SnapshotOrderItem from './SnapshotOrderItem.vue';

Vue.component('snapshot-order-item', SnapshotOrderItem);

export default {
  name: 'SnapshotOrder',

  props: [
    'perimeter'
  ],

  data() {
    const defaultForm = Object.freeze({
      name: null,
      email: null,
      phone: null,
      perimeter: this.perimeter,
      comment: '',
      packages: []
    });

    return {
      cart: 1,
      form: Object.assign({}, defaultForm),
      snapshotStoreUrl: process.env.VUE_APP_SNAPSHOTSTOREURL,
      snapshotsStore: [],
      ordered: false,
      validate: {
        required: value => !!value || this.$t('mandatory'),
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || this.$t('email.invalid');
        },
        phone: (value) => {
          const pattern = /^\+?(?:[0-9]\s?){6,14}[0-9]$/;
          if (value.length > 0) {
            return pattern.test(value) || this.$t('phone.invalid');
          }
          return true;
        },
        name: value => value.indexOf(' ') >= 0 || this.$t('name.invalid')
      }
    };
  },

  methods: {

    showTopic(curindex) {
      if (curindex > 0) {
        if (this.groupedsnapshots[curindex - 1].topic !== this.groupedsnapshots[curindex].topic) {
          return true;
        }
        return false;
      }
      return true;
    },

    toggleItemOrder(item) {
      this.form.packages = this.form.packages.includes(item)
        ? this.form.packages.filter(i => i !== item) : [...this.form.packages, item];
    },

    async submitRequest() {
      this.cart = 4;

      const headers = {
        'Content-Type': 'application/json'
      };

      const submitData = this.form;
      submitData.perimeter = submitData.perimeter.bfsnumber;
      submitData.firstname = submitData.name.split(' ')[0];
      submitData.lastname = submitData.name.split(' ')[1];

      await this.$storeApi.post('', JSON.stringify(submitData), { headers })
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
    noPackages() {
      if (!this.form.packages.length) {
        return '';
      }
      return `${this.form.packages.length} / ${this.groupedsnapshots.length}`;
    }
  }
};
</script>
