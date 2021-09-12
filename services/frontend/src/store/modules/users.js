import axios from "axios";

export default {
  state: {
    user: null,
  },
  getters: {
    isAuthenticated: (state) => !!state.user,
    stateUser: (state) => state.user,
  },
  actions: {
    async register({ dispatch }, form) {
      await axios.post("notes", form);
      let UserForm = new FormData();
      UserForm.append("username", form.username);
      UserForm.append("password", form.password);
      await dispatch("logIn", UserForm);
    },
    async logIn({ dispatch }, user) {
      await axios.post("login", user);
      await dispatch("viewMe");
    },
    async viewMe({ commit }) {
      let { data } = await axios.get("users/whoami");
      commit("setUser", data);
    },
    // eslint-disabled-next-line no-empty-pattern
    async deleteNote({}, id) {
      await axios.delete(`user/${id}`);
    },
    async logOut({ commit }) {
      let user = null;
      commit("logout", user);
    },
  },
  mutations: {
    setUser(state, username) {
      state.user = username;
    },
    logout(state, user) {
      state.user = user;
    },
  },
};
