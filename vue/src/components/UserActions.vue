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
<div v-if="vertical">
   <v-btn small text color="white" class="mt-4">
    <router-link :to="'/' + $i18n.locale + '/login/'">{{ $t('loginText') }}</router-link>
  </v-btn><br>
  <v-btn small outlined color="white" class="mt-4" v-if="!noRequest">
    <router-link key="signup" :to="'/' + $i18n.locale + '/signup/'">
      {{ $t('signupText') }}
    </router-link>
  </v-btn>
</div>
<div v-else>
  <v-btn small text color="primary">
    <router-link :to="'/' + $i18n.locale + '/login/'">{{ $t('loginText') }}</router-link>
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
