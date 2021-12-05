<template>
  <div class="category-box">
    <div class="container">
      <h2 class="text-center my-4"><span class="title shadow">Categories</span></h2>
      <div class="row d-flex justify-content-center">
        <div
          class="col-5 col-md-3 col-lg-2 my-1"
          v-for="category in this.$store.state.categories"
          :key="category.id"
        >
          <div class="bg-white text-center rounded">
            <div>
              <router-link
                :to="{ name: 'shop', query: { category: category.slug } }"
              >
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
              <router-link
                :to="{ name: 'shop', query: { category: category.slug } }"
              >
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
export default {
  name: "category-box",
  data() {
    return {};
  },
  mounted() {},
};
</script>

<style scoped>
a {
  text-decoration: none;
}

/*h2 {
  text-decoration: underline;
  }*/
</style>

