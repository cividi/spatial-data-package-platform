<!-- eslint-disable -->
<i18n>
{
  "de": {
    "objectslink": "Alle Objekte",
    "PAR": {
      "objectslink": "@:objectslink"
    },
    "MGT": {
      "objectslink": "@:objectslink"
    }
  },
  "fr": {
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
        <img alt="dføur logo" height="36" src="@/assets/images/logo.svg">
      </router-link>

      <v-divider />

      <div id="snapshotnavContent" class="ma-4">

        <div class="nodata pb-8">
          <div class="smaller hint">
            <h4>{{ title }}</h4>
            <p class="show-linebreaks">{{ description }}</p>
            <v-btn
              v-if="annotations.object.showlink"
              :to="'/' + $i18n.locale + '/' + wshash + '/annotations/OBJ/'"
              class="listlink elevation-0"
              block
            >
              <v-icon left>
                mdi-view-grid
              </v-icon>
              {{ $t('objectslink') }}
            </v-btn>
          </div>
        </div>

        <snapshot-list
          :snapshots="snapshotsWorkspace"
          :workspaceHash="wshash"
          :snapshotHash="hash"
          v-on:editme="editSnapshot"
        />

        <v-btn
          v-if="$store.state.isUserLoggedIn"
          fab color="primary"
          @click="newSnapshot" >
        <v-icon>mdi-plus</v-icon>
        </v-btn>
      </div>

      <v-toolbar
        width="320"
        absolute
        bottom>
        <div class="useractions">
          <user-actions noLogin="1" />
        </div>
        <v-spacer />
        <language-switch />
      </v-toolbar>
    </v-navigation-drawer>

    <snapshot-map ref="map"
      v-if="hash"
      :geojson="geojson"
      :annotations="annotations"
      :spatialDatasettes="spatialDatasettes"
      :geoboundsIn="geobounds"
    />

    <annotations-list ref="map"
      v-if="annokind"
      :annotations="annotations.items"
      :kind="annokind"
      :categories="annotations.categories"
      :states="annotations.states"
    />

    <v-overlay
      absolute="absolute"
      opacity="0.2"
      z-index="1002"
      :value="!!editing"
      >
      <snapshot-edit
        v-if="editing"
        :isNew="editing.isNew"
        v-bind="editing.snapshot"
        v-on:cancel="abortEdit"
        v-on:saved="onSnapshotSaved"
      />
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

.show-linebreaks {
  white-space: pre-wrap;
}

h4 {
  margin-bottom: 0.8em;
}

.listlink {
  text-transform: initial;
  font-weight: 700;
  font-size: 13px;
  opacity: 1;
  letter-spacing: 0;
}
.listlink span {
  justify-content: flex-start;
}
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import AnnotationsList from '../components/AnnotationsList.vue';
import SnapshotList from '../components/SnapshotList.vue';
import SnapshotMap from '../components/SnapshotMap.vue';
import SnapshotEdit from '../components/SnapshotEdit.vue';
import ErrorMessage from '../components/ErrorMessage.vue';


Vue.component('annotations-list', AnnotationsList);
Vue.component('snapshot-list', SnapshotList);
Vue.component('snapshot-map', SnapshotMap);
Vue.component('snapshot-edit', SnapshotEdit);
Vue.component('error-message', ErrorMessage);

export default {
  data() {
    return {
      hash: this.$route.params.hash,
      wshash: this.$route.params.wshash,
      annokind: this.$route.params.annokind,
      geojson: null,
      annotations: {
        items: [],
        categories: null,
        states: null,
        usergroups: null,
        mode: '',
        findme: false,
        marker: {
          open: false,
          likes: false
        },
        polygon: {
          open: false,
          likes: false
        },
        object: {
          open: false,
          likes: false
        }
      },
      spatialDatasettes: null,
      geobounds: [],
      municipalityName: '',
      snapshotsWorkspace: [],
      title: '',
      description: '',
      errorsettings: {},
      editing: undefined
    };
  },

  async mounted() {
    await this.getWorkspaceInfo();
    if (this.hash) {
      await this.getWorkspaceData();
    }
    if (this.geojson) {
      this.$refs.map.setupMeta();
      this.$refs.map.setupMapbox();
      this.$refs.map.displayMapbox();
      document.title = `dføur – ${this.title}`;
    }
  },

  computed: {
    municipality() {
      if (this.$route.params.hasOwnProperty('municipality') && this.$route.params.municipality) {
        return this.$route.params.municipality;
      }
      return null;
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
          query: gql`query getworkspace($wshash: ID!, $hash: ID!, $lang: LanguageCodeEnum!) {
            workspace(id: $wshash) {
              id
              pk
              title
              description
              mode
              findmeEnabled
              annotationsOpen
              annotationsLikesEnabled
              polygonOpen
              polygonLikesEnabled
              objectOpen
              objectLikesEnabled
              objectsPageLink
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
              annotations {
                id
                pk
                kind
                rating
                data
                category {
                  pk
                  name(languageCode: $lang)
                  icon
                  color
                  commentsEnabled
                }
                state {
                  pk
                  name(languageCode: $lang)
                  decoration
                }
                attachements {
                  document
                  myOrder
                }
              }
              categories {
                pk
                color
                name(languageCode: $lang)
                hideInList
                hideInLegend
                icon
              }
              states {
                pk
                name(languageCode: $lang)
                decoration
                hideInList
                hideInLegend
              }
              spatialDatasettes {
                name
                baseUrl
                queries
              }
              usergroups {
                key
                name(languageCode: $lang)
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
            hash: btoa(`SnapshotNode:${this.hash}`),
            lang: this.$route.params.lang
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
      if (workspaceInfo.snapshot) {
        const snapshot = workspaceInfo.snapshot;
        if (!workspace.snapshots.map(s => s.pk).includes(snapshot.pk)) {
          this.$router.push({ name: 'home' });
        }
        this.municipalityName = snapshot.municipality.fullname;
        this.$store.commit('setBfsnumber', snapshot.municipality.bfsNumber);
        this.$store.commit('setBfsname', snapshot.municipality.fullname);
      }

      this.snapshotsWorkspace = workspace.snapshots;
      this.annotations.items = workspace.annotations;
      this.annotations.categories = workspace.categories;
      this.annotations.states = workspace.states;
      this.annotations.usergroups = workspace.usergroups;
      this.annotations.mode = workspace.mode;
      this.annotations.findme = workspace.findmeEnabled;
      this.annotations.marker.open = workspace.annotationsOpen;
      this.annotations.marker.likes = workspace.annotationsLikesEnabled;
      this.annotations.polygon.open = workspace.polygonOpen;
      this.annotations.polygon.likes = workspace.polygonLikesEnabled;
      this.annotations.object.open = workspace.objectOpen;
      this.annotations.object.likes = workspace.objectLikesEnabled;
      this.annotations.object.showlink = workspace.objectsPageLink;

      this.spatialDatasettes = workspace.spatialDatasettes;
      this.title = workspace.title;
      this.description = workspace.description;
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
    abortEdit() {
      this.editing = undefined;
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
    newSnapshot() {
      this.editing = { isNew: true, snapshot: {} };
    }
  }
};
</script>
