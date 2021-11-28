<template>
  <div class="some-products pt-5">
    <div class="container my-3">
      <h1 class="text-center">{{ title }}</h1>

      <div class="row my-4">
        <ProductBox
          v-for="product in products"
          :key="product.id"
          :product="product"
        />
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
import axios from "axios";

import ProductBox from "@/components/ProductBox";

export default {
  name: "some-products",
  data() {
    return {
      products: [],
    };
  },
  components: { ProductBox },
  props: {
    title: String,
    path: String,
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    async getProducts() {
      axios
        .get(this.path)
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            this.error.push("Something went wrong. Please try later!");
            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>