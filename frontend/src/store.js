import { createStore } from "vuex";

export default createStore({
  state: {
    token: "",
    cart: [],
    url: "https://himelbikon.pythonanywhere.com/",
    // url: "http://127.0.0.1:8000",
    sitename: " | Mens Fashion",
    categories: [],
  },
  mutations: {},
  actions: {},
  modules: {},
});
