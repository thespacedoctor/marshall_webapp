// _multi_link_exploder.js
// =======================
// Author: Dave Young
// Date created: June 6, 2014
// Summary: Explode the links found in a dropdown link

// xjs-ready-event-function
// xjs-get-json-response-from-python-script

var multi_link_exploder = function() {
    console.log('multi link exploder triggered');

    var links = $(this).siblings("ul.dropdown-menu").children("li");
    links.each(function(index) {
        var url = $(this).children("a").attr("href");
        window.open(url, "_blank");
    });
};
