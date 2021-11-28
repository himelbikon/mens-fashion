import { createWebHistory, createRouter } from "vue-router";
import store from "./store";

import Home from "@/views/Home";
import About from "@/views/About";
import Login from "@/views/Login";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/about",
    name: "about",
    component: About,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  // {
  //   path: "/checkout",
  //   name: "checkout",
  //   component: Checkout,
  //   meta: {
  //     requireLogin: true,
  //   },
  // },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.token
  ) {
    next({ name: "login", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
