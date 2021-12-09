<template>
  <div class="header">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <router-link :to="{ name: 'home' }" class="navbar-brand">
          <img class="img-fluid" src="../assets/a.png" style="width: 50px" />
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarColor03"
          aria-controls="navbarColor03"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarColor03">
          <div class="form-group">
            <div class="input-group">
              <input
                class="form-control me-sm-2 px-3"
                type="text"
                placeholder="Search"
                aria-describedby="button-addon2"
              />
              <button
                class="btn btn-secondary my-2 my-sm-0 rounded-1"
                type="submit"
                id="button-addon2"
              >
                Search
              </button>
            </div>
          </div>

          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link :to="{ name: 'home' }" class="nav-link"
                >Home
                <span class="visually-hidden">(current)</span>
              </router-link>
            </li>

            <li class="nav-item">
              <router-link :to="{ name: 'shop' }" class="nav-link"
                >Shop</router-link
              >
            </li>

            <li
              class="nav-item dropdown"
              v-if="this.$store.state.isAuthenticated"
            >
              <a
                class="nav-link dropdown-toggle"
                data-bs-toggle="dropdown"
                href="#"
                role="button"
                aria-haspopup="true"
                aria-expanded="false"
                >User</a
              >
              <div class="dropdown-menu">
                <router-link :to="{ name: 'orders' }" class="dropdown-item">
                  Orders
                </router-link>
                <!-- <a class="dropdown-item" href="#">Another action</a>
                <a class="dropdown-item" href="#">Something else here</a> -->
                <!-- <div class="dropdown-divider"></div> -->
                <button class="dropdown-item" @click="logout">Logout</button>
              </div>
            </li>

            <li class="nav-item">
              <router-link :to="{ name: 'about' }" class="nav-link"
                >About</router-link
              >
            </li>
            <li class="nav-item" v-if="!this.$store.state.isAuthenticated">
              <router-link :to="{ name: 'login' }" class="nav-link"
                >Login</router-link
              >
            </li>
            <li class="nav-item" v-if="!this.$store.state.isAuthenticated">
              <router-link :to="{ name: 'register' }" class="nav-link"
                >Register</router-link
              >
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'cart' }" class="nav-link"
                ><i class="fas fa-shopping-cart"></i> ({{
                  this.$store.state.cart.length
                }})
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "header",
  methods: {
    logout() {
      this.$store.commit("setLogout");
      this.$router.push({ name: "home" });
    },
  },
};
</script>