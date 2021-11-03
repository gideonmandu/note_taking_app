<template>
  <section>
    <h1>Edit note</h1>
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
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "EditNote",
  props: ["id"],
  data() {
    return {
      form: {
        title: "",
        content: "",
      },
    };
  },
  created: function () {
    this.GetNote();
  },
  computed: {
    ...mapGetters({ note: "stateNote" }),
  },
  methods: {
    ...mapActions(["updateNote", "viewNote"]),
    async submit() {
      try {
        let note = {
          id: this.id,
          form: this.form,
        };
        await this.updateNote(note);
        this.$router.push({ name: "Note", params: { id: this.note.id } });
      } catch (error) {
        console.log(error);
      }
    },
    async GetNote() {
      try {
        await this.viewNote(this.id);
        this.form.title = this.note.title;
        this.form.content = this.note.content;
      } catch (error) {
        console.error(error);
        this.$router.push("/dashboard");
      }
    },
  },
};
</script>
