// plot_lightcurves.js
// ====================
// Author: Dave Young
// Date created: March 20, 2015
// Summary: The Lightcurve plot code

var transientLightcurve = function() {

    // -------------- INSTANTIATE MODULE ATTRIBUTES ---------------- // 
    var chartDataUrl = undefined;
    var axes = undefined;
    var canvas = undefined;
    var dataLine = undefined;
    var svgElement = undefined;
    // xt-initialise-variable

    // -------------- USEFUL FUNCTIONS ------------------------ //
    var parseDate = d3.time.format("%Y-%m-%dT%H:%M:%S").parse;

    // -------------- PUBLIC METHODS ---------------- //
    var init = function(thisSvg) {
        // INITIATE ALL THE DEFAULT COMPONENTS REQUIRED FOR THE PLOT
        // console.log('plot function triggered');
        svgElement = d3.select(thisSvg);

        // FIRST SELECT THE CANVAS
        chartDataUrl = $(thisSvg).attr("data-src");
        canvas = new chartCanvas();
        canvas = canvas.set_canvas_element(thisSvg);

        // NOW INITIALISE AXES OBJECT FROM CANVAS DIMENSIONS
        axes = new chartAxes;
        axes = axes.initialise_axes_for_chart(canvas);

        return {};
    }

    var plot = function() {

        // console.log('plot function triggered');
        // CONVERT THE DATA FROM STRING TO THE CORRECT FORMAT
        d3.json(chartDataUrl, function(lightcurveData) {
            data = lightcurveData.chartData;
            data.forEach(function(d) {
                d.observationDate = parseDate(d.observationDate);
                d.magnitude = +d.magnitude;
                d.observationMJD = +d.observationMJD;
            });

            _update_axes(lightcurveData);
            _add_datapoints(data);
            _update_canvas(lightcurveData);

        });

    }

    // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    var _update_axes = function(lightcurveData) {
        // UPDATE THE AXES OF THE PLOT BASED ON THE DATA
        // console.log('_update_axes function triggered');

        // CALCULATE THE DATE SCALE FOR THE BOTTOM X AXIS
        var x1Max = d3.max(data, function(d) {
            return d.observationDate;
        })

        var x1Min = d3.min(data, function(d) {
            return d.observationDate;
        })

        // SET THE X1RANGE TO THE DEFAULT MINIMUM RANGE
        var dayDiff = (+x1Max - (+x1Min)) / (1000 * 60 * 60 * 24);
        if (dayDiff < 3.) {
            minX1range = 3.0 * 1000 * 60 * 60 * 24;
            var midDate = (+x1Max + (+x1Min)) / 2;
            //   console.log('midDate in millisec: ' + midDate);
            x1Max = midDate + minX1range / 2;
            x1Min = midDate - minX1range / 2;
            x1Max = new Date(x1Max);
            x1Min = new Date(x1Min);
        }

        x1Range = [x1Min, x1Max]
            // console.log('[x1Min, x1Max]: ' + x1Range);
            // console.log(typeof x1Max);

        // SET THE Y-RANGE (RESERVED FOR MAGNITUDES)
        var y1Max = d3.max(data, function(d) {
            return d.magnitude;
        })
        var y1Min = d3.min(data, function(d) {
            return d.magnitude;
        })

        y1Range = 3.
        if (y1Max - y1Min < y1Range) {
            var yMid = (y1Max + y1Min) / 2;
            y1Min = yMid - y1Range / 2.;
            y1Max = yMid + y1Range / 2.;
        }
        y1Range = [y1Min, y1Max]

        // UPDATE THE AXES SETTINGS
        axes.update_settings({
            chartTitle: lightcurveData.chartAttributes.title,
            axes: axes,
            x1Range: x1Range,
            y1Range: y1Range,
            x2Range: x1Range,
            y2Range: y1Range,
            x1Title: lightcurveData.chartAttributes.x1title,
            y1Title: lightcurveData.chartAttributes.y1title,
            x1LabelsRotate: undefined,
            y1LabelsRotate: undefined,
            x1TickFormat: d3.time.format("%Y-%m-%d"),
            y1TickFormat: undefined,
            x1TickSize: 6,
            y1TickSize: 6,
            x2TickSize: 6,
            y2TickSize: 6,
        });
    }

    var _update_canvas = function(lightcurveData) {
        //   console.log('_update_canvas function triggered');
        canvas.update_settings({
            chartTitle: lightcurveData.chartAttributes.title,
            axes: axes,
            dataline: {}
        });
    }

    var _add_datapoints = function(data, chartObject) {
        //   console.log('_add_datapoints function triggered');
        // AND THE DATALINE
        dataline = new chartPath();
        dataline = dataline.initialise_path({
            axes: axes,
            chart: canvas,
            x1Values: "observationDate",
            y1Values: "magnitude",
            color: "red",
            id: Math.floor((Math.random() * 10000) + 1).toString()
        });

        datapoints = new chartDatapoints();
        datapoints = datapoints.init({
            data: data,
            x1Values: "observationDate",
            y1Values: "magnitude",
            color: "red",
            id: Math.floor((Math.random() * 10000) + 1).toString(),
            shape: "circle",
            radius: 3.5,
            axes: axes
        });

        canvas.update_settings({
            dataline: {
                dataline: dataline,
                data: data
            },
            datapoints: {
                datapoints: datapoints
            }
        });
    }

    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        init: init,
        plot: plot
            // xt-public-pointers
    };

};

var plot_lightcurves = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable
    var plotArray = new Array();

    // be careful with variable names for items went compiling JS
    $("svg[chartType='lightcurve']").each(function(index, thisSvg) {
        var newPlot = new transientLightcurve();
        newPlot.init(thisSvg);
        newPlot.plot();
        plotArray.push(newPlot);
    });

    // {
    //     alert(allSvgs[i].attr("data-src"));
    //     
    //     
    //     // Initialise Axes object from canvas dimensions
    //     var axes = chartAxes.initialise_axes_for_chart(canvas);

    // }

    // -------------- PUBLIC METHODS ---------------- //
    // xt-update-object-settings-method

    // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    // xt-function-as-named-variable

})();
