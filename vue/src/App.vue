<template>
  <v-app>

    <v-app-bar app flat id="topbar">
      <router-link id="logo" to="/">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>
      <v-spacer></v-spacer>
      <nav id="mainnav" class="d-none d-md-block">
        <router-link
          v-for="item in mainnav"
          :key="item.text"
          :to="item.route">{{item.text}}</router-link>
      </nav>
      <v-spacer></v-spacer>
      <div class="useractions d-none d-sm-block">
        <v-btn small text color="primary">
          <router-link to="/login">Login</router-link>
        </v-btn>
        <v-btn small outlined color="primary">
          <router-link key="signup" to="/signup">Kostenlos Account erstellen</router-link>
        </v-btn>
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
      <v-flex class="useractions d-sm-none center">
        <v-divider></v-divider>
        <v-btn small text color="white" class="mt-4">
          <router-link to="/login">Login</router-link>
        </v-btn>
        <v-btn small outlined color="white" class="mt-4">
          <router-link key="signup" to="/signup">Kostenlos Account erstellen</router-link>
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
