<!-- eslint-disable -->
<i18n>
{
  "de": {
    "calltoactionText": "Angebot für Ihre Gemeinde einholen",
    "hasSnapshot.title": "Datenverfügbarkeit",
    "hasSnapshot.p1": "Für {municipalityText} stehen erste Daten zur Verfügung.",
    "hasSnapshot.p2": "Erkunden Sie unsere weiteren Fallbeispiele um ein besseres Bild der Möglichkeiten für Ihre Gemeinde zu erhalten.",
    "noSnapshot.title": "Datenverfügbarkeit",
    "noSnapshot.municipalityText": "diese Gemeinde",
    "noSnapshot.p1": "Für {municipalityText} sind zur Zeit noch keine Analysen freigeschaltet.",
    "noSnapshot.p2": "Erkunden Sie unsere Fallbeispiele um ein besseres Bild der Möglichkeiten für Ihre Gemeinde zu erhalten.",
    "listtitle": "Fallbeispiele",
    "listtitleMore": "Weitere Fallbeispiele"
  },
  "fr": {
    "calltoactionText": "Offre pour votre commune",
    "hasSnapshot.title": "Disponibilité des données",
    "hasSnapshot.p1": "Les premières données concernant {municipalityText} sont disponibles.",
    "hasSnapshot.p2": "Prenez compte de nos études pour une meilleure vue d’ensemble des possibilitiées qui s’offrent à votre commune.",
    "noSnapshot.title": "Disponibilité des données",
    "noSnapshot.municipalityText": "cette communauté",
    "noSnapshot.p1": "En ce moment il n’éxiste pas encore de données pour {municipalityText}.",
    "noSnapshot.p2": "Prenez compte de nos études pour une meilleure vue d’ensemble des possibilitiées qui s’offrent à votre commune.",
    "listtitle": "Examples",
    "listtitleMore": "D'autres examples"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div id="snapshotview">
    <v-navigation-drawer
      v-if="$store.state.notIframe && !screenshotMode"
      id="snapshotnav"
      clipped="clipped"
      app
      width="320"
      v-model="snapshotnav">
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-divider />

      <div id="snapshotnavContent" class="ma-4">
        <search :dense="true" :term="municipalityName"/>

        <div v-if="!hash" class="nodata pb-8">
          <div class="smaller hint">
            <!-- <h4>{{ $t('noSnapshot.title') }}</h4> -->
            <p>{{ $t('noSnapshot.p1', { municipalityText: municipalityText }) }}</p>
            <p>{{ $t('noSnapshot.p2') }}</p>
          </div>
        </div>

        <div class="useractions">
          <v-btn small block outlined color="primary">
            <router-link key="signup" :to="'/' + $i18n.locale + '/signup/'">
              {{ $t('calltoactionText', { municipalityText: municipalityText }) }}
            </router-link>
          </v-btn>
        </div>

        <snapshot-list
            v-if="hash"
            :snapshots="snapshotsMunicipality" :withTopic="false"
          />

        <snapshot-list
          v-if="snapshotsStore"
          :snapshots="snapshotsStore" :withTopic="true"
        />

        <v-subheader
          class="px-0 snapshot-list-title">{{ listtitleText }}
        </v-subheader>

        <snapshot-list
          v-if="snapshotsExamples"
          :snapshots="snapshotsExamples" :withTopic="false"
        />

      </div>

      <v-toolbar
        width="320"
        absolute
        bottom>
        <div class="useractions">
          <user-actions noRequest="1" />
        </div>
        <v-spacer/>
        <language-switch/>
      </v-toolbar>
    </v-navigation-drawer>

    <snapshot-map ref="map"
      :geojson="geojson"
      :geoboundsIn="geobounds"
      :predecessor="predecessor"
    />

     <error-message
      :settings="errorsettings"
    />
  </div>
</template>

<style>
#snapshotview .v-text-field--outlined fieldset {
  border-color: rgba(0, 0, 0, 0.12);
}

#snapshotview .gemeindesuche input::placeholder {
  color: #000;
  opacity: 1;
  font-weight: 900;
}

h4 {
  margin-bottom: 0.8em;
}
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import SnapshotList from '../components/SnapshotList.vue';
import SnapshotMap from '../components/SnapshotMap.vue';
import ErrorMessage from '../components/ErrorMessage.vue';

Vue.component('snapshot-list', SnapshotList);
Vue.component('snapshot-map', SnapshotMap);
Vue.component('error-message', ErrorMessage);

