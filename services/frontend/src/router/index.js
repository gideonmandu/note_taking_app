import { createRouter, createWebHistory } from "vue-router";

import store from "../store";
import Home from "../views/Home.vue";
import Register from "../views/Register";
import Login from "../views/Login";
import Dashboard from "../views/Dashboard";
import Profile from "../views/Profile";
import Note from "../views/Note";
import EditNote from "../views/EditNote";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "profile",
    component: Profile,
    meta: { requiresAuth: true },
  },
  {
    path: "/note/:id",
    name: "Note",
    component: Note,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: "/note/:id",
    name: "EditNote",
    component: EditNote,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
