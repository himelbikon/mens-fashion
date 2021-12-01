import { createStore } from "vuex";

export default createStore({
  state: {
    token: "",
    cart: [],
    isAuthenticated: false,
    url: "https://himelbikon.pythonanywhere.com/",
    // url: "http://127.0.0.1:8000",
    sitename: " | Mens Fashion",
    categories: [],
  },
  mutations: {
    initStore(state) {
      if (localStorage.getItem("cart")) {
        state.cart = JSON.parse(localStorage.getItem("cart"));
      }
      if (localStorage.getItem("token")) {
        state.token = JSON.parse(localStorage.getItem("token"));
        state.isAuthenticated = true;
      }
    },
    setLogin(state, token) {
      state.isAuthenticated = true;
      state.token = token;

      localStorage.setItem("token", JSON.stringify(token));
    },
    setLogout(state) {
      state.isAuthenticated = false;
      state.token = "";

      localStorage.removeItem("token");
    },
    addToCart(state, obj) {
      const exists = state.cart.filter((i) => {
        return i.product.id === obj.product.id;
      });

      if (!exists.length) {
        state.cart.push(obj);
      } else {
        for (let i = 0; i < state.cart.length; i++) {
          if (state.cart[i].product.id === obj.product.id) {
            state.cart[i].quantity += obj.quantity;
          }
        }
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    deleteFromCart(state, id) {
      for (let i = 0; i < state.cart.length; i++) {
        if (state.cart[i].product.id === id) {
          state.cart.splice(i, 1);
        }
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    increaseCart(state, id) {
      for (let i = 0; i < state.cart.length; i++) {
        if (state.cart[i].product.id === id) {
          state.cart[i].quantity += 1;
        }
      }
      // save to localStorage
      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    decreaseCart(state, id) {
      for (let i = 0; i < state.cart.length; i++) {
        if (state.cart[i].product.id === id) {
          if (state.cart[i].quantity > 1) {
            state.cart[i].quantity -= 1;
          } else {
            state.cart.splice(i, 1);
          }
        }
      }
      // save to localStorage
      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
  },
  actions: {},
  modules: {},
});
