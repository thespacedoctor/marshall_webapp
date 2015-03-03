$(function() {
    $(document.body).on("click", "a.changePriorityLink", function() {
        var thisTicket = $(this).closest("div.singleTicket");
        var oldClass = thisTicket.attr("class");
        var newPriority = $(this).text();

        // display the hidden priority link and hide the one just clicked
        var dropdownMenu = $(this).closest(".dropdown-menu");
        dropdownMenu.find("li.hidden").toggleClass("hidden");
        $(this).closest("li").toggleClass("hidden");

        // Remove old border and label color
        if (oldClass.indexOf("border-red") >= 0) {
            thisTicket.toggleClass("border-red");
            thisTicket.find(".priorityLabel").toggleClass("red");
        } else if (oldClass.indexOf("border-yellow") >= 0) {
            thisTicket.toggleClass("border-yellow");
            thisTicket.find(".priorityLabel").toggleClass("yellow");
        } else if (oldClass.indexOf("border-green") >= 0) {
            thisTicket.toggleClass("border-green");
            thisTicket.find(".priorityLabel").toggleClass("green");
        }

        // Add new border and label color
        if (newPriority.indexOf("critical") >= 0) {
            thisTicket.toggleClass("border-red");
            thisTicket.find(".priorityLabel").toggleClass("red");
            thisTicket.find(".priorityLabel").html("<strong>CRITICAL</strong>");
        } else if (newPriority.indexOf("important") >= 0) {
            thisTicket.toggleClass("border-yellow");
            thisTicket.find(".priorityLabel").toggleClass("yellow");
            thisTicket.find(".priorityLabel").html("<strong>IMPORTANT</strong>");
        } else if (newPriority.indexOf("useful") >= 0) {
            thisTicket.toggleClass("border-green");
            thisTicket.find(".priorityLabel").toggleClass("green");
            thisTicket.find(".priorityLabel").html("<strong>USEFUL</strong>");
        } else if (newPriority.indexOf("high") >= 0) {
            thisTicket.toggleClass("border-red");
            thisTicket.find(".priorityLabel").toggleClass("red");
            thisTicket.find(".priorityLabel").html("<strong>HIGH</strong>");
        } else if (newPriority.indexOf("medium") >= 0) {
            thisTicket.toggleClass("border-yellow");
            thisTicket.find(".priorityLabel").toggleClass("yellow");
            thisTicket.find(".priorityLabel").html("<strong>MEDIUM</strong>");
        } else if (newPriority.indexOf("low") >= 0) {
            thisTicket.toggleClass("border-green");
            thisTicket.find(".priorityLabel").toggleClass("green");
            thisTicket.find(".priorityLabel").html("<strong>LOW</strong>");
        }

    });
});
