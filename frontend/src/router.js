import { createWebHistory, createRouter } from "vue-router";
import store from "./store";

import Home from "@/views/Home";
import About from "@/views/About";
import Login from "@/views/Login";
import Product from "@/views/Product";
import Shop from "@/views/Shop";
import Cart from "@/views/Cart";
import Checkout from "@/views/Checkout";
// import Test from "@/views/Test";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  // {
  //   path: "/test/",
  //   name: "test",
  //   component: Test,
  // },
  {
    path: "/about/",
    name: "about",
    component: About,
  },
  {
    path: "/login/",
    name: "login",
    component: Login,
  },
  {
    path: "/products/:id/",
    name: "product",
    component: Product,
  },
  {
    path: "/shop",
    name: "shop",
    component: Shop,
  },
  {
    path: "/cart",
    name: "cart",
    component: Cart,
  },
  {
    path: "/checkout",
    name: "checkout",
    component: Checkout,
    meta: {
      requireLogin: true,
    },
  },
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
