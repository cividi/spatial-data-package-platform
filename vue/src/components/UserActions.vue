<!-- eslint-disable -->
<i18n>
{
  "de": {
    "loginText": "Login",
    "logoutText": "Logout",
    "signupText": "Unverbindliche Anfrage"
},
  "fr": {
    "loginText": "Login",
    "logoutText": "Logout",
    "signupText": "Demande sans engagement"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<div v-if="vertical">
   <v-btn small text color="white" class="mt-4">
    <router-link v-if="!$store.state.isUserLoggedIn" :to="'/' + $i18n.locale + '/login/'">
      {{ $t('loginText') }}
    </router-link>
    <router-link v-else :to="'/' + $i18n.locale + '/logout/'">
      {{ $t('logoutText') }}
    </router-link>
  </v-btn><br>
  <v-btn small outlined color="white" class="mt-4" v-if="!noRequest">
    <router-link key="signup" :to="'/' + $i18n.locale + '/signup/'">
      {{ $t('signupText') }}
    </router-link>
  </v-btn>
</div>
<div v-else>
  <v-btn small text color="primary">
    <router-link v-if="!$store.state.isUserLoggedIn" :to="'/' + $i18n.locale + '/login/'">
      {{ $t('loginText') }}
    </router-link>
    <router-link v-else :to="'/' + $i18n.locale + '/logout/'">
      {{ $t('logoutText') }}
    </router-link>
  </v-btn>
  <v-btn small outlined color="primary" v-if="!noRequest">
    <router-link key="signup" :to="'/' + $i18n.locale + '/signup/'">
      {{ $t('signupText') }}
    </router-link>
  </v-btn>
</div>
</template>

<style>
.useractions .v-btn {
  text-transform: initial;
}
</style>

<script>
export default {
  name: 'UserActions',
  data() {
    return {
    };
  },
  props: [
    'vertical',
    'noRequest'
  ]
};
</script>
