<template>
  <div class="orders">
    <div class="container my-2 bg-white">
      <table class="table">
        <thead>
          <tr class="text-center">
            <th colspan="3">Orders</th>
          </tr>
          <tr>
            <th scope="col">Name</th>
            <th>Token</th>
            <th>Is Delivered?</th>
          </tr>
        </thead>
        <tbody class="text-dark">
          <tr v-for="order in orders" :key="order">
            <td scope="row">
              <router-link
                :to="{ name: 'order-details', params: { id: order.id } }"
              >
                {{ order.first_name }} {{ order.last_name }}
              </router-link>
            </td>
            <td>{{ order.token }}</td>
            <td>{{ order.delivered }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "orders",
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    document.title = "Orders" + this.$store.state.sitename;

    this.getOrders();
  },
  methods: {
    async getOrders() {
      console.log("get orders");
      await axios
        .get("/api/shop/orders/")
        .then((response) => {
          // for (const data in response.data) {
          //   this.orders.push(data);
          // }

          this.orders = response.data;
        })
        .catch((error) => {
          if (error.response) {
            console.log(JSON.stringify(error.response.data));
          } else {
            console.log("Something went wrong!");
          }
        });

      for (let i = 0; i < this.orders.length; i++) {
        if (this.orders[i].delivered) {
          this.orders[i].delivered = "True";
        } else {
          this.orders[i].delivered = "False";
        }
      }
    },
  },
};
</script>