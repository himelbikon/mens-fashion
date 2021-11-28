<template>
  <div class="col-12 col-md-6 col-lg-3 my-4">
    <div class="bg-white shadow">
      <div>
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
      </div>
      <div class="p-2">
        <h5>{{ product.name }}</h5>
        <p>Price: ${{ product.price }}</p>
      </div>
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