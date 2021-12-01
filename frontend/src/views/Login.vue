<template>
  <div class="login">
    <div class="container">
      <div class="row d-flex justify-content-center">
        <div class="col-12 col-md-6 col-lg-4 my-2 bg-white py-5 rounded">
          <form @submit.prevent="submitHandler()">
            <!-- <legend class="text-center">Login</legend> -->

            <h4 class="text-center">Login</h4>

            <div class="form-group">
              <label for="exampleInputEmail1" class="form-label mt-3"
                >Email address</label
              >
              <input
                type="email"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                placeholder="Enter email"
                v-model="email"
              />
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1" class="form-label mt-4"
                >Password</label
              >
              <input
                type="password"
                class="form-control mb-5"
                id="exampleInputPassword1"
                placeholder="Password"
                v-model="password"
              />
            </div>

            <div class="alert alert-danger" v-if="errors.length">
              <div v-for="error in errors" :key="error">{{ error }}</div>
            </div>

            <button type="submit" class="btn btn-outline-primary w-100">
              Login
            </button>

            <div class="alert alert-danger" v-if="success">
              <div>{{ success }}</div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      errors: [],
      success: "",
      email: "",
      password: "",
    };
  },
  mounted() {
    document.title = "Login" + this.$store.state.sitename;
  },
  methods: {
    async submitHandler() {
      // console.log("form");
      this.errors = [];

      if (this.email === "") {
        this.errors.push("Enter your email please!");
      } else if (this.password === "") {
        this.errors.push("Enter password please!");
      } else {
        await axios
          .post("/api/users/token/", {
            email: this.email,
            password: this.password,
          })
          .then((response) => {
            const token = response.data.access;
            this.$store.commit("setLogin", token);
            if (this.$route.query.to) {
              this.$router.push(this.$route.query.to);
            } else {
              this.$router.push({ name: "home" });
            }
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${error.response.data[property]}`);
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.error.push("Something went wrong. Please try later!");
              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>

<style scoped>
</style>