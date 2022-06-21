// <!-- Initialize Swiper -->
var swiper = new Swiper(".Swiper-slide", {
  spaceBetween: 30,
  loop: true,
  autoplay: {
     delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
