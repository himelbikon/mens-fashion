<template>
  <div class="home">
    <section><Carousel /></section>
    <section><SomeProducts title="Latest Products" /></section>
    <section><CategoryBox /></section>
    <section><SomeProducts title="Popular Products" /></section>
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
};
</script>