export default {
  data() {
    return {
      hash: this.$route.params.hash,
      bfsNumber: this.$route.params.bfsNumber,
      snapshotStoreUrl: process.env.VUE_APP_SNAPSHOTSTOREURL,
      geojson: null,
      geobounds: [],
      municipalityName: '',
      snapshotsStore: [],
      snapshotsExamples: [],
      snapshotsIdExamplesExclude: [],
      snapshotsMunicipality: [],
      predecessor: null,
      screenshotMode: this.$route.query.hasOwnProperty('screenshot'),
      screenshotIsThumbnail: this.$route.query.hasOwnProperty('thumbnail'),
      errorsettings: {}
    };
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

    if (this.hash) {
      await this.getSnapshotInfo(this.hash);

      await this.getSnapshotData(this.hash);
      if (this.geojson) {
        this.$refs.map.setupMeta();
        this.$refs.map.setupMapbox();
        this.$refs.map.displayMapbox();
      }
    } else {
      await this.getEmpty(this.bfsNumber);
      this.$refs.map.setupEmpty();
      this.$refs.map.displayMapbox();
    }
  },

  computed: {
    municipality() {
      if (this.$route.params.hasOwnProperty('municipality') && this.$route.params.municipality) {
        return this.$route.params.municipality;
      }
      return null;
    },

    municipalityText() {
      return this.municipalityName ? this.municipalityName : this.$t('noSnapshot.municipalityText');
    },

    listtitleText() {
      if (this.snapshotsMunicipality.length > 0) {
        return this.$t('listtitleMore');
      }
      return this.$t('listtitle');
    },

    snapshotnav: {
      get() {
        return this.$store.state.snapshotnav;
      },
      set(val) {
        this.$store.commit('setSnapshotnav', val);
      }
    }
  },

  methods: {
    async getSnapshotInfo(hash) {
      const result = await this.$apollo.query({
        query: gql`query getsnapshot($hash: ID!) {
          snapshot(id: $hash) {
            id
            pk
            predecessor {
              id
              pk
            }
            municipality {
              bfsNumber
              fullname
              snapshots {
                id
                pk
                title
                topic
                thumbnail
                screenshot
              }
            }
          }

          snapshots(isShowcase: true) {
            edges {
              node {
                id
                pk
                title
                topic
                thumbnail
                screenshot
              }
            }
          }
        }`,
        variables: {
          hash: btoa(`SnapshotNode:${hash}`)
        }
      }).catch((error) => {
        this.errorsettings = { type: 'netwokerror', open: true, error };
      });
      if (result) {
        if (result.data.hasOwnProperty('snapshot') && result.data.snapshot) {
          this.municipalityName = result.data.snapshot.municipality.fullname;
          this.snapshotsMunicipality = result.data.snapshot.municipality.snapshots;
          const snapshotsIdExamplesExclude = this.snapshotsMunicipality.map(
            snapshot => snapshot.id
          );
          this.snapshotsExamples = result.data.snapshots.edges.map(
            snapshot => snapshot.node
          ).filter(
            snapshot => !snapshotsIdExamplesExclude.includes(snapshot.id)
          );
          this.predecessor = (result.data.snapshot.predecessor);
          this.$store.commit('setBfsnumber', result.data.snapshot.municipality.bfsNumber);
          this.$store.commit('setBfsname', result.data.snapshot.municipality.fullname);
        } else {
          this.$router.push({ name: 'home' });
        }
      }
    },

    async getSnapshotData(hash) {
      const result = await this.$apollo.query({
        query: gql`query getsnapshot($hash: ID!) {
          snapshot(id: $hash) {
            id
            pk
            data
          }
        }`,
        variables: {
          hash: btoa(`SnapshotNode:${hash}`)
        }
      }).catch((error) => {
        this.errorsettings = { type: 'netwokerror', open: true, error };
      });
      if (result) {
        if (result.data.hasOwnProperty('snapshot') && result.data.snapshot) {
          this.geojson = result.data.snapshot.data;
        } else {
          this.$router.push({ name: 'home' });
        }
      }
    },

    async getEmpty(bfsNumber) {
      const result = await this.$apollo.query({
        query: gql`query getmunicipality($bfsNumber: ID!) {
          municipality(id: $bfsNumber) {
            id
            bfsNumber
            fullname
            perimeter
            perimeterBounds
            snapshots {
              id
              pk
              title
              topic
              thumbnail
              screenshot
            }
          }

          snapshots(isShowcase: true) {
            edges {
              node {
                id
                pk
                title
                topic
                thumbnail
                screenshot
              }
            }
          }
        }`,
        variables: {
          bfsNumber: btoa(`MunicipalityNode:${bfsNumber}`)
        }
      }).catch((error) => {
        this.errorsettings = { type: 'netwokerror', open: true, error };
      });
      if (result) {
        this.municipalityName = result.data.municipality.fullname;
        this.geojson = result.data.municipality.perimeter;
        this.geobounds = result.data.municipality.perimeterBounds;
        this.snapshotsExamples = result.data.snapshots.edges.map(snapshot => snapshot.node);
        this.$store.commit('setBfsnumber', result.data.municipality.bfsNumber);
        this.$store.commit('setBfsname', result.data.municipality.fullname);
      }
    }
  }
};
</script>
