import Vue from 'vue';
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import VueApollo from 'vue-apollo';
import vuetify from './plugins/vuetify';
import router from './router';
import store from './store';
import i18n from './trans';
import LanguageSwitch from './components/LanguageSwitch.vue';
import UserActions from './components/UserActions.vue';
import App from './App.vue';

require('@/assets/styles/main.css');

Vue.config.productionTip = false;

const apiLink = new HttpLink({
  uri: process.env.VUE_APP_GRAPHQL_URI
});

const apolloClient = new ApolloClient({
  link: apiLink,
  cache: new InMemoryCache()
  // connectToDevTools: true
});

Vue.use(VueApollo);

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

Vue.component('language-switch', LanguageSwitch);
Vue.component('user-actions', UserActions);

new Vue({
  router,
  store,
  i18n,
  vuetify,
  apolloProvider,
  render: h => h(App)
}).$mount('#app');
