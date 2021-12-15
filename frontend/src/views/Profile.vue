<template>
  <div class="profile">
    <div class="container bg-white">
      <div class="row">
        <div class="col-12 col-lg-6">
          <div class="my-2">
            <form>
              <div class="my3">
                <label for="exampleInputEmail1" class="form-label"
                  >First Name</label
                >
                <input
                  type="text"
                  class="form-control"
                  aria-describedby="emailHelp"
                  :value="user.first_name"
                />
              </div>
              <div class="my-3">
                <label for="exampleInputEmail1" class="form-label"
                  >Email address</label
                >
                <input
                  type="email"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                  :value="user.email"
                />
              </div>

              <button type="button" class="btn btn-outline-primary">
                Save
              </button>

              <div>{{ user }}</div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "profile",
  data() {
    return {
      user: {},
    };
  },
  mounted() {
    document.title = "Profile" + this.$store.state.sitename;
    this.user = this.$store.state.user;
  },
};
</script>