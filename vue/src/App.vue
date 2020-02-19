<!-- eslint-disable -->
<i18n>
{
  "de": {
    "loginText": "Login",
    "signupText": "Unverbindliche Anfrage",
    "mainnav.about": "Hintergrund",
    "mainnav.imprint": "Impressum",
    "mainnav.contact": "Kontakt"
},
  "fr": {
    "loginText": "Login",
    "signupText": "Demande sans engagement",
    "mainnav.about": "Contexte",
    "mainnav.imprint": "Impressum",
    "mainnav.contact": "Contact"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-app>
    <v-app-bar app flat id="topbar">
      <router-link id="logo" :to="'/' + $i18n.locale + '/'">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>
      <v-spacer></v-spacer>
      <nav id="mainnav" class="d-none d-md-block">
        <router-link
          v-for="item in mainnav"
          :key="item.textKey"
          :to="'/' + $i18n.locale + item.route">{{ $t(item.textKey) }}</router-link>
      </nav>
      <v-spacer></v-spacer>
      <div class="d-none d-md-block"><language-switch/></div>
      <div class="useractions d-none d-sm-block">
        <v-btn small text color="primary">
          <router-link :to="'/' + $i18n.locale + '/login'">{{ $t('loginText') }}</router-link>
        </v-btn>
        <v-btn small outlined color="primary">
          <router-link key="signup" :to="'/' + $i18n.locale + '/signup'">
            {{ $t('signupText') }}
          </router-link>
        </v-btn>
      </div>
      <v-app-bar-nav-icon @click="mobnav=!mobnav" class="d-md-none"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer
      right app dark color="primary" class="mobnav" v-model="mobnav" disable-resize-watcher>
      <v-toolbar flat color="primary" class="mx-2">
        <v-spacer></v-spacer>
        <v-btn icon large @click="mobnav=!mobnav">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <div class="text-right mx-2"><language-switch expanded="1" /></div>
      <v-list color="primary">
        <v-list-item
          v-for="item in mainnav" :key="item.textKey"
          :to="'/' + $i18n.locale + item.route">
          <v-list-item-content>
            <v-list-item-title>{{ $t(item.textKey) }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-flex class="useractions d-sm-none center">
        <v-divider></v-divider>
        <v-btn small text color="white" class="mt-4">
          <router-link :to="'/' + $i18n.locale + '/login'">{{ $t('loginText') }}</router-link>
        </v-btn><br>
        <v-btn small outlined color="white" class="mt-4">
          <router-link key="signup" :to="'/' + $i18n.locale + '/signup'">
            {{ $t('signupText') }}
          </router-link>
        </v-btn>
      </v-flex>
    </v-navigation-drawer>

    <v-content>
      <router-view/>
    </v-content>
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

#mainnav a {
  color: #000;
  margin: 0 0.5em;
}

.v-application .mobnav a {
  color: #fff;
}
</style>

<script>
export default {
  data() {
    return {
      mobnav: false,
      mainnav: [
        { route: '/about', textKey: 'mainnav.about' },
        { route: '/imprint', textKey: 'mainnav.imprint' },
        { route: '/contact', textKey: 'mainnav.contact' }
      ]
    };
  }
};
</script>
