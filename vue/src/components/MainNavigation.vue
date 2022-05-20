<!-- eslint-disable -->
<i18n>
{
  "de": {
    "mainnav.home": "Projekt",
    "mainnav.map": "Karte",
    "mainnav.gallery": "Galerie",
    "mainnav.add": "Eintragen"
  },
  "fr": {
    "mainnav.home": "Projekt",
    "mainnav.map": "Karte",
    "mainnav.gallery": "Galerie",
    "mainnav.add": "Eintragen"
  },
  "en": {
    "mainnav.home": "Project",
    "mainnav.map": "Map",
    "mainnav.gallery": "Galery",
    "mainnav.add": "Add an entry"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <v-app-bar app flat fixed id="topbar">
      <v-row no-gutters>
        <v-col cols="4" sm="4">
          <v-app-bar-nav-icon @click="mobnav=!mobnav" class="d-md-none"></v-app-bar-nav-icon>
        </v-col>
        <v-col cols="12" sm="4" class="text-center">
          <language-switch expanded="1" />
        </v-col>
        <!-- <div class="d-none d-md-block"><language-switch/></div>
        <div class="useractions d-none d-sm-block">
          <user-actions />
        </div>-->
        <v-col cols="4" sm="4" class="text-right">
          <nav id="mainnav" class="d-none d-md-block">
            <router-link
              v-for="item in mainnav"
              :key="item.textKey"
              :to="'/' + $i18n.locale + item.route + '/'">{{ $t(item.textKey) }}</router-link>
          </nav>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-navigation-drawer
      left app dark color="primary" class="mobnav" v-model="mobnav" disable-resize-watcher>
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
          :to="'/' + $i18n.locale + item.route + '/'">
          <v-list-item-content>
            <v-list-item-title>{{ $t(item.textKey) }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-flex class="useractions d-sm-none center">
        <v-divider></v-divider>
      </v-flex>
    </v-navigation-drawer>
  </div>
</template>

<style>
#mainnav a {
  margin: 0 0.5em;
  font-size: 1.6em;
  font-weight: bold;
  text-transform: uppercase;
}

#topbar {
  background-color: transparent;
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
        { route: '/', textKey: 'mainnav.home' },
        { route: '/map', textKey: 'mainnav.map' },
        { route: '/gallery', textKey: 'mainnav.gallery' },
        { route: '/add', textKey: 'mainnav.add' }
      ]
    };
  }
};
</script>
