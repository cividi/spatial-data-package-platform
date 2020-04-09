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
#topbar {
  border-bottom: 1px solid #e4e4e4;
}
</style>

<script>
import LayoutDefault from '@/layouts/LayoutDefault.vue';

export default {
  data() {
    return {};
  },

  mounted() {
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

  methods: {
    setInitialSnapshotnav() {
      if (this.$route.params.hash) {
        if (['lg', 'xl'].includes(this.$vuetify.breakpoint.name)) {
          this.$store.commit('setSnapshotnav', false);
        } else {
          this.$store.commit('setSnapshotnav', true);
        }
      } else {
        this.$store.commit('setSnapshotnav', false);
      }
    }
  }
};
</script>
