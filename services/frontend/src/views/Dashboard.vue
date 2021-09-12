<template>
  <div>
    <section>
      <h1>Add new note</h1>
      <hr />
      <br />
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-lable">Title:</label>
          <input
            type="text"
            name="title"
            id=""
            class="form-control"
            v-model="form.title"
          />
        </div>
        <div class="mb-3">
          <lable class="form-lable" for="content">Content:</lable>
          <textarea
            name="content"
            id=""
            cols="30"
            rows="10"
            class="form-control"
            v-model="form.content"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
    <br /><br />
    <section>
      <h1>Notes</h1>
      <hr />
      <br />
      <div v-if="notes.length">
        <div class="notes" v-for="note in notes" :key="note.id">
          <div class="card" style="width: 18rem">
            <div class="card-body">
              <ul>
                <li><strong>Note Title:</strong>{{ note.title }}</li>
                <li><strong>Author:</strong>{ note.author.username}</li>
                <li>
                  <router-link :to="{ name: 'Note', params: { id: note.id } }"
                    >view</router-link
                  >
                </li>
              </ul>
            </div>
          </div>
          <br />
        </div>
      </div>
      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Dashboard",
  data() {
    return {
      form: {
        title: "",
        content: "",
      },
    };
  },
  created: function () {
    return this.$store.dispatch("getNotes");
  },
  computed: {
    ...mapGetters({ notes: "stateNotes" }),
  },
  methods: {
    ...mapActions(["createNote"]),
    async submit() {
      await this.createNote(this.form);
    },
  },
};
</script>
