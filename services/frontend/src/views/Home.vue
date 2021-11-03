<template>
  <section>
    <p>This site is built on FastAPI and Vue3.</p>
    <div v-if="isLoggedIn" class="" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Login</a></span>
    </p>
  </section>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>
