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
    "mainnav.home": "Projet",
    "mainnav.map": "Carte",
    "mainnav.gallery": "Galerie",
    "mainnav.add": "Soumettre un objet"
  },
  "en": {
    "mainnav.home": "Project",
    "mainnav.map": "Map",
    "mainnav.gallery": "Gallery",
    "mainnav.add": "Submit"
  },
  "it": {
    "mainnav.home": "Progetto",
    "mainnav.map": "Mappa",
    "mainnav.gallery": "Galleria",
    "mainnav.add": "Inserisci"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <div>
    <v-app-bar app prominent flat id="topbar" absolute>
      <v-row no-gutters>
        <v-col cols="7" class="text-left">
          <nav class="d-none d-sm-block">
            <language-switch
              expanded="1" v-if="$route.name == 'home'"
              style="pointer-events: all;" />
          </nav>
        </v-col>
        <!-- <div class="d-none d-md-block"><language-switch/></div>
        <div class="useractions d-none d-sm-block">
          <user-actions />
        </div>-->
        <v-col cols="5" class="text-right">
          <v-app-bar-nav-icon
            @click="mobnav=!mobnav" class="d-sm-none"
            style="pointer-events: all;">
          </v-app-bar-nav-icon>
          <nav id="mainnav" class="d-none d-sm-block">
            <router-link
              v-for="item in mainnav"
              :key="item.textKey"
              :to="'/' + $i18n.locale + item.route + '/'">{{ $t(item.textKey) }}</router-link>
          </nav>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-navigation-drawer
      left app dark color="primary"
      class="mobnav" v-model="mobnav"
      disable-resize-watcher width="320px">
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
#mainnav {
  margin-top: 3.5em;
}
#mainnav a {
  pointer-events: all;
  display: block;
  width: fit-content;
  margin: auto 0 12px auto;
  font-family: 'Helvetica Neue LT W05 75 Bold', 'Arial', sans-serif;
  font-size: 2.2em;
  font-weight: bold;
  letter-spacing: 0.06em; /* 60% / 1000 + em */
  line-height: 1em;
  text-transform: uppercase;
  border-bottom: 8px solid #000;
}

#topbar {
  background-color: transparent;
  font-size: 1em !important;
  pointer-events: none;
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
        { route: '/map', textKey: 'mainnav.map' },
        { route: '/gallery', textKey: 'mainnav.gallery' },
        { route: '/add', textKey: 'mainnav.add' },
        { route: '/', textKey: 'mainnav.home' }
      ]
    };
  }
};
</script>
