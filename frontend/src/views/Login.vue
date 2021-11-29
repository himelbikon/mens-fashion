<template>
  <div class="login">This is login</div>
</template>

<script>
export default {
  name: "login",
  mounted() {
    document.title = "Login" + this.$store.state.sitename;
  },
};
</script>