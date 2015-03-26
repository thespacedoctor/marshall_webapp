// _chartData.js
// =============
// Author: Dave Young
// Date created: March 23, 2015
// Summary: Grab the data from the chartData attribute of the SVG element

// xjs-ready-event-function
// xjs-get-json-response-from-python-script

var chartData = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable

    // -------------- Public Methods ---------------- //
    // xt-update-object-settings-method
    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    var get = function(thisSvg) {
        console.log('get_data function triggered');
        chartDataUrl = $(thisSvg).attr("data-src");
        alert(chartDataUrl);
        return {};
    }

    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        get: get
            // xt-public-pointers
    };

})();
