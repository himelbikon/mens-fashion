<template>
  <div class="product">this is product {{ this.$route.params.id }}</div>
</template>

<script>
export default {
  name: "product",
  mounted() {
    document.title = "Product" + this.$store.state.sitename;
  },
};
</script>