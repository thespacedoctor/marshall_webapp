// plot_lightcurves.js
// ====================
// Author: Dave Young
// Date created: March 20, 2015
// Summary: The Lightcurve plot code

var transientLightcurve = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable

    // -------------- Public Methods ---------------- //
    var plot = function(chartDataUrl, canvas, axes) {
            console.log('plot function triggered');
            d3.json(chartDataUrl, function(lightcurveData) {
                alert(lightcurveData.chartAttributes.title);
            });
        }
        // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        plot: plot
            // xt-public-pointers
    };

})();

var plot_lightcurves = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable

    // be careful with variable names for items went compiling JS
    $("svg[chartType='lightcurve']").each(function(index, thisSvg) {
        // grab chart url
        var chartDataUrl = $(thisSvg).attr("data-src");
        // Select the canvas element
        var canvas = chartCanvas.set_canvas_element(thisSvg);
        // Initialise Axes object from canvas dimensions
        var axes = chartAxes.initialise_axes_for_chart(canvas);
        transientLightcurve.plot(chartDataUrl, canvas, axes);

    });

    // {
    //     alert(allSvgs[i].attr("data-src"));
    //     
    //     
    //     // Initialise Axes object from canvas dimensions
    //     var axes = chartAxes.initialise_axes_for_chart(canvas);

    // }

    // -------------- Public Methods ---------------- //
    // xt-update-object-settings-method

    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    // xt-function-as-named-variable

})();
