import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    notIframe: window.self === window.top
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
});
