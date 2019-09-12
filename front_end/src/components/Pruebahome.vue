<template >
  <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <div class="slider-size">
          <img src="../../static/neveraxD.jpg" style="height: 100%;" />
        </div>
      </div>
      <div class="carousel-item">
        <div class="slider-size">
          <img src="../../static/neveraxD.jpg" style="height: 100%;" />
        </div>
      </div>
      <div class="carousel-item">
        <div class="slider-size">
          <img src="../../static/neveraxD.jpg" style="height: 80%;" />
        </div>
      </div>
    </div>
    <a
      class="carousel-control-prev"
      href="#carouselExampleIndicators"
      role="button"
      data-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a
      class="carousel-control-next"
      href="#carouselExampleIndicators"
      role="button"
      data-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</template>

<script>
export default {};
</script>
<style scoped>
@media (max-width: 767px) {
  .slider-size {
    height: auto;
  }
  .slider-size > img {
    width: 80%;
  }
}

/* tablets */
@media (max-width: 991px) and (min-width: 768px) {
  .slider-size {
    height: auto;
  }
  .slider-size > img {
    width: 80%;
  }
}

/* laptops */
@media (max-width: 1023px) and (min-width: 992px) {
  .slider-size {
    height: 200px;
  }
  .slider-size > img {
    width: 80%;
  }
}

/* desktops */
@media (min-width: 1024px) {
  .slider-size {
    height: 300px;
  }
  .slider-size > img {
    width: 60%;
  }
}
</style>