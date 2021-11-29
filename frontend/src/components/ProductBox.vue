<template>
  <div class="bg-white shadow">
    <div>
      <router-link :to="{ name: 'product', params: { id: product.id } }">
        <img
          :src="`${this.$store.state.url}${product.image}`"
          :alt="`${this.$store.state.url}${product.image}`"
          class="img-fluid w-100"
          v-if="product.image"
        />
        <img
          src="https://via.placeholder.com/500x500"
          alt=""
          class="img-fluid w-100"
          v-else
        />
      </router-link>
    </div>
    <div class="p-2">
      <h5>
        <router-link :to="{ name: 'product', params: { id: product.id } }">
          {{ product.name }}
        </router-link>
      </h5>
      <p>Price: ${{ product.price }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "product-box",
  props: {
    product: Object,
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>