// <!-- Initialize Swiper -->
var swiper = new Swiper(".mySwiper", {
  spaceBetween: null,
  centeredSlides: true,

  speed: 1600,
  autoplay: {
    delay: 4000,

    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
