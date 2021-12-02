<template>
  <div class="cart">
    <div class="container bg-white my-2">
      <table class="table" v-if="this.$store.state.cart.length">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Qty</th>
            <th scope="col">Full Price</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr
            class="text-dark"
            v-for="(item, key) in this.$store.state.cart"
            :key="item.id"
          >
            <td>{{ key + 1 }}</td>
            <td scope="row">
              <router-link
                :to="{ name: 'product', params: { id: item.product.id } }"
              >
                {{ item.product.name }}
              </router-link>
            </td>
            <td>${{ item.product.price }}</td>
            <td>
              {{ item.quantity }}
            </td>
            <td>${{ item.product.price * item.quantity }}</td>
            <td>
              <button
                type="button"
                class="btn btn-primary btn-sm me-2"
                @click="decreaseCart(item.product.id)"
              >
                -
              </button>
              <button
                type="button"
                class="btn btn-primary btn-sm ms-2"
                @click="increaseCart(item.product.id)"
              >
                +
              </button>

              <button
                class="btn btn-outline-danger btn-sm mx-4"
                @click="deleteFromCart(item.product.id)"
              >
                x
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <h5 class="p-2 text-center" v-else>No products in cart!</h5>
    </div>

    <div class="container my-2 bg-white py-2">
      <h5 class="my-4">Total Price: ${{ totalCartPrice }}</h5>
      <router-link
        class="btn btn-outline-primary text-white"
        :to="{ name: 'checkout' }"
        >Checkout</router-link
      >
    </div>
  </div>
</template>


<script>
export default {
  name: "cart",
  mounted() {
    document.title = "Cart" + this.$store.state.sitename;
  },
  methods: {
    increaseCart(id) {
      this.$store.commit("increaseCart", id);
    },
    decreaseCart(id) {
      this.$store.commit("decreaseCart", id);
    },
    deleteFromCart(id) {
      this.$store.commit("deleteFromCart", id);
    },
  },
  computed: {
    totalCartPrice() {
      let price = 0;

      this.$store.state.cart.map((i) => {
        price += i.product.price * i.quantity;
      });

      return price;
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