<template>
  <div>
    <div
      id="carouselExampleCaptions"
      class="carousel slide"
      data-bs-ride="carousel"
    >
      <div class="carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleCaptions"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img
            src="../assets/1.jpg"
            class="d-block w-100"
            alt="../assets/a.jpg"
          />
          <div class="carousel-caption d-none d-md-block">
            <!-- <h5>First slide label</h5> -->
            <!-- <p class="bg-light text-dark py-2 rounded">
              Some representative placeholder content for the first slide.
            </p> -->
            <router-link :to="{ name: 'shop' }" class="btn btn-outline-primary"
              >Shop Now</router-link
            >
          </div>
        </div>
        <div class="carousel-item">
          <img
            src="../assets/2.jpg"
            class="d-block w-100"
            alt="../assets/a.jpg"
          />
          <div class="carousel-caption d-none d-md-block">
            <!-- <p class="bg-light text-dark py-2 rounded">
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit
              reiciendis, ullam quam expedita inventore pariatur.
            </p> -->
            <router-link :to="{ name: 'shop' }" class="btn btn-outline-primary"
              >Shop Now</router-link
            >
          </div>
        </div>
        <div class="carousel-item">
          <img
            src="../assets/3.jpg"
            class="d-block w-100"
            alt="../assets/a.jpg"
          />
          <div class="carousel-caption d-none d-md-block">
            <!-- <p class="bg-light text-dark py-2 rounded">
              Some representative placeholder content for the first slide.
            </p> -->
            <router-link :to="{ name: 'shop' }" class="btn btn-outline-primary"
              >Shop Now</router-link
            >
          </div>
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "carousel",
};
</script>

<style scoped>
img {
  width: 100%;
}
</style>