<template>
  <v-app>
    <component :is="$route.meta.layout">
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
export default {
  data() {
    return {};
  }
};
</script>
