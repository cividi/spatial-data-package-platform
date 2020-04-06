<!-- eslint-disable -->
<i18n>
{
  "de": {
    "listtitle": "Scans"
  },
  "fr": {
    "listtitle": "Scans"
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
      width="320">
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-divider />

      <div id="snapshotnavContent" class="ma-4">
        <search :dense="true" :term="municipalityName"/>

        <div class="nodata pb-8">
          <div class="smaller hint">
            <h4>{{ title }}</h4>
            <p>{{ description }}</p>
          </div>
        </div>

        <snapshot-list
          :snapshots="snapshotsWorkspace"
          :pushRoute="false"
          :listtitle="this.$t('listtitle')"
          @loadSnapshot="loadSnapshot"
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
      bfsNumber: this.$route.params.bfsNumber,
      geojson: null,
      geobounds: [],
      municipalityName: '',
      snapshotsWorkspace: [],
      title: '',
      description: ''
    };
  },

  async mounted() {
    await this.getWorkspace(this.hash);
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
    }
  },

  methods: {
    async getWorkspace(hash) {
      const result = await this.$apollo.query({
        query: gql`query getworkspace($hash: ID!) {
          workspace(id: $hash) {
            id
            pk
            title
            description
            
            snapshotFirst {
              id
              pk
              data
              municipality {
                bfsNumber
                fullname
              }
            }

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
        }`,
        variables: {
          hash: btoa(`WorkspaceNode:${hash}`)
        }
      });
      if (result.data.hasOwnProperty('workspace') && result.data.workspace) {
        const workspaceData = result.data.workspace;
        this.geojson = workspaceData.snapshotFirst.data;
        this.municipalityName = workspaceData.snapshotFirst.municipality.fullname;
        this.snapshotsWorkspace = workspaceData.snapshots;
        this.title = workspaceData.title;
        this.description = workspaceData.description;
        this.$store.commit('setBfsnumber', workspaceData.snapshotFirst.municipality.bfsNumber);
        this.$store.commit('setBfsname', workspaceData.snapshotFirst.municipality.fullname);
      } else {
        this.$router.push({ name: 'home' });
      }
    },

    async loadSnapshot(hash) {
      const result = await this.$apollo.query({
        query: gql`query getsnapshot($hash: ID!) {
          snapshot(id: $hash) {
            id
            pk
            data
            municipality {
              bfsNumber
              fullname
            }
          }
        }`,
        variables: {
          hash: btoa(`SnapshotNode:${hash}`)
        }
      });
      if (result.data.hasOwnProperty('snapshot') && result.data.snapshot) {
        this.geojson = result.data.snapshot.data;
        this.municipalityName = result.data.snapshot.municipality.fullname;
        this.$store.commit('setBfsnumber', result.data.snapshot.municipality.bfsNumber);
        this.$store.commit('setBfsname', result.data.snapshot.municipality.fullname);
        if (this.geojson) {
          await this.$refs.map.destroyMap();
          this.$refs.map.setupMeta();
          this.$refs.map.setupMapbox();
          this.$refs.map.displayMapbox();
        }
      } else {
        this.$router.push({ name: 'home' });
      }
    }
  }
};
</script>
