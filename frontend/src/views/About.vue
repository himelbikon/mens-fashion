<template>
  <div class="about">
    This is about

    <router-link :to="{ name: 'home' }">home</router-link>
  </div>
</template>

<script>
export default {
  name: "about",
};
</script>