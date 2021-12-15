$(function() {
    //   console.log('move to links');

    $("a.ticketMoveToLink").bind("click", function(event) {
        // alert("found you");
        var notification = $(this).attr("notification");
        var notification = decodeURIComponent(notification);
        var dynamicNotification = $("span#dynamicNotification");
        dynamicNotification.html(notification);
        var thisTicket = $(this).closest("div.singleTicket");
        fade_and_hide(thisTicket);
        $.post("/marshall/actions/refresh_sidebar_list_counts?method=put");
    });
    $(document.body).on("click", "a.ticketMoveToLinkUndo", function(event) {
        var ticketId = $(this).attr("id");
        var ticketToShow = $("div#" + ticketId);
        show_and_unfade(ticketToShow);
        var dynamicNotification = $("span#dynamicNotification");
        setTimeout(function() {
            dynamicNotification.show().html("");
        }, 200);
        $.post("/marshall/actions/refresh_sidebar_list_counts?method=put")
    });

});
