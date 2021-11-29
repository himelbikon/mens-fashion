<template>
  <div class="shop">
    <div class="container my-3">
      <div class="row">
        <div class="col-12 col-lg-9">
          <!-- <h3 class="text-center">All Products</h3> -->

          <div class="row">
            <div
              class="col-12 col-md-6 col-lg-4 my-3"
              v-for="product in products"
              :key="product.id"
            >
              <ProductBox :product="product" />
            </div>
          </div>

          <div class="text-center">
            <button class="btn btn-outline-primary" @click="getProducts()">
              Load More
            </button>
          </div>
        </div>

        <div class="col-12 col-lg-3 my-4">
          <div class="list-group mb-3">
            <h5 class="p-2 text-center fw-bold bg-primary rounded text-white">
              Order By
            </h5>

            <router-link
              :to="{ name: 'shop' }"
              class="list-group-item list-group-item-action active"
              >Latest Products
            </router-link>
            <router-link
              :to="{ name: 'shop', query: { orderby: 'views' } }"
              class="list-group-item list-group-item-action"
              >Most Viewed Products
            </router-link>
          </div>

          <div class="list-group mb-3">
            <h5 class="p-2 text-center fw-bold bg-primary rounded text-white">
              Category
            </h5>

            <router-link
              :to="{ name: 'shop', query: { category: category.slug } }"
              class="list-group-item list-group-item-action"
              v-for="category in this.$store.state.categories"
              :key="category.id"
            >
              {{ category.name }}
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
      orderby: "",
      category: "",
    };
  },
  mounted() {
    document.title = "Shop" + this.$store.state.sitename;
    this.urlQuery();

    this.getProducts();
  },
  components: { ProductBox },
  methods: {
    async getProducts() {
      await axios
        .get(
          `/api/shop/products?orderby=${this.orderby}&page=${this.page}&category=${this.category}`
        )
        .then((response) => {
          response.data.map((i) => {
            this.products.push(i);
          });

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
    urlQuery() {
      this.orderby = "";
      this.category = "";
      if (this.$route.query.orderby) {
        this.orderby = this.$route.query.orderby;
      } else if (this.$route.query.category) {
        this.category = this.$route.query.category;
      }
    },
  },
  watch: {
    $route(to, from) {
      if (to != from) {
        this.products = [];
        this.page = 1;
        this.urlQuery();
        this.getProducts();
      }
    },
  },
};
</script>