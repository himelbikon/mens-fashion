<template>
  <div class="checkout">
    <div class="container my-2">
      <div class="row">
        <div class="col-12 col-md-6">
          <table class="table bg-white" v-if="cart.length">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Price</th>
                <th scope="col">Qty</th>
                <th scope="col">Full Price</th>
              </tr>
            </thead>
            <tbody>
              <tr class="text-dark" v-for="item in cart" :key="item">
                <td scope="row">
                  <router-link
                    :to="{ name: 'product', params: { id: item.product.id } }"
                  >
                    {{ item.product.name }}
                  </router-link>
                </td>
                <td>${{ item.product.price }}</td>
                <td>{{ item.quantity }}</td>
                <td>${{ item.product.price * item.quantity }}</td>
              </tr>
            </tbody>
          </table>

          <h5 class="p-2 text-center" v-else>No products in cart!</h5>

          <div class="bg-white text-dark p-2">Total: {{ totalPrice }}</div>
        </div>

        <div class="col-12 col-md-6 bg-white">
          <h5 class="py-2">Shipping details</h5>

          <form v-if="this.$store.state.cart.length">
            <div class="form-group mb-4">
              <label class="form-label" for="inputDefault">First Name</label>
              <input
                type="text"
                class="form-control"
                placeholder="First Name"
                id="inputDefault"
                v-model="first_name"
              />
            </div>

            <div class="form-group mb-4">
              <label class="form-label" for="inputDefault">Last Name</label>
              <input
                type="text"
                class="form-control"
                placeholder="Last Name"
                id="inputDefault"
                v-model="last_name"
              />
            </div>

            <div class="form-group mb-4">
              <label for="exampleInputEmail1" class="form-label"
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

            <div class="form-group mb-4">
              <label class="form-label" for="inputDefault">Phone</label>
              <input
                type="text"
                class="form-control"
                placeholder="Phone"
                id="inputDefault"
                v-model="phone"
              />
            </div>

            <div class="form-group mb-4">
              <label class="form-label" for="inputDefault">Address</label>
              <input
                type="text"
                class="form-control"
                placeholder="Address"
                id="inputDefault"
                v-model="address"
              />
            </div>

            <div class="form-group mb-4">
              <label class="form-label" for="inputDefault">Zip Code</label>
              <input
                type="text"
                class="form-control"
                placeholder="Zip Code"
                id="inputDefault"
                v-model="zipcode"
              />
            </div>

            <div class="form-group mb-4">
              <label class="form-label" for="inputDefault">Place</label>
              <input
                type="text"
                class="form-control"
                placeholder="Place"
                id="inputDefault"
                v-model="place"
              />
            </div>

            <div class="alert alert-danger" v-if="errors.length">
              <div v-for="error in errors" :key="error">{{ error }}</div>
            </div>

            <!-- <button
              type="button"
              class="btn btn-outline-primary my-2"
              @click="orderHandler"
            >
              Submit
            </button> -->

            <div>
              <div ref="paypal"></div>
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
  name: "checkout",
  data() {
    return {
      no_blank: false,
      loaded: false,
      paidFor: false,
      cart: {},
      items: [],
      errors: [],
      totalPrice: 0,
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      zipcode: "",
      place: "",
      token: "Ecommerce_",
    };
  },
  mounted() {
    document.title = "Checkout" + this.$store.state.sitename;
    this.cart = this.$store.state.cart;
    this.totalCartPrice();
    this.collectItems();
    this.generateToken();
    this.mountPaypal();
  },
  methods: {
    mountPaypal: function () {
      const script = document.createElement("script");
      script.src =
        "https://www.paypal.com/sdk/js?client-id=AbzYFUyRQHaRRb0NQ6vsehobiGBGwcFjcJBlMIxrfbzy_mFH4nklge6-raop0Nk9YW2Ryulu9Z0yPI_z";
      // AbzYFUyRQHaRRb0NQ6vsehobiGBGwcFjcJBlMIxrfbzy_mFH4nklge6-raop0Nk9YW2Ryulu9Z0yPI_z
      script.addEventListener("load", this.setLoaded);
      document.body.appendChild(script);
    },
    setLoaded: function () {
      this.loaded = true;
      window.paypal
        .Buttons({
          createOrder: (data, actions) => {
            this.blankChecker();
            if (this.no_blank) {
              return actions.order.create({
                purchase_units: [
                  {
                    description: this.token,
                    amount: {
                      currency_code: "USD",
                      value: this.totalPrice,
                    },
                  },
                ],
              });
            }
          },
          onApprove: async (data, actions) => {
            const order = await actions.order.capture();
            this.data;
            this.paidFor = true;
            console.log(order);
            this.orderHandler();
          },
          onError: (err) => {
            console.log(err);
          },
        })
        .render(this.$refs.paypal);
    },
    totalCartPrice() {
      let price = 0;
      this.cart.map((i) => {
        price += i.product.price * i.quantity;
      });

      this.totalPrice = price;
    },
    async orderHandler() {
      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        phone: this.phone,
        address: this.address,
        zipcode: this.zipcode,
        place: this.place,
        token: this.token,
        paid_amount: this.totalPrice,
        items: this.items,
      };

      await axios
        .post("/api/shop/orders/", data)
        .then(() => {
          this.$store.commit("clearCart");
          this.$router.push({ name: "orders" });
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            this.error.push("Something went wrong. Please try later!");
            console.log(JSON.stringify(error));
          }
        });
    },
    blankChecker() {
      this.errors = [];

      if (this.first_name === "") {
        this.errors.push("Enter first name");
      } else if (this.last_name === "") {
        this.errors.push("Enter last name");
      } else if (this.email === "") {
        this.errors.push("Enter email");
      } else if (this.phone === "") {
        this.errors.push("Enter phone");
      } else if (this.address === "") {
        this.errors.push("Enter address");
      } else if (this.zipcode === "") {
        this.errors.push("Enter zipcode");
      } else if (this.place === "") {
        this.errors.push("Enter place");
      } else {
        this.no_blank = true;
      }
    },
    collectItems() {
      this.cart.map((i) => {
        const item = {
          product: i.product.id,
          price: i.product.price,
          quantity: i.quantity,
        };

        this.items.push(item);
      });
    },
    generateToken() {
      const string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
      let token = "";
      for (let i = 0; i < 20; i++) {
        token += string[this.random(0, string.length)];
      }
      this.token += token;
      // console.log(this.token);
    },
    random(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>