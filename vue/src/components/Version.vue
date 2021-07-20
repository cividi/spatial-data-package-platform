<template>
  <div class="version">
    <a target="_blank" :href="'https://github.com/cividi/spatial-data-package-platform/releases/tag/' + version[0]">v{{version[0]}}</a>
    &nbsp;
    (<a target="_blank" :href="'https://github.com/cividi/spatial-data-package-platform/commit/' + version[1]">{{version[1]}}</a>)
  </div>
</template>

<script>
export default {
  name: 'Version',
  data() {
    return {
      version: process.env.VUE_APP_GIT_VERSION.split('\t')
    };
  }
};
</script>

<style>
  .version {
    height: 35px;
    text-align: center;
  }
</style>
