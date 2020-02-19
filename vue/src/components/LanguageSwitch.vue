<template>
  <div>
    <ul>
      <li
        v-for="lang in languages"
        :key="lang"
        @click="changeLanguage(lang)"
        >{{ lang }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'LanguageSwitch',
  data() {
    return {
      languages: ['de', 'fr']
    };
  },

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
