<template>
  <v-app>
    <component :is="selectedLayout">
      <router-view :key="$route.fullPath"/>
    </component>
  </v-app>
</template>

<style>
#app {
  background: #fff;
}
</style>

<script>
import LayoutDefault from '@/layouts/LayoutDefault.vue';

export default {
  data() {
    return {
      fathomSiteId: process.env.VUE_APP_FATHOM_SITEID,
      fathomUrl: process.env.VUE_APP_FATHOM_URL || 'cdn.usefathom.com'
    };
  },

  created() {
    this.setInitialSnapshotnav();
  },

  computed: {
    selectedLayout() {
      if (this.$route && this.$route.hasOwnProperty('meta') && this.$route.meta.hasOwnProperty('layout')) {
        return this.$route.meta.layout;
      }
      return LayoutDefault;
    }
  },

  mounted() {
    if (this.fathomSiteId !== '') {
      const fathomScript = document.createElement('script');
      fathomScript.setAttribute('src', `https://${this.fathomUrl}/script.js`);
      fathomScript.setAttribute('spa', 'auto');
      fathomScript.setAttribute('data-site', this.fathomSiteId);
      fathomScript.setAttribute('exluded-domains', 'www,www.local,localhost');
      fathomScript.setAttribute('defer', true);
      document.head.appendChild(fathomScript);
    }
  },

  methods: {
    setInitialSnapshotnav() {
      if (this.$route.params.hash) {
        if (['lg', 'xl'].includes(this.$vuetify.breakpoint.name)) {
          this.$store.commit('setSnapshotnav', true);
        } else {
          this.$store.commit('setSnapshotnav', false);
        }
      } else {
        this.$store.commit('setSnapshotnav', true);
      }
    }
  }
};
</script>
