var show_and_unfade = function(element) {
  console.log('fade and hide animation triggered');

  element.animate({
    opacity: 1.0
  }, 150);
  element.delay(600).slideDown(300);
}