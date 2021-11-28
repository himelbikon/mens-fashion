<template>
  <div class="footer bg-dark text-white">
    <div class="container mt-3">
      <div class="row">
        <div class="col-12 col-md-4 my-3">
          <h3>
            <router-link :to="{ name: 'home' }" class="navbar-brand" href="#"
              >Mens Fashion</router-link
            >
          </h3>
          <div>
            Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Dignissimos corrupti facere aperiam, molestiae deleniti magnam vero
            iure mollitia quo soluta.
          </div>
        </div>
        <div class="col-12 col-md-4 my-3">
          <h3>Quick Links</h3>
          <ul>
            <li>
              <router-link class="text-white" :to="{ name: 'home' }"
                >Home</router-link
              >
            </li>
            <li>
              <router-link class="text-white" :to="{ name: 'home' }"
                >About</router-link
              >
            </li>
            <li>
              <router-link class="text-white" :to="{ name: 'home' }"
                >Shop</router-link
              >
            </li>
            <li>
              <router-link class="text-white" :to="{ name: 'home' }"
                >Contact us</router-link
              >
            </li>
          </ul>
        </div>
        <div class="col-12 col-md-4 my-3">
          <h3>Quick Links</h3>
          <div class="d-flex justify-content-center flex-wrap">
            <router-link
              :to="{ name: 'home' }"
              class="m-2 py-2 px-4 bg-light text-dark rounded-pill"
              >Men</router-link
            >
            <router-link
              :to="{ name: 'home' }"
              class="m-2 py-2 px-4 bg-light text-dark rounded-pill"
              >Women</router-link
            >
            <router-link
              :to="{ name: 'home' }"
              class="m-2 py-2 px-4 bg-light text-dark rounded-pill"
              >Men</router-link
            >
            <router-link
              :to="{ name: 'home' }"
              class="m-2 py-2 px-4 bg-light text-dark rounded-pill"
              >Women</router-link
            >
            <router-link
              :to="{ name: 'home' }"
              class="m-2 py-2 px-4 bg-light text-dark rounded-pill"
              >Men</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "footer",
};
</script>

<style scoped>
ul {
  list-style: none;
}

a {
  text-decoration: none;
}
</style>