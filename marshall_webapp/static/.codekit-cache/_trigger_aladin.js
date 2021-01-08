
// _trigger_aladin.js
// ==================
// Author: Dave Young
// Date created: September 29, 2015
// Summary: Trigger Aladin with context tab selected

$(function() {
    $("a[data-toggle='tab']").bind("click", function(event) {

        if ($(this).text().indexOf("context") >= 0) {
            var reset = reset_all_tickets;
            reset();
            var thisId = $(this).attr('href');
            var aladinDiv = $("div" + thisId).find("div.aladin-hide");
            aladinDiv.attr('class', "aladin");
            dryxAladin(aladinDiv);
        }
    });
});

function reset_all_tickets() {
    $("div.aladin").each(function(index, thisObject) {
        $(thisObject).attr('class', "aladin-hide");
        $(thisObject).html("");
    });

    $("div.singleTicket").each(function(index, thisObject) {
        $(thisObject).find("a[data-toggle='tab']:first").click();
    });
}
