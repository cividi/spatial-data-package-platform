<!-- eslint-disable -->
<i18n>
{
  "de": {
    "loginText": "Login",
    "signupText": "Unverbindliche Anfrage"
  },
  "fr": {
    "loginText": "Login",
    "signupText": "Demande sans engagement"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <v-btn small text color="primary">
      <router-link :to="'/' + $i18n.locale + '/login'">{{ $t('loginText') }}</router-link>
    </v-btn>
    <v-btn small outlined color="primary">
      <router-link key="signup" :to="'/' + $i18n.locale + '/signup'">
        {{ $t('signupText') }}
      </router-link>
    </v-btn>
  </div>
</template>

<style>
</style>
