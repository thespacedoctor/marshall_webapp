$(function() {
    //console.log('affix some love');
    var leftSideBar = $('div#leftSidebar');
    if ($(window).innerWidth() > 1040 && $(window).innerHeight() > leftSideBar.height() * 1.2) {
        $('div#leftSidebar').affix({
            offset: {
                top: 170,
                bottom: 100
            }
        });
    }
});
