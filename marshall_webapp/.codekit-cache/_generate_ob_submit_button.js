$(function() {

    $(document.body).on("focusout", "input[name='currentMag']", function() {
        var x = $(this).val();
        if (x > 20.5) {
            alert("current magnitude must brighter than 20.5 mag");
            return false;
        }
    });

    $(document.body).on("click", "button.generateOBSubmitButton", function() {
        var modalId = $(this).attr("id");
        setTimeout(function() {
            modalId = "#" + modalId;
            $(modalId).modal('hide');
            $(this).off();
        }, 500);
    });

});
