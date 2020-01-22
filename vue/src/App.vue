<template>
  <v-app>

    <v-app-bar app flat id="topbar">
      <router-link id="logo" to="/">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>
      <v-spacer></v-spacer>
      <nav id="mainnav" class="d-none d-md-block">
        <router-link to="/about">Hintergrund</router-link>
        <router-link to="/imprint">Impressum</router-link>
        <router-link to="/contact">Kontakt</router-link>
      </nav>
      <v-spacer></v-spacer>
      <div class="useractions d-none d-sm-block">
        <v-btn small text color="primary">Login</v-btn>
        <v-btn small outlined color="primary">Kostenlos Account erstellen</v-btn>
      </div>
      <v-app-bar-nav-icon @click="mobnav=!mobnav" class="d-md-none"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer right app dark color="primary" v-model="mobnav" disable-resize-watcher>
      <v-toolbar flat color="primary">
        <v-spacer></v-spacer>
        <v-btn icon large @click="mobnav=!mobnav">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-list color="primary">
        <v-list-item v-for="item in mainnav" :key="item.text" router :to="item.route">
          <v-list-item-content>
            <v-list-item-title>{{item.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-flex class="useractions d-sm-none center" style="border-top: 1px solid #fff3;">
        <v-btn small text color="white">Login</v-btn>
        <v-btn small outlined color="white">Kostenlos Account erstellen</v-btn>
      </v-flex>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid>
        <router-view/>
      </v-container>
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
.v-navigation-drawer .useractions .v-btn {
  margin-top: 1em;
  width: calc(100% - 32px);
}
.mainnav {
}

#mainnav a {
  color: #000;
  margin: 0 0.5em;
}

#mainnav a.router-link-exact-active {
  /* color: #42b983; */
}
</style>
<script>
export default {
  data() {
    return {
      mobnav: false,
      mainnav: [
        { route: 'about', text: 'Hintergrund' },
        { route: 'imprint', text: 'Impressum' },
        { route: 'contact', text: 'Kontakt' }
      ]
    };
  }
};
</script>
