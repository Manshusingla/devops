// window.onscroll = function() {scrollFunction()};

// function scrollFunction() {
//   if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
//     let ele = document.getElementsByClassName('header1')[0];
//     ele.setAttribute ('style', 'background-color: #00b98e !important;');
//   } else {
//     let ele = document.getElementsByClassName('header1')[0];
//     ele.setAttribute ('style', 'background-color: white !important;');
//   }
// }

//   jQuery(function($) {
//      var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
//      $('ul a').each(function() {
//       if (this.href === path) {
//        $(this).addClass('active');
//       }
//      });
//     });

$(function($) {
    let url = window.location.href;
     $('nav ul li a').each(function() {
      if (this.href === url) {
      $(this).addClass('active');
     }
    });
   });