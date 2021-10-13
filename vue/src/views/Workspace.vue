<!-- eslint-disable -->
<i18n>
{
  "de": {
    "cancel": "abbrechen",
    "mySnapshots": "Meine Kartenlayer",
    "addSnapshot": "Kartenlayer hinzufügen",
    "workspace.intro": "Willkommen bei {platformName}. Dies ist dein persönlicher Workspace. Einführungs-video anschauen.",
    "snapshotEdit.warning": "Bearbeiten des Workspaces ist nur eingeloggt möglich."
  },
  "fr": {
    "cancel": "Annuler",
    "mySnapshots": "Mes couche de données",
    "addSnapshot": "Ajouter des données",
    "workspace.intro": "Einführungsvideo: youtube.com/XYZ",
    "snapshotEdit.warning": "La modification des workspace n'est possible qu'en étant connecté."
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div id="snapshotview">
    <v-navigation-drawer
      v-if="$store.state.notIframe"
      id="snapshotnav"
      clipped="clipped"
      app
      width="320"
      v-model="snapshotnav">
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-4 d-block">
        <img alt="dføur logo" height="36" src="@/assets/images/logo-dfour.svg">
      </router-link>

      <v-divider />

      <div id="snapshotnavContent" class="ma-4">

        <v-alert
          v-if="$store.state.isUserLoggedIn && onboardingTipsWorkspace"
          icon="mdi-lightbulb-outline"
          outlined dense dismissible
          class="body-2"
          color="primary"
          v-on:click="dismissTip('workspace')"
        >
          {{ $t('workspace.intro', { platformName: "dføur" }) }}
        </v-alert>

        <div class="nodata">
          <div class="smaller hint">
            <h4>{{ title }}</h4>
          </div>
        </div>

        <div class="nodata pb-8">
          <div class="smaller hint">
            <p class="show-linebreaks">{{ description }}</p>
          </div>
        </div>

        <div class="px-0" v-if="$store.state.isUserLoggedIn">
          <div class="smaller hint">
            <h4>{{ $t('mySnapshots') }}</h4>
          </div>
        </div>

        <snapshot-list
          :snapshots="snapshotsWorkspace"
          :workspaceHash="wshash"
          :snapshotHash="hash"
          v-on:editme="editSnapshot"
        />

        <v-list class="snapshotlist"
          three-line
          v-if="$store.state.isUserLoggedIn">
          <v-list-item class="px-0 mb-4 requestable"
            dense @click="addSnapshot">
            <v-list-item-avatar tile size="64" class="my-0">
              <v-icon>mdi-layers-plus</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title style="font-weight:700">{{ $t('addSnapshot') }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <v-alert
          v-if="!$store.state.isUserLoggedIn"
          icon="mdi-shield-lock-outline"
          text outlined dense
          class="body-2"
          color="grey"
        >
          {{ $t('snapshotEdit.warning') }}
        </v-alert>

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
    />
    <v-overlay
      absolute="absolute"
      opacity="0.9"
      z-index="1002"
      :value="!!overlayVisible"
      >


      <v-card
        id="snapshotadd" light class="pa-4"
        :class="{ snapshotordering: ordering, snapshotediting: editing }">
        <v-tooltip right>
          <template v-slot:activator="{ on, attrs }">
            <v-icon
              v-bind="attrs" v-on="on"
              style="position: absolute; top:10px; right:5px;"
              class="pa-2"
              @click="abortAddSnapshot" >mdi-close-circle-outline
            </v-icon>
          </template>
          <span>{{ $t('cancel') }}</span>
        </v-tooltip>

        <snapshot-add
          v-if="!ordering && !editing"
          v-on:order="newOrder"
          v-on:new="newSnapshot"
        />

        <snapshot-order
          v-if="ordering"
          :perimeter="perimeter"
          v-on:back="goBack"
        />

        <snapshot-edit
          v-if="editing"
          :isNew="editing.isNew"
          v-bind="editing.snapshot"
          v-on:back="goBack"
          v-on:saved="onSnapshotSaved"
        />

      </v-card>

     </v-overlay>

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

#snapshotadd {
  width: 90vw;
  min-width: 300px;
  max-width: 500px;
}

@media only screen and (max-width: 600px) {
  #snapshotadd {
    width: 100vw;
    height: 100vh;
    border-radius: 0;
  }
}

/* .snapshotordering {
  width: 95vw !important;
  height: 80vh;
  max-width: 1100px !important;
} */

.snapshotediting {
  max-width: 400px !important;
  width: 95vw !important;
}

.show-linebreaks {
  white-space: pre-wrap;
}

h4 {
  margin-bottom: 0.8em;
}

.addSnapshotButton {
  width: 50% !important;
  min-height: 200px;
  margin-top: 20px;
  border-radius: 5px;
  text-transform: none;
}

.choice-btn__content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.choice-btn__content i.choice {
  width: 80px !important;
  height: 80px !important;
  font-size: 70px !important;
}

.choice-btn__content p {
  padding-top: 5px;
  font-size: 1em;
}
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import SnapshotList from '../components/SnapshotList.vue';
import SnapshotMap from '../components/SnapshotMap.vue';
import SnapshotEdit from '../components/SnapshotEdit.vue';
import SnapshotOrder from '../components/SnapshotOrder.vue';
import ErrorMessage from '../components/ErrorMessage.vue';
import SnapshotAdd from '../components/SnapshotAdd.vue';

Vue.component('snapshot-list', SnapshotList);
Vue.component('snapshot-map', SnapshotMap);
Vue.component('snapshot-edit', SnapshotEdit);
Vue.component('snapshot-order', SnapshotOrder);
Vue.component('error-message', ErrorMessage);

export default {
  components: { SnapshotAdd },
  data() {
    return {
      hash: this.$route.params.hash,
      wshash: this.$route.params.wshash,
      geojson: null,
      geobounds: [],
      municipalityName: '',
      snapshotsWorkspace: [],
      title: '',
      description: '',
      errorsettings: {},
      addsnapshot: undefined,
      editing: undefined,
      ordering: undefined,
      onboardingTipsWorkspace: true,
      snapshotsStore: [],
      snapshotStoreUrl: process.env.VUE_APP_SNAPSHOTSTOREURL
    };
  },

  async mounted() {
    if (localStorage.onboardingTipsWorkspace) {
      if (localStorage.onboardingTipsWorkspace === 'true') {
        this.onboardingTipsWorkspace = true;
      } else {
        this.onboardingTipsWorkspace = false;
      }
    }
    await this.getWorkspaceInfo();
    await this.getWorkspaceData();
    if (this.geojson) {
      this.$refs.map.setupMeta();
      this.$refs.map.setupMapbox();
      this.$refs.map.displayMapbox();
    }

    fetch(`${this.snapshotStoreUrl}?lang=${this.$i18n.locale}`)
      .then(response => response.json())
      .then((data) => {
        data.forEach((el, i) => {
          data[i].thumbnail = `${this.snapshotStoreUrl}/${el.thumbnail}`;
        });

        this.snapshotsStore = data;
      });
  },

  computed: {
    municipality() {
      if (this.$route.params.hasOwnProperty('municipality') && this.$route.params.municipality) {
        return this.$route.params.municipality;
      }
      return null;
    },

    overlayVisible() {
      if (!!this.addsnapshot || !!this.ordering || !!this.editing) {
        return true;
      }
      return false;
    },

    perimeter() {
      return {
        bfsname: this.$store.state.bfsname,
        bfsnumber: this.$store.state.bfsnumber
      };
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
    async getWorkspaceInfo() {
      let workspaceInfo = this.$store.getters.WorkspaceInfoByHash(this.wshash);

      if (!workspaceInfo) {
        const result = await this.$apollo.query({
          query: gql`query getworkspace($wshash: ID!, $hash: ID!) {
            workspace(id: $wshash) {
              id
              pk
              title
              description
              snapshots {
                id
                pk
                title
                topic
                screenshot
                thumbnail
                datafile
                municipality {
                  bfsNumber
                  fullname
                }
              }
            }

            snapshot(id: $hash) {
              id
              pk
              municipality {
                bfsNumber
                fullname
                snapshots {
                  id
                  pk
                  title
                  topic
                  screenshot
                  thumbnail
                  datafile
                }
              }
            }
          }`,
          variables: {
            wshash: btoa(`WorkspaceNode:${this.wshash}`),
            hash: btoa(`SnapshotNode:${this.hash}`)
          }
        }).catch((error) => {
          this.errorsettings = { type: 'netwokerror', open: true, error };
        });
        if (result) {
          if (result.data.hasOwnProperty('workspace') && result.data.workspace) {
            workspaceInfo = result.data;
            this.$store.commit('addWorkspaceInfo', { hash: this.wshash, value: workspaceInfo });
          } else {
            this.$router.push({ name: 'home' });
          }
        }
      }
      const workspace = workspaceInfo.workspace;
      const snapshot = workspaceInfo.snapshot;
      if (!workspace.snapshots.map(s => s.pk).includes(snapshot.pk)) {
        this.$router.push({ name: 'home' });
      }
      this.municipalityName = snapshot.municipality.fullname;
      this.snapshotsWorkspace = workspace.snapshots;
      this.title = workspace.title;
      this.description = workspace.description;
      this.$store.commit('setBfsnumber', snapshot.municipality.bfsNumber);
      this.$store.commit('setBfsname', snapshot.municipality.fullname);
    },

    async getWorkspaceData() {
      const result = await this.$apollo.query({
        query: gql`query getworkspace($wshash: ID!, $hash: ID!) {
          workspace(id: $wshash) {
            id
            pk
            title
          }
          snapshot(id: $hash) {
            id
            pk
            data
          }
        }`,
        variables: {
          wshash: btoa(`WorkspaceNode:${this.wshash}`),
          hash: btoa(`SnapshotNode:${this.hash}`)
        },
        options: {
          cachePolicy: 'no-cache'
        }
      }).catch((error) => {
        this.errorsettings = { type: 'netwokerror', open: true, error };
      });
      if (result) {
        if (result.data.hasOwnProperty('workspace') && result.data.workspace) {
          this.geojson = result.data.snapshot.data;
        } else {
          this.$router.push({ name: 'home' });
        }
      }
    },
    editSnapshot(snapshot) {
      this.editing = { isNew: false, snapshot };
    },
    goBack() {
      this.editing = undefined;
      this.ordering = undefined;
    },
    async onSnapshotSaved({ snapshot }) {
      const { data } = await this.$apollo.query({
        query: gql`query getworkspace($wshash: ID!) {
            workspace(id: $wshash) {
              snapshots {
                id
                pk
                title
                topic
                screenshot
                thumbnail
                datafile
                municipality {
                  bfsNumber
                  fullname
                }
              }
            }
          }
        `,
        variables: {
          wshash: btoa(`WorkspaceNode:${this.wshash}`)
        },
        fetchPolicy: 'no-cache'
      });
        // abusing vue's watching of Array.prototype.splice because it just wouldn't react otherwise
      this.snapshotsWorkspace.splice(
        0,
        this.snapshotsWorkspace.length,
        ...data.workspace.snapshots
      );
      this.editing = undefined;

      if (this.$route.params.hash === snapshot.pk) {
        // current snapshot was updated, reload window
        this.$router.go();
      } else {
        // co to edited snapshot
        this.$router.push(`/${
          this.$route.params.lang
        }/${
          this.$route.params.wshash
        }/${
          snapshot.pk
        }/`);
      }
    },
    addSnapshot() {
      this.addsnapshot = true;
    },
    abortAddSnapshot() {
      this.addsnapshot = undefined;
      this.ordering = undefined;
      this.editing = undefined;
    },
    newSnapshot() {
      this.editing = { isNew: true, snapshot: {} };
      this.ordering = undefined;
    },
    newOrder() {
      this.ordering = true;
      this.editing = undefined;
    },
    abortOrder() {
      this.ordering = undefined;
      this.addsnapshot = undefined;
    },
    dismissTip() {
      this.onboardingTipsWorkspace = false;
      localStorage.onboardingTipsWorkspace = this.onboardingTipsWorkspace;
    }
  }
};
</script>
