$(function() {
    $(".classificationForm").on("change", "select#clsClassificationWRTMax", function() {
        var classPhase = $(this).val();
        var phaseInput = $(this).closest("form").find("#clsClassificationPhase");
        var prepend = phaseInput.closest("div.input-prepend").find("span.add-on");
        if (classPhase == "post-max" || classPhase == "pre-max") {
            phaseInput.removeAttr('disabled');
            if (classPhase == "post-max") {
                prepend.html("-");
            } else {
                prepend.html("+");
            }
        } else {
            var phaseInput = $(this).closest("form").find("#clsClassificationPhase");
            phaseInput.attr('disabled', true);
            prepend.html("?");
        }
    });

});
