<template>
  <div class="cart">
    <div class="container">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Quantity</th>
            <th scope="col">Full Price</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
            class="table-secondary"
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
            <td>{{ item.product.price }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.product.price * item.quantity }}</td>
            <td><button class="btn btn-outline-danger btn-sm">x</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>


<script>
export default {
  name: "cart",
  mounted() {
    document.title = "Cart" + this.$store.state.sitename;
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>