<template>
  <div class="home">
    <section><Carousel /></section>
    <section>
      <SomeProducts title="Latest Products" path="/api/shop/latest/8/" />
    </section>
    <section><CategoryBox /></section>
    <section>
      <SomeProducts title="Popular Products" path="/api/shop/popular/8/" />
    </section>
    <section><ProductOffer /></section>
    <section><Feature /></section>
    <section><Subscribe /></section>
  </div>
</template>

<script>
import Carousel from "@/components/Carousel";
import SomeProducts from "@/components/SomeProducts";
import CategoryBox from "@/components/CategoryBox";
import ProductOffer from "@/components/ProductOffer";
import Feature from "@/components/Feature";
import Subscribe from "@/components/Subscribe";

export default {
  name: "home",
  components: {
    Carousel,
    SomeProducts,
    CategoryBox,
    ProductOffer,
    Feature,
    Subscribe,
  },
  mounted() {
    document.title = "Mens Fashion";
  },
};
</script>