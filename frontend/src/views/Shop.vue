<template>
  <div class="shop">
    <div class="container my-3">
      <div class="row">
        <div class="col-12 col-lg-9">
          <!-- <h3 class="text-center">All Products</h3> -->

          <div class="row">
            <div
              class="col-12 col-md-6 col-lg-4 my-4"
              v-for="product in products"
              :key="product.id"
            >
              <ProductBox :product="product" />
            </div>
          </div>

          <button class="btn btn-outline-primary" @click="getProducts()">
            Load More
          </button>
        </div>

        <div class="col-12 col-lg-3 my-4">
          <div class="list-group">
            <h5 class="p-2 text-center fw-bold bg-primary rounded text-white">
              Order By
            </h5>

            <router-link
              :to="{ name: 'shop', query: { to: 'latest' } }"
              class="list-group-item list-group-item-action active"
              >Latest Product
            </router-link>
            <router-link
              :to="{ name: 'shop', query: { to: 'popular' } }"
              class="list-group-item list-group-item-action"
              >Popular Product
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import ProductBox from "@/components/ProductBox";

export default {
  name: "shop",
  data() {
    return {
      products: [],
      page: 1,
    };
  },
  mounted() {
    document.title = "Shop" + this.$store.state.sitename;

    this.getProducts();
  },
  components: { ProductBox },
  methods: {
    getProducts() {
      axios
        .get(`/api/shop/latest/9/${this.page}/`)
        .then((response) => {
          response.data.map((i) => {
            this.products.push(i);
          });

          // this.products = response.data;
          this.page += 1;
        })
        .catch((error) => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data));
          } else {
            console.log(error);
          }
        });
    },
  },
};
</script>