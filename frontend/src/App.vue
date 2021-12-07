<template>
  <div class="main-app">
    <Header />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";

import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
  mounted() {
    this.$store.commit("initStore");
    this.setCategories();
    if (this.$store.state.token) {
      this.getProfile();
    }
    // this.$router.push({ name: "orders" });
  },
  watch: {
    $route(to, from) {
      if (to != from) {
        window.scroll(0, 0);
      }
    },
  },
  methods: {
    async setCategories() {
      await axios
        .get("/api/shop/categories/")
        .then((response) => {
          this.$store.state.categories = response.data;
        })
        .catch((error) => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data));
          }
        });
    },
    async getProfile() {
      await axios
        .get("/api/users/profile/")
        .then(() => {
          console.log("Logged in user!");
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data);
          }
          this.$store.commit("setLogout");
        });
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Serif:ital@1&display=swap");

* {
  font-family: "Noto Serif", serif;
}

.title {
  /*background: white;*/
  border-radius: 50px;
  padding: 3px 50px;
  background: #5b62f4;
  color: white;
  font-weight: bold;
}

main {
  min-height: 80vh;
}
</style>
