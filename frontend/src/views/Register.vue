<template>
  <div class="register">
    <div class="container">
      <div class="row d-flex justify-content-center">
        <div class="col-12 col-md-6 col-lg-4 my-2 bg-white py-5 rounded">
          <form @submit.prevent="submitHandler()" v-if="!success">
            <!-- <legend class="text-center">Login</legend> -->

            <h4 class="text-center">Register</h4>

            <div class="form-group">
              <label for="exampleInputPassword1" class="form-label mt-4"
                >First Name:</label
              >
              <input
                type="text"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="First Name"
                v-model="first_name"
              />
            </div>

            <div class="form-group">
              <label for="exampleInputPassword1" class="form-label mt-4"
                >Last Name:</label
              >
              <input
                type="text"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Last Name"
                v-model="last_name"
              />
            </div>

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
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Password"
                v-model="password"
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
                v-model="password2"
              />
            </div>

            <div class="alert alert-danger" v-if="errors.length">
              <div v-for="error in errors" :key="error">{{ error }}</div>
            </div>

            <button type="submit" class="btn btn-outline-primary w-100">
              Register
            </button>
          </form>

          <div class="alert alert-success" v-if="success">
            <div>{{ success }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "register",
  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      password2: "",
      errors: [],
      success: "",
    };
  },
  mounted() {
    document.title = "Registration" + this.$store.state.sitename;
  },
  methods: {
    submitHandler() {
      this.errors = [];

      if (this.first_name === "") {
        this.errors.push(`First Name is empty!`);
      } else if (this.last_name === "") {
        this.errors.push(`Last Name is empty!`);
      } else if (this.email === "") {
        this.errors.push(`Email is empty!`);
      } else if (this.password === "") {
        this.errors.push(`Password is empty!`);
      } else if (this.password != this.password2) {
        this.errors.push(`Passwords didn.t matched!`);
      } else {
        this.registration();
      }
    },
    registration() {
      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        password: this.password,
        email_subject: document.title,
        url: this.$store.state.url,
      };

      axios
        .post(`/api/users/register/`, data)
        .then(() => {
          this.success = `Check your email ${this.email}`;
        })
        .catch((error) => {
          if (error.response) {
            for (const key in error.response.data) {
              this.errors.push(`${key}: ${error.response.data[key]}`);
              console.log(`${key}: ${error.response.data[key]}`);
            }
          } else {
            console.log(`Something is wrong`);
          }
        });
    },
  },
};
</script>