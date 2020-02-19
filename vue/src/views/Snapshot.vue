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
  <v-container my-12>
  <v-layout >
    <v-flex>
      <h1>Snapshot</h1>
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
