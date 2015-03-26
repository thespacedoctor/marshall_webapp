// plot_lightcurves.js
// ====================
// Author: Dave Young
// Date created: March 20, 2015
// Summary: The Lightcurve plot code

var transientLightcurve = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var chartDataUrl = undefined;
    var axes = undefined;
    var canvas = undefined;
    // xt-initialise-variable

    var parseDate = d3.time.format("%Y-%m-%dt%H:%M:%S").parse;

    // -------------- Public Methods ---------------- //
    var init = function(thisSvg) {
        // console.log('plot function triggered');
        chartDataUrl = $(thisSvg).attr("data-src");
        // Select the canvas element
        canvas = chartCanvas.set_canvas_element(thisSvg);
        // Initialise Axes object from canvas dimensions
        axes = chartAxes.initialise_axes_for_chart(canvas);

    }

    var plot = function() {
        // console.log('plot function triggered');
        d3.json(chartDataUrl, function(lightcurveData) {
            data = lightcurveData.chartData;
            data.forEach(function(d) {
                observationDate = parseDate(d.observationDate);
                magnitude = +d.magnitude;
                observationMJD = +d.observationMJD;
            });

            // scale the axes data ranges according to the data
            xRange = d3.extent(data, function(d) {
                return d.observationDate;
            });

            yRange = [d3.max(data, function(d) {
                    return d.magnitude;
                }),
                d3.min(data, function(d) {
                    return d.magnitude;
                })
            ]

            // update the axes settings
            axes.update_settings({
                chartTitle: lightcurveData.chartData.title,
                axes: axes,
                xRange: xRange,
                yRange: yRange,
                xTitle: lightcurveData.chartData.x1Title,
                yTitle: lightcurveData.chartData.y1Title,
                xLabelsRotate: -65,
                yLabelsRotate: -15,
                xTickFormat: d3.time.format("%Y-%m-%dt%H:%M:%S"),
                yTickFormat: undefined
            });

            canvas.update_settings({
                chartTitle: lightcurveData.chartData.title,
                axes: axes,
                dataline: {}
            });
        });

    }

    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    var _parseDate = function(element) {
        console.log('_parseDate function triggered');

    }

    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        init: init,
        plot: plot
            // xt-public-pointers
    };

})();

var plot_lightcurves = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable

    // be careful with variable names for items went compiling JS
    $("svg[chartType='lightcurve']").each(function(index, thisSvg) {
        transientLightcurve.init(thisSvg);
        transientLightcurve.plot();
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
