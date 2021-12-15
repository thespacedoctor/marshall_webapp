var fade_and_hide = function(element) {
    // console.log('fade and hide animation triggered');

    element.animate({
        opacity: 0.25
    }, 150);
    element.delay(600).slideUp(300);
}
