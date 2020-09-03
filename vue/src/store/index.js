import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    notIframe: window.self === window.top,
    bfsnumber: '',
    bfsname: '',
    snapshotnav: false,
    workspacesInfo: {}
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
    },

    addWorkspaceInfo(state, hashNvalue) {
      state.workspacesInfo[hashNvalue.hash] = hashNvalue.value;
    }
  },
  getters: {
    WorkspaceInfoByHash: state => (hash) => {
      if (state.workspacesInfo.hasOwnProperty(hash)) {
        return state.workspacesInfo[hash];
      }
      return false;
    }
  },
  actions: {
  },
  modules: {
  }
});
