<template>
  <div class="profile">{{ user }}</div>
</template>

<script>
export default {
  name: "profile",
  data() {
    return {
      user: {},
    };
  },
  mounted() {
    document.title = "Profile" + this.$store.state.sitename;
    this.user = this.$store.state.user;
  },
};
</script>