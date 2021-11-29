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
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
   watch: {
    $route(to, from) {
      if (to != from) {
        window.scroll(0, 0);
      }
    },
  },
};
</script>

<style>
main {
  min-height: 80vh;
}
</style>
