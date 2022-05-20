<!-- eslint-disable -->
<i18n>
{
  "de": {
    "img.1.alt":
      "dføur",
    "h2.2": "Beispiele",
    "networkerror": "Die Projekterfassung ist zur Zeit nicht verfügbar."
  },
  "fr": {
    "img.1.alt":
      "Le dføur",
    "h2.2": "Examples",
   "networkerror": "La recherche n'est pas disponible actuellement."
  },
  "en": {
    "img.1.alt":
      "dføur",
    "h2.2": "Examples",
    "networkerror": "The data is currently not available, please try again soon."
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<div>
  <v-container my-12 class="text-center" >
      <h3>Under construction...</h3>
  </v-container>

  <v-snackbar color="primary" v-model="snackbar" :timeout="9000">
    {{ $t('networkerror') }}
    <v-btn icon @click="snackbar=false" >
      <v-icon>mdi-close-circle-outline</v-icon>
    </v-btn>
  </v-snackbar>
</div>

</template>

<style>
.gmdscn {
  position: relative;
  max-width: 720px;
  margin: 0 auto;
}

.gmdscn .gemeindesuche.v-select {
  position: absolute;
  top: calc(50% - 30px);
  left: 50%;
  transform: translateX(-50%);
}

.introtxt {
  max-width: 660px;
}

.quotetxt {
  font-style: italic;
}
</style>

<script>
import gql from 'graphql-tag';

export default {
  name: 'Home',

  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      snapshotsExamples: [],
      networkError: false,
      snackbar: false,
      searchEnabled: true,
      exampleGalleryEnabled: true,
      homepageSnippet: ''
    };
  },

  created() {
    this.$store.commit('setBfsnumber', '');
    this.$store.commit('setBfsname', '');
  },

  async mounted() {
    const sessionid = this.$cookies.get('sessionid', '');
    if (sessionid) {
      this.$store.commit('setIsLoggedIn');
      const workspaceid = this.$cookies.get('workspaceid', '');
      if (workspaceid) {
        const hashed = workspaceid.replace(/^"|"$/g, '').split('/');
        const wshash = hashed[0];
        const hash = hashed[1];
        this.$router.push({ name: 'workspaceRedirect', params: { wshash, hash } });
      }
    } else {
      this.$store.commit('setIsLoggedOut');
    }
    await this.getConfig();
    await this.getSnapshotsExamples();
  },

  methods: {
    async getConfig() {
      const language = this.$i18n.locale;
      const configResult = await this.$apollo.query({
        query: gql`query getconfig($language: String) {
          config(language: $language) {
            searchEnabled,
            exampleGalleryEnabled,
            homepageSnippet
          }
        }`,
        variables: {
          language
        },
        fetchPolicy: 'no-cache' // fixes empty homepage, apollo bug?
      }).catch(() => {
        this.snackbar = true;
        this.networkError = true;
      });
      if (configResult) {
        const config = configResult.data.config;
        if (config) {
          this.searchEnabled = config.searchEnabled;
          this.exampleGalleryEnabled = config.exampleGalleryEnabled;
          this.homepageSnippet = config.homepageSnippet;
        }
      }
    },

    async getSnapshotsExamples() {
      const result = await this.$apollo.query({
        query: gql`{
          snapshots(isShowcase: true) {
            edges {
              node {
                id
                pk
                title
                topic
                thumbnail
                municipality {
                  name
                }
              }
            }
          }
        }`
      }).catch(() => {
        this.snackbar = true;
        this.networkError = true;
      });
      if (result) {
        const snapshots = result.data.snapshots.edges.map(snapshot => snapshot.node);
        // fake random, for more randomness, use https://www.npmjs.com/package/lodash.shuffle package
        this.snapshotsExamples = snapshots.sort(() => (Math.random() > 0.5 ? -1 : 1)).slice(0, 3);
        this.snackbar = false;
        this.networkError = false;
      }
    }
  }
};
</script>
