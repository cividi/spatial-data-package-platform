import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    notIframe: window.self === window.top,
    bfsnumber: '',
    bfsname: '',
    snapshotnav: false
  },
  mutations: {
    setBfsnumber(state, nr) {
      state.bfsnumber = nr;
    },

    setBfsname(state, name) {
      state.bfsname = name;
    },

    setSnapshotnav(state, value) {
      state.snapshotnav = value;
    }
  },
  actions: {
  },
  modules: {
  }
});
