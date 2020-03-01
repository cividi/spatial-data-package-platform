<template>
  <v-app>
    <component :is="$route.meta.layout">
      <router-view/>
    </component>
    <!--<v-footer app>
    </v-footer>-->
  </v-app>
</template>

<style>
#app {
  background: #fff;
}
#topbar {
  border-bottom: 1px solid #e4e4e4;
}
.useractions .v-btn {
  text-transform: initial;
}
</style>

<script>
export default {
  data() {
    return {
      layout: 'div'
    };
  }
};
</script>
