<template>
  <div class="product-offer">
    <div
      class="container mt-5 bg-white p-5"
      v-for="showcase in showcases"
      :key="showcase.id"
    >
      <div class="row">
        <div class="col-12 col-lg-6 mb-3">
          <img
            :src="this.$store.state.url + showcase.image"
            :alt="this.$store.state.url + showcase.image"
            class="img-fluid w-100 rounded"
            v-if="showcase.image"
          />
          <img
            src="https://via.placeholder.com/500x500"
            alt=""
            class="img-fluid w-100 rounded"
            v-else
          />
        </div>

        <div class="col-12 col-lg-6">
          <div class="">
            <h3>{{ showcase.name }}</h3>
            <div>
              {{ showcase.details }}
            </div>
            <div class="mt-5">
              <router-link
                :to="{ name: 'product', params: { id: showcase.product_id } }"
                type="button"
                class="btn btn-outline-success"
              >
                View Product
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "product-showcase",
  data() {
    return {
      showcases: [],
    };
  },
  mounted() {
    axios
      .get("/api/shop/showcases/")
      .then((response) => {
        this.showcases = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        if (error.message) {
          console.log(JSON.stringify(error.response.data));
        } else {
          console.log("Something is wrong");
        }
      });
  },
};
</script>