<template>
  <div class="product-offer">
    <div class="container mt-5 bg-white p-5">
      <div class="row">
        <div class="col-12 col-lg-6">
          <img
            src="https://via.placeholder.com/500x500"
            alt=""
            class="img-fluid w-100 rounded"
          />
        </div>

        <div class="col-12 col-lg-6 my-3">
          <div class="">
            <h3>Smart Watch</h3>
            <div>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Libero,
              in aliquam, quia iste, amet illo ullam accusamus quasi ipsa
              pariatur cum quod ipsum quam atque ut natus rem porro. Dolore
              magnam, reprehenderit quasi nostrum reiciendis sequi et amet enim
              sed iure doloremque iusto aspernatur cum nemo. Temporibus, enim.
              Tempora, eius!
            </div>
            <div class="mt-5">
              <router-link
                :to="{ name: 'home' }"
                type="button"
                class="btn btn-outline-success"
              >
                View Product
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>