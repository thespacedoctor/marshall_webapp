var post_to_url_in_background = function(event) {

    event.preventDefault();
    var href = $(this).attr("href");
    var action = $(this).attr("action");
    if (typeof href !== 'undefined' && href !== false) {
        $.get(href, function(data, textStatus) {});
    }

    var notification = $(this).attr("notification");
    if (typeof notification !== 'undefined' && notification !== false) {
        var notification = decodeURIComponent(notification);
        var dynamicNotification = $("span#dynamicNotification");
        dynamicNotification.html(notification);
    }
}
