$(function() {
    $("select#sortBy").change(function(event) {
        var form = $("#ticketTableSortingForm");
        $("input#sortDesc").attr("value", "False");
        form.submit();
    })
    $("button#sortDescendingButton").bind("click", function(event) {
        var form = $("#ticketTableSortingForm");
        $("input#sortDesc").attr("value", "True");
        form.submit();
    });
    $("button#sortAscendingButton").bind("click", function(event) {
        var form = $("#ticketTableSortingForm");
        $("input#sortDesc").attr("value", "False");
        form.submit();
    });
});
