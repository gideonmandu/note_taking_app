import { createApp } from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:5000/"; // Backend

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      (originalRequest._retry = true), store.dispatch("logOut");
      return router.push("/login");
    }
  }
});

createApp(App).use(store).use(router).mount("#app");
