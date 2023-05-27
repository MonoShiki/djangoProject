$(document).ready(function(){
  $('.carousel').slick({
    dots: false,
    infinite: true,
    speed: 400,
    slidesToShow: 5,
    slidesToScroll: 1,
    adaptiveHeight: true,
    arrows:true,
    autoplay:true,
    autoPlayTimer:"20s"
  });
});

const dropdownLink = document.getElementById('dropdown-link');
const dropdownMenu = document.getElementById('dropdown-menu');

dropdownLink.addEventListener('mouseover', () => {
  dropdownMenu.style.display = 'block';
});

dropdownLink.addEventListener('mouseout', () => {
  dropdownMenu.style.display = 'none';
});