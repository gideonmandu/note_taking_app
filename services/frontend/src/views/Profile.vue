<template>
  <section>
    <h1>Your Profile</h1>
    <hr />
    <br />
    <div class="">
      <p><strong>Full Name:</strong>{{ user.full_name }}</p>
      <p><strong>Username:</strong>{{ use.username }}</p>
      <p><button class="btn btn-primary" @click="deleteAccount()"></button></p>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Profile",
  created: function () {
    return this.$store.dispatch("viewMe");
  },
  computed: {
    ...mapGetters({ user: "stateUser" }),
  },
  methods: {
    ...mapActions(["deleteUser"]),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch("logOut");
        this.$router.push("/");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
