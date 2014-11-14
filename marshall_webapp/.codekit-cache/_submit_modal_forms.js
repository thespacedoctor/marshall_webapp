// _submit_modal_forms.js
// ======================
// Author: Dave Young
// Date created: July 2, 2014
// Summary: The buttons on my modal forms at in the footer of the modal, and therefore seperated from the actual form. This util associates the submit button with the form

// xjs-ready-event-function
// xjs-get-json-response-from-python-script

var submit_modal_forms = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var submitButton = $("button[formId]");
    // console.log('submit button: ' + submitButton.html());

    var submitForm = undefined;
    var formId = undefined;

    submitButton.bind("click", function(event) {
        formId = $(this).attr("formId");
        submitForm = $("#" + formId);
        submitForm.submit();
    });

    // xt-initialise-variable

    // -------------- Public Methods ---------------- //
    // xt-update-object-settings-method
    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        // xt-public-pointers
    };

})();
