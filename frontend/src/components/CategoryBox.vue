<template>
  <div class="category-box">
    <div class="container">
      <h2 class="text-center my-3">Categories</h2>
      <div class="row d-flex justify-content-center">
        <div
          class="col-5 col-md-3 col-lg-2 my-1"
          v-for="category in categories"
          :key="category.id"
        >
          <div class="bg-white text-center rounded">
            <div>
              <router-link :to="{ name: 'home' }">
                <img
                  :src="`${this.$store.state.url}${category.image}`"
                  :alt="`${this.$store.state.url}${category.image}`"
                  class="img-fluid w-100 rounded"
                  v-if="category.image"
                />
                <img
                  src="https://via.placeholder.com/350x200"
                  alt=""
                  class="img-fluid w-100 rounded"
                  v-else
                />
              </router-link>
            </div>
            <h6 class="p-1">
              <router-link :to="{ name: 'home' }">
                {{ category.name }}
              </router-link>
            </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "category-box",
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    axios
      .get("/api/shop/categories/")
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        if (error.response) {
          console.log(JSON.stringify(error.response.data));
        }
      });
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>

