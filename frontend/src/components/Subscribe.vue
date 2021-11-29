<template>
  <div class="subscribe">
    <div class="container my-5 bg-primary py-5 rounded">
      <div class="row py-5">
        <div class="col-12 col-md-6 d-flex justify-content-center">
          <div class="text-white">
            <h2 class="text-white">Get Our Latest Offers News</h2>
            <p>Subscribe news latter</p>
          </div>
        </div>

        <div class="col-12 col-md-6">
          <div class="form-group mx-3">
            <div class="input-group">
              <input
                type="email"
                class="form-control mx-3"
                placeholder="Your Email here"
                aria-label="Recipient's username"
                aria-describedby="button-addon2"
                disabled
                v-if="subscribed"
                v-model="email"
              />
              <input
                type="email"
                class="form-control mx-3"
                placeholder="Your Email here"
                aria-label="Recipient's username"
                aria-describedby="button-addon2"
                v-else
                v-model="email"
              />
              <button
                class="btn btn-primary rounded-1"
                type="button"
                id="button-addon2"
                disabled
                v-if="subscribed"
                @click="postSubscribe()"
              >
                Subscribe
              </button>
              <button
                class="btn btn-primary rounded-1"
                type="button"
                id="button-addon2"
                v-else
                @click="postSubscribe()"
              >
                Subscribe
              </button>
            </div>
          </div>
        </div>
      </div>
      <!-- <div class="row text-center text-white" v-if="subscribed">
        <div>Your email submitted successfully. Thank You!</div>
      </div> -->
      <div class="row d-flex justify-content-center">
        <div
          class="alert alert-success text-white col-10 col-md-6"
          v-if="subscribed"
        >
          <div>Your email submitted successfully. Thank You!</div>
        </div>
        <div class="alert alert-danger text-white col-10 col-md-6" v-if="alert">
          <div>{{ alert }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "subscribe",
  data() {
    return {
      subscribed: false,
      email: "",
      alert: "",
    };
  },
  methods: {
    postSubscribe() {
      this.alert = "";
      if (this.email) {
        axios
          .post("/api/users/subscribe/", { email: this.email })
          .then(() => {
            this.subscribed = true;
          })
          .catch((error) => {
            if (error.response) {
              console.log(JSON.stringify(error.response.data));
            }
          });
      } else {
        this.alert = "Enter your email, please!";
      }
    },
  },
};
</script>