! function($) {
    // "use strict"; // jshint ;_;
    $(document.body).on("click", "th.link", function(event) {
        href = $(this).attr("href");
        window.location = href;
    });

    $(document.body).on("click", "tr.link > td", function(event) {
        if (event.target === this) {
            href = $(this).closest("tr.link").attr("href");
            window.location = href;
        }
    });
}(window.jQuery);
