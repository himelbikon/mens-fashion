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
          <h4 class="fw-bold mb-3">{{ product.name }}</h4>
          <div>Price: {{ product.price }}</div>
          <div>Category: {{ product.category_name }}</div>
          <div>Viewed: {{ product.views }}</div>
          <p class="my-2" v-if="product.details">
            {{ product.details.substring(0, 200).concat("...") }}
          </p>
          <hr />

          <div class="input-group mb-3 w-75">
            <input
              type="number"
              min="1"
              class="form-control mx-3"
              aria-label="Recipient's username"
              aria-describedby="button-addon2"
            />
            <button
              class="btn btn-primary rounded-1"
              type="button"
              id="button-addon2"
            >
              Add To Cart
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "product",
  data() {
    return {
      product: "",
      bigImg: "",
    };
  },
  mounted() {
    document.title = "Product" + this.$store.state.sitename;

    this.getProduct();
  },
  methods: {
    async getProduct() {
      // console.log(this.$route.params);
      await axios
        .get(`/api/shop/products/${this.$route.params.id}/`)
        .then((response) => {
          this.product = response.data;
          if (response.data.image) {
            this.bigImg = response.data.image;
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
  },
};
</script>

<style scoped>
img {
  cursor: pointer;
}
</style>