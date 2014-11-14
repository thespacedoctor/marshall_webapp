$(function() {
    $(".classificationForm").on("change", "select#clsClassificationWRTMax", function() {
        var classPhase = $(this).val();
        var phaseInput = $(this).closest("form").find("#clsClassificationPhase");
        var prepend = phaseInput.closest("div.input-prepend").find("span.add-on");
        if (classPhase == "post-max" || classPhase == "pre-max") {
            phaseInput.removeAttr('disabled');
            if (classPhase == "post-max") {
                prepend.html("+");
            } else {
                prepend.html("-");
            }
        } else {
            var phaseInput = $(this).closest("form").find("#clsClassificationPhase");
            phaseInput.attr('disabled', true);
            prepend.html("?");
        }
    });

});

// Function above repeated for Pyramid version of the marshall classification form
$(function() {
    $(".classificationForm").on("change", "select[name='clsClassificationWRTMax']", function() {
        var classPhase = $(this).val();
        var phaseInput = $(this).closest("form").find("input[name='clsClassificationPhase']");
        var prepend = phaseInput.closest("div.input-prepend").find("span.add-on");
        if (classPhase == "post-max" || classPhase == "pre-max") {
            phaseInput.removeAttr('disabled');
            if (classPhase == "post-max") {
                prepend.html("+");
            } else {
                prepend.html("-");
            }
        } else {
            phaseInput.attr('disabled', true);
            if (classPhase == "at-max") {
                prepend.html("");
            } else {
                prepend.html("?");
            }
        }
    });
});

$(function() {
    $(".classificationForm").on("change", "select[name='clsType']", function() {
        var clsType = $(this).val();
        var clsSnClassification = $(this).closest("form").find("select[name='clsSnClassification']");
        var clsPeculiar = $(this).closest("form").find("input[name='clsPeculiar']");

        if (clsType == "supernova") {
            clsSnClassification.removeAttr('disabled');
            clsPeculiar.removeAttr('disabled');
        } else {
            clsSnClassification.attr('disabled', true);
            clsPeculiar.attr('disabled', true);
        }
    });
});
