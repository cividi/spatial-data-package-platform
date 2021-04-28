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
    },

    setIsLoggedIn(state) {
      state.isUserLoggedIn = true;
    },

    setIsLoggedOut(state) {
      state.isUserLoggedIn = false;
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
    snapshotStore: {
      namespaced: true,
      state: {
        perimeter: null,
        items: [],
        comment: '',
        loading: false,
        error: null,
        submitted: false
      },
      mutations: {
        UPDATE_COMMENT(state, comment) {
          state.comment = comment;
        },
        UPDATE_PERIMETER(state, perimeter) {
          state.perimeter = perimeter;
        },
        TOGGLE_ITEM(state, item) {
          state.items = state.items.includes(item)
            ? state.items.filter(i => i !== item) : [...state.items, item];
        },
        RESET_CART(state) {
          state.perimeter = null;
          state.items = [];
          state.comment = '';
        },
        SET_LOADING(state, loadingSate) {
          state.loading = loadingSate;
        },
        SET_SUBMITTED(state, submittedSate) {
          state.submitted = submittedSate;
        },
        SET_ERROR(state, error) {
          state.loading = error;
        }
      },
      getters: {
        getItems(state) {
          return state.items;
        },
        getPerimeter(state) {
          return state.perimeter;
        },
        getComment(state) {
          return state.comment;
        },
        getStatus(state) {
          return { loading: state.loading, error: state.error, submitted: state.submitted };
        },
        getCart(state) {
          return {
            packages: state.items,
            perimeter: state.perimeter.bfsNumber,
            comment: state.comment,
            user: 'Test'
          };
        }
      },
      actions: {
        toggleItem({ commit }, item) {
          commit('TOGGLE_ITEM', item);
        },
        setPerimeter({ commit }, perimter) {
          commit('UPDATE_PERIMETER', perimter);
        },
        updateComment({ commit }, data) {
          commit('UPDATE_COMMENT', data);
        },
        resetCart({ commit }) {
          commit('RESET_CART');
        }
      }
    }
  }
});
