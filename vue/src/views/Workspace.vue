<!-- eslint-disable -->
<i18n>
{
  "de": {
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
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-divider />

      <div id="snapshotnavContent" class="ma-4">

        <div class="nodata pb-8">
          <div class="smaller hint">
            <h4>{{ title }}</h4>
            <p class="show-linebreaks">{{ description }}</p>
          </div>
        </div>

        <snapshot-list
          :snapshots="snapshotsWorkspace"
          :workspaceHash="wshash"
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
</style>

<script>
import Vue from 'vue';
import gql from 'graphql-tag';
import SnapshotList from '../components/SnapshotList.vue';
import SnapshotMap from '../components/SnapshotMap.vue';

Vue.component('snapshot-list', SnapshotList);
Vue.component('snapshot-map', SnapshotMap);

export default {
  data() {
    return {
      hash: this.$route.params.hash,
      wshash: this.$route.params.wshash,
      geojson: null,
      geobounds: [],
      municipalityName: '',
      snapshotsWorkspace: [],
      title: '',
      description: ''
    };
  },

  async mounted() {
    await this.getWorkspace();
    if (this.geojson) {
      this.$refs.map.setupMeta();
      this.$refs.map.setupMapbox();
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
    async getWorkspace() {
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
              screenshot {
                url
              }
            }
          }

          snapshot(id: $hash) {
            id
            pk
            data
            municipality {
              bfsNumber
              fullname
              snapshots {
                id
                pk
                title
                topic
                screenshot {
                  url
                }
            }
            }
          }
        }`,
        variables: {
          wshash: btoa(`WorkspaceNode:${this.wshash}`),
          hash: btoa(`SnapshotNode:${this.hash}`)
        }
      });
      if (result.data.hasOwnProperty('workspace') && result.data.workspace) {
        const workspace = result.data.workspace;
        const snapshot = result.data.snapshot;
        if (!workspace.snapshots.map(s => s.pk).includes(snapshot.pk)) {
          this.$router.push({ name: 'home' });
        }
        this.geojson = snapshot.data;
        this.municipalityName = snapshot.municipality.fullname;
        this.snapshotsWorkspace = workspace.snapshots;
        this.title = workspace.title;
        this.description = workspace.description;
        this.$store.commit('setBfsnumber', snapshot.municipality.bfsNumber);
        this.$store.commit('setBfsname', snapshot.municipality.fullname);
      } else {
        this.$router.push({ name: 'home' });
      }
    }
  }
};
</script>
