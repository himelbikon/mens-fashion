<template>
  <div class="product">
    <div class="container bg-white py-2">
      <div class="row">
        <div class="col-12 col-lg-6">
          <div class="d-flex justify-content-center">
            <img
              :src="this.$store.state.url + bigImg"
              :alt="this.$store.state.url + bigImg"
              class="img-fluid w-75 rounded"
              v-if="bigImg"
            />
            <img
              src="https://via.placeholder.com/500x500"
              alt=""
              class="img-fluid w-75"
              v-else
            />
          </div>
          <div class="row d-flex justify-content-center">
            <div class="col-2 p-0 my-1 rounded">
              <img
                :src="this.$store.state.url + product.image"
                :alt="this.$store.state.url + product.image"
                class="img-fluid w-75 rounded"
                v-if="product.image"
                @click="setBigImg(product.image)"
              />
            </div>
            <div class="col-2 p-0 my-1 rounded">
              <img
                :src="this.$store.state.url + product.image2"
                :alt="this.$store.state.url + product.image2"
                class="img-fluid w-75 rounded"
                v-if="product.image2"
                @click="setBigImg(product.image2)"
              />
            </div>
            <div class="col-2 p-0 my-1 rounded">
              <img
                :src="this.$store.state.url + product.image3"
                :alt="this.$store.state.url + product.image3"
                class="img-fluid w-75 rounded"
                v-if="product.image3"
                @click="setBigImg(product.image3)"
              />
            </div>
            <div class="col-2 p-0 my-1 rounded">
              <img
                :src="this.$store.state.url + product.image4"
                :alt="this.$store.state.url + product.image4"
                class="img-fluid w-75 rounded"
                v-if="product.image4"
                @click="setBigImg(product.image4)"
              />
            </div>
            <div class="col-2 p-0 my-1 rounded">
              <img
                :src="this.$store.state.url + product.image5"
                :alt="this.$store.state.url + product.image5"
                class="img-fluid w-75 rounded"
                v-if="product.image5"
                @click="setBigImg(product.image5)"
              />
            </div>
          </div>
        </div>
        <!-- column divider -->
        <div class="col-12 col-lg-6">
          <div>
            <h4 class="fw-bold mb-3">{{ product.name }}</h4>
            <div>Price: {{ product.price }}</div>
            <div>Category: {{ product.category_name }}</div>
            <div>Viewed: {{ product.views }}</div>
            <p class="my-2" v-if="product.details">
              {{ product.details.substring(0, 200).concat("...") }}
            </p>
          </div>
          <hr />

          <div class="input-group mb-3 w-75">
            <input
              type="number"
              min="1"
              class="form-control mx-3"
              aria-describedby="button-addon2"
              v-model="quantity"
            />
            <button
              class="btn btn-primary rounded-1"
              type="button"
              id="button-addon2"
              @click="addToCart()"
            >
              Add To Cart {{ quantityInCart }}
            </button>
          </div>

          <div class="py-2 w-75" v-if="quantityInCart">
            <button
              type="button"
              class="btn btn-primary btn-sm me-2"
              @click="decreaseCart()"
            >
              -
            </button>
            {{ quantityInCart }}
            <button
              type="button"
              class="btn btn-primary btn-sm ms-2"
              @click="increaseCart()"
            >
              +
            </button>

            <button
              class="btn btn-outline-danger btn-sm mx-4"
              @click="deleteFromCart()"
            >
              x
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="container bg-white py-2 my-2">
      <h3 class="text-center my-3">{{ product.name }} details</h3>

      <div class="p-3">{{ product.details }}</div>
    </div>

    <div class="container bg-light pb-2" v-if="categorySlug">
      <SomeProducts
        title="Most Viewed Products"
        :path="`/api/shop/products?limit=8&page=1&category=${categorySlug}`"
        nolink="false"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";

import SomeProducts from "@/components/SomeProducts";

export default {
  name: "product",
  data() {
    return {
      product: {},
      quantity: 1,
      quantityInCart: 0,
      bigImg: "",
      categorySlug: "",
    };
  },
  mounted() {
    document.title = "Product" + this.$store.state.sitename;
    this.getProduct();
  },
  components: { SomeProducts },
  watch: {
    $route(to, from) {
      if (to != from) {
        this.getProduct();
      }
    },
  },
  methods: {
    async getProduct() {
      await axios
        .get(`/api/shop/products/${this.$route.params.id}/`)
        .then((response) => {
          this.product = response.data;
          this.setQuantity();
          this.categorySlug = response.data.category_name
            .replace(" ", "-")
            .toLowerCase();

          if (response.data.image) {
            this.bigImg = response.data.image;
          } else {
            this.bigImg = "";
          }
        })
        .catch((error) => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data));
          } else {
            console.log(error);
          }
        });
    },
    setBigImg(img) {
      this.bigImg = img;
    },
    addToCart() {
      const obj = { product: this.product, quantity: this.quantity };
      this.$store.commit("addToCart", obj);
      this.setQuantity();
    },
    deleteFromCart() {
      this.$store.commit("deleteFromCart", this.product.id);
      this.setQuantity();
    },
    setQuantity() {
      let set_quantity = false;

      this.$store.state.cart.map((item) => {
        if (item.product.id === this.product.id) {
          this.quantityInCart = item.quantity;
          set_quantity = true;
        }
      });

      if (!set_quantity) {
        this.quantityInCart = 0;
      }
    },
    increaseCart() {
      this.$store.commit("increaseCart", this.product.id);
      this.setQuantity();
    },
    decreaseCart() {
      this.$store.commit("decreaseCart", this.product.id);
      this.setQuantity();
    },
  },
  computed: {},
};
</script>

<style scoped>
img {
  cursor: pointer;
}
</style>