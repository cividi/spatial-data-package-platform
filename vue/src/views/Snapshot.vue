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
    async getSnapshot(val) {
      const result = await this.$apollo.query({
        query: gql`query snapshot(slugHash$: String!){
          snapshot(ID: $slugHash) {
            node {
              id
            }
          }
        }`,
        variables: {
          slugHash: val
        }
      });
      return result;
    }
  },

  mounted() {
  }
};
</script>
