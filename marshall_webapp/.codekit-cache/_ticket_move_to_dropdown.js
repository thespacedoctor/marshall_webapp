$(function() {
    console.log('move to links');

    $("a.ticketMoveToLink").bind("click", function(event) {
        // alert("found you");
        var notification = $(this).attr("notification");
        var notification = decodeURIComponent(notification);
        var dynamicNotification = $("span#dynamicNotification");
        dynamicNotification.html(notification);
        var thisTicket = $(this).closest("div.singleTicket");
        fade_and_hide(thisTicket);
    });
    $(document.body).on("click", "a.ticketMoveToLinkUndo", function(event) {
        var ticketId = $(this).attr("id");
        var ticketToShow = $("div#" + ticketId);
        show_and_unfade(ticketToShow);
        var dynamicNotification = $("span#dynamicNotification");
        setTimeout(function() {
            dynamicNotification.show().html("");
        }, 200);
    });
});
