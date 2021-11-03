<template>
  <section>
    <form @submit.prevent="submit">
      <div class="mb-3">
        <lable for="username" class="form-lable">Username:</lable>
        <input
          type="text"
          name="username"
          class="form-control"
          v-model="form.username"
        />
      </div>
      <div class="mb-3">
        <lable for="password" class="form-lable">Password:</lable>
        <input
          type="text"
          name="password"
          class="form-control"
          v-model="form.password"
        />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    ...mapActions(["logIn"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      await this.logIn(User);
      this.$router.push("/dashboard");
    },
  },
};
</script>
