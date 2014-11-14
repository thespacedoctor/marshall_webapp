// _no_project_status_selection_form.js
// ====================================
// Author: Dave Young
// Date created: August 12, 2014
// Summary: Post to a URL in background to change the project status of a markdown wiki page, and hide the row

// xjs-ready-event-function 
// xjs-get-json-response-from-python-script

var _no_project_status_selection_form = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var selectionLink = $("a.projectStatus");
    // xt-initialise-variable

    selectionLink.bind("click", function(event) {
        var row = $(this).closest("tr");
        fade_and_hide(row);
    });

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
