$(function() {
    //console.log('affix some love');
    if ($(window).width() > 1040) {
        $('div#leftSidebar').affix({
            offset: {
                top: 170,
                bottom: 50
            }
        });
    }
});
