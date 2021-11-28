<template>
  <div class="some-products pt-5">
    <div class="container my-3">
      <h1 class="text-center">{{ title }}</h1>

      <div class="row my-4">
        <ProductBox />
        <ProductBox />
        <ProductBox />
        <ProductBox />
        <ProductBox />
        <ProductBox />
        <ProductBox />
        <ProductBox />
      </div>

      <div class="text-center mb-5">
        <router-link
          :to="{ name: 'home' }"
          type="button"
          class="btn btn-outline-primary"
        >
          View All Products
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import ProductBox from "@/components/ProductBox";

export default {
  name: "some-products",
  components: { ProductBox },
  props: {
    title: String,
  },
};
</script>