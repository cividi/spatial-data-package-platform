import Vue from 'vue';
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import VueApollo from 'vue-apollo';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';


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

new Vue({
  router,
  store,
  vuetify,
  apolloProvider,
  render: h => h(App)
}).$mount('#app');
