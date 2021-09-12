import createPersistedState from "vuex-persistedstate";
import { createStore } from "vuex";
import notes from "./modules/notes";
import users from "./modules/users";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    notes,
    users,
  },
  plugins: [createPersistedState],
});
