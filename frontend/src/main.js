import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
// import axios from "axios";
import "./bootstrap.min.css";
import "bootstrap";

// if (localStorage.getItem("token")) {
//   axios.defaults.headers.common = {
//     Authorization: "Bearer " + JSON.parse(localStorage.getItem("token")),
//   };
// }

createApp(App).use(router).use(store).mount("#app");
