<template>
  <div class="home">
    <section><Carousel /></section>
    <section>
      <SomeProducts
        title="Latest Products"
        path="/api/shop/products?limit=8&page=1"
      />
    </section>
    <section><CategoryBox /></section>
    <section>
      <SomeProducts
        title="Most Viewed Products"
        path="/api/shop/products?limit=8&page=1&orderby=views"
      />
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