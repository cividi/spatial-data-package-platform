import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    notIframe: window.self === window.top,
    bfsnumber: '',
    bfsname: '',
    snapshotnav: false,
    isUserLoggedIn: false,
    workspacesInfo: {},
    mapCenter: null,
    mapZoomLevel: null,
    rated: []
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
    },

    setIsLoggedIn(state) {
      state.isUserLoggedIn = true;
    },

    setIsLoggedOut(state) {
      state.isUserLoggedIn = false;
    },

    setMapZoomLevel(state, value) {
      state.mapZoomLevel = value;
    },

    setMapCenter(state, value) {
      state.mapCenter = value;
    },

    addRated(state, value) {
      state.rated = [...state.rated, value];
    }
  },
  getters: {
    WorkspaceInfoByHash: state => (hash) => {
      if (state.workspacesInfo.hasOwnProperty(hash)) {
        return state.workspacesInfo[hash];
      }
      return false;
    },

    IsRated: state => commentPk => state.rated.includes(commentPk)
  },
  actions: {
  },
  modules: {
  }
});
