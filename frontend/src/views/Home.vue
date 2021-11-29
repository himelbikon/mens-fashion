<template>
  <div class="home">
    <section><Carousel /></section>
    <section>
      <SomeProducts title="Latest Products" path="/api/shop/latest/8/1/" />
      <!-- /api/shop/latest/{limit}/{page}/ limit is home many and page is like pagination  -->
    </section>
    <section><CategoryBox /></section>
    <section>
      <SomeProducts title="Popular Products" path="/api/shop/popular/8/1/" />
    </section>
    <section><ProductShowcase /></section>
    <section><Feature /></section>
    <section><Subscribe /></section>
  </div>
</template>

<script>
import Carousel from "@/components/Carousel";
import SomeProducts from "@/components/SomeProducts";
import CategoryBox from "@/components/CategoryBox";
import ProductShowcase from "@/components/ProductShowcase";
import Feature from "@/components/Feature";
import Subscribe from "@/components/Subscribe";

export default {
  name: "home",
  components: {
    Carousel,
    SomeProducts,
    CategoryBox,
    ProductShowcase,
    Feature,
    Subscribe,
  },
  mounted() {
    document.title = "Mens Fashion";
  },
};
</script>