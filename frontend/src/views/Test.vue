<template>
  <div class="test">
    <div class="text-center" v-for="product in products" :key="product.id">
      <h3>{{ product.s }}</h3>
    </div>

    <div class="text-center">
      <button class="btn btn-outline-primary" @click="action()">
        Load More
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "test",
  data() {
    return {
      products: [
        { id: 1, s: "asas" },
        { id: 2, s: "sdsd" },
      ],
    };
  },
  methods: {
    action() {
      console.log("click");

      this.products.push({ id: 3, s: "sdsd" });
    },
  },
};
</script>