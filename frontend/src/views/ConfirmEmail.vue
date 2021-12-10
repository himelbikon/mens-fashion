<template>
  <div class="confirm-email">confirm email</div>
</template>

<script>
import axios from "axios";
export default {
  name: "confirm-email",
  mounted() {
    document.title = "Confirm Email" + this.$store.state.sitename;
    if (this.$store.state.user.email_confirmed) {
      this.$router.push({ name: "home" });
    }

    this.send_mail();
  },
  methods: {
    send_mail() {
      axios
        .get("/api/users/email-confirmation/")
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data);
          } else {
            console.log("Soemthing went wrong!");
          }
        });
    },
  },
};
</script>