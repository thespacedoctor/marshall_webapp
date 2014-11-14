$(function() {
    $(document.body).on("click", "button.generateOBSubmitButton", function() {
        var modalId = $(this).attr("id");
        setTimeout(function() {
            modalId = "#" + modalId;
            $(modalId).modal('hide');
            $(this).off();
        }, 500);
    });

});
