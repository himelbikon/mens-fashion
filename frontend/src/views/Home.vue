<template>
  <div class="home">
    <router-link :to="{ name: 'about' }">about</router-link>
  </div>
</template>

<script>
export default {
  name: "home",
};
</script>