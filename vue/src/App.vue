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

  computed: {
    selectedLayout() {
      if (this.$route && this.$route.hasOwnProperty('meta') && this.$route.meta.hasOwnProperty('layout')) {
        return this.$route.meta.layout;
      }
      return LayoutDefault;
    }
  }
};
</script>
