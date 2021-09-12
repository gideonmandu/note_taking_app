import axios from "axios";

export default {
  state: {
    notes: null,
    note: null,
  },
  getters: {
    stateNotes: (state) => state.notes,
    stateNote: (state) => state.note,
  },
  actions: {
    async createNote({ dispatch }, note) {
      await axios.post("note", note);
      await dispatch("getNotes");
    },
    async getNotes({ commit }) {
      let { data } = await axios.get("notes");
      commit("setNotes", data);
    },
    async viewNote({ commit }, id) {
      let { data } = await axios.get(`note/${id}`);
      commit("setNote", data);
    },
    // eslint-disabled-next-line no-empty-pattern
    async updateNote({}, note) {
      await axios.patch(`note/${note.id}`, note.form);
    },
    // eslint-disabled-next-line no-empty-pattern
    async deleteNote({}, id) {
      await axios.delete(`note/${id}`);
    },
  },
  mutations: {
    setNotes(state, notes) {
      state.notes = notes;
    },
    setNote(state, note) {
      state.note = note;
    },
  },
};
