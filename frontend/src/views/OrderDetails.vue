<template>
  <div class="orrder-details">
    <div class="container my-2 bg-white">
      <table class="table">
        <tbody class="text-dark">
          <tr>
            <td scope="row">First Name:</td>
            <td>{{ order.first_name }} {{ order.last_name }}</td>
          </tr>

          <tr>
            <td>Last Name:</td>
            <td>{{ order.last_name }}</td>
          </tr>

          <tr>
            <td>Email:</td>
            <td>{{ order.email }}</td>
          </tr>

          <tr>
            <td>Phone:</td>
            <td>{{ order.phone }}</td>
          </tr>

          <tr>
            <td>Address:</td>
            <td>{{ order.address }}</td>
          </tr>
          <tr>
            <td>Zip Code:</td>
            <td>{{ order.zipcode }}</td>
          </tr>
          <tr>
            <td>Place:</td>
            <td>{{ order.place }}</td>
          </tr>
          <tr>
            <td>Total Place:</td>
            <td>{{ order.paid_amount }}</td>
          </tr>

          <tr>
            <td>Token:</td>
            <td>{{ order.token }}</td>
          </tr>
        </tbody>
      </table>

      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in order.items" :key="item">
            <td scope="row">
              <router-link
                :to="{ name: 'product', params: { id: item.product } }"
              >
                {{ item.name }}
              </router-link>
            </td>
            <td>{{ item.price }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.quantity * item.price }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "order-details",
  data() {
    return {
      order: {},
    };
  },
  mounted() {
    document.title = "Order Details" + this.$store.state.sitename;

    this.getOrder();
  },
  methods: {
    async getOrder() {
      axios
        .get(`/api/shop/orders/${this.$route.params.id}/`)
        .then((response) => {
          this.order = response.data;
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data);
            for (const key in error.response.data) {
              console.log(key, error.response.data[key]);
            }
          } else {
            console.log(error);
          }
        });
    },
  },
};
</script>