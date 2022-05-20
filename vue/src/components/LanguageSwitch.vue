<template>
<div v-if="expanded">
    <v-btn
      v-for="lang in $i18n.availableLocales"
      :key="lang"
      text plain
      elevation="0"
      class="mx-1 px-0 main"
      @click="changeLanguage(lang)">{{ lang }}</v-btn>
</div>
<div v-else>
  <v-speed-dial
    id="langnav"
    open-on-hover
    direction="left"
    transition="slide-x-reverse-transition">
    <template v-slot:activator>
      <v-btn
        id="langnav"
        small
        elevation="0"
        fab>{{ $i18n.locale }}
      </v-btn>
    </template>
    <v-btn
      v-for="lang in $i18n.availableLocales.filter(language => language !== $i18n.locale)"
      :key="lang"
      fab
      small
      color="primary"
      elevation="0"
      class="mx-1 px-0"
      @click="changeLanguage(lang)">{{ lang }}</v-btn>
  </v-speed-dial>
</div>
</template>

<style scoped>
.main {
  font-weight: bold;
}
</style>

<script>
export default {
  name: 'LanguageSwitch',
  props: ['expanded'],
  methods: {
    changeLanguage(lang) {
      this.$i18n.locale = lang;
      const newParams = this.$route.params;
      newParams.lang = lang;
      this.$router.push({
        name: this.$route.name,
        params: newParams
      });
    }
  }
};
</script>
