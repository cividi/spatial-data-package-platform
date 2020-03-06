<!-- eslint-disable -->
<i18n>
{
  "de": {
    "mainnav.about": "Hintergrund",
    "mainnav.imprint": "Impressum",
    "mainnav.contact": "Kontakt"
},
  "fr": {
    "mainnav.about": "Contexte",
    "mainnav.imprint": "Impressum",
    "mainnav.contact": "Contact"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
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
        <user-actions />
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
        <user-actions vertical="1" />
      </v-flex>
    </v-navigation-drawer>
  </div>
</template>

<style>
#mainnav a {
  color: #000;
  margin: 0 0.5em;
  font-size: 1.6em;
}

.v-application .mobnav a {
  color: #fff;
}
</style>

<script>
export default {
  name: 'MainNavigation',
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
