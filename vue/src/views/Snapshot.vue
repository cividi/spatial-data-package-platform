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
  <v-container>
    <v-navigation-drawer
      :width="320"
      left app >
      <router-link id="logo" :to="'/' + $i18n.locale + '/'" class="px-4 py-1 d-block">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>

      <v-toolbar
      :width="320"
      absolute
      bottom
        class="useractions center">
        <user-actions />
      </v-toolbar>
    </v-navigation-drawer>

    <v-layout >
      <v-flex>
        <h1>Map</h1>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<style>
</style>

<script>
import gql from 'graphql-tag';

export default {
  data() {
    return {
    };
  },

  methods: {
    async getSnapshot(hash) {
      const result = await this.$apollo.query({
        query: gql`query getsnapshot($hash: ID!){
          snapshot(id: $hash) {
            id
            pk
            data
          }
        }`,
        variables: {
          hash: btoa(`SnapshotNode:${hash}`)
        }
      });
      return result;
    }
  },

  async created() {
    const hash = this.$route.params.hash;
    const result = await this.getSnapshot(hash);
    console.log(result);
  }
};
</script>
