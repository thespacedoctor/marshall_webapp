// _chartAxes.js
// =============
// Author: Dave Young
// Date created: June 11, 2014
// Summary: Use this module to setup axes for your plots - first setup the canvas using the `chartCanvas` module and use the new canvas to determine the dimensions of the axes required using `initialise_axes_for_chart`
//          Once the axes have been created, add them to the canvas using the `chartCanvas` object methods

var chartAxes = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var chartObject = undefined;
    var canvasWidth = undefined;
    var canvasHeight = undefined;
    var xGridLines = undefined;
    var yGridLines = undefined;
    var xLabelsRotate = undefined;
    var yLabelsRotate = undefined;
    var xTickFormat = undefined;
    var yTickFormat = undefined;
    var x = undefined;
    var y = undefined;
    // xt-initialise-variable

    // -------------- Public Methods ---------------- //
    var initialise_axes_for_chart = function(aChartObject) {
        // console.log('initialise_axes_for_chart function triggered');

        chartObject = aChartObject;

        return {
            y: get_y(),
            x: get_x(),
            yAxis: _get_y_axis(),
            xAxis: _get_x_axis(),
            yGridlines: _get_y_grid_lines(),
            xGridlines: _get_x_grid_lines(),
            xLabelsRotate: xLabelsRotate,
            yLabelsRotate: yLabelsRotate,
            update_settings: update_axes_settings_via_json
        };
    }

    var get_x = function() {
        // console.log('_getX function triggered');
        x = d3.time.scale().range([0, chartObject.width]);
        return x
    }

    var get_y = function() {
        // console.log('get_y function triggered');
        y = d3.scale.linear().range([chartObject.height, 0]);
        return y
    }

    var update_axes_settings_via_json = function(settings) {
        // console.log('update_axes_settings_via_json function triggered');
        if (settings.xRange !== undefined) {
            _set_x_range(settings.xRange);
        }
        if (settings.yRange !== undefined) {
            _set_y_range(settings.yRange);
        }
        if (settings.xTitle !== undefined) {
            _set_x_title(settings.xTitle);
        }
        if (settings.yTitle !== undefined) {
            _set_y_title(settings.yTitle);
        }
        if (settings.xLabelsRotate !== undefined) {
            settings.axes.xLabelsRotate = +settings.xLabelsRotate
        }
        if (settings.yLabelsRotate !== undefined) {
            settings.axes.yLabelsRotate = +settings.yLabelsRotate
        }
        if (settings.yTickFormat !== undefined) {
            settings.axes.yAxis.tickFormat(settings.yTickFormat);
        }
        if (settings.xTickFormat !== undefined) {
            settings.axes.xAxis.tickFormat(settings.xTickFormat);
        }
        // xt-set-setting-if-defined
    }

    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    var _set_x_range = function(range) {
        // console.log('__set_x_range function triggered');
        // console.log('changing x range: ' + x.domain(range));

        x.domain(range);
        // console.log("_set_x_range:" + range);
    }

    var _set_y_range = function(range) {
        // console.log('_set_y_range function triggered');
        y.domain(range);
        // console.log("_set_y_range:" + range);
    }

    var _set_x_title = function(xTitle) {
        // console.log('_set_x_title function triggered');
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.xTitle",
            element_class: "text xTitle",
            extras: {
                attr: [{
                    attr: "x",
                    value: chartObject.width / 2
                }, {
                    attr: "y",
                    value: chartObject.height * 1.15
                }],
                text: [xTitle]
            },
            parent_element: chartObject.canvas,
            transform: undefined
        });

    }

    var _set_y_title = function(yTitle) {
        // console.log('_set_x_title function triggered');
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.yTitle",
            element_class: "text yTitle",
            extras: {
                attr: [{
                    attr: "x",
                    value: 0 - (chartObject.height / 2)
                }, {
                    attr: "y",
                    value: 0 - chartObject.width * 0.07
                }, {
                    attr: "dy",
                    value: "1em"
                }],
                text: [yTitle]
            },
            parent_element: chartObject.canvas,
            transform: "rotate(-90)"
        });
    }

    var _get_x_axis = function() {
        // console.log('_getXAis function triggered');
        xAxis = d3.svg.axis().scale(x)
            .orient("bottom").ticks(5);
        return xAxis
    }

    var _get_y_axis = function() {
        // console.log('_get_y_axis function triggered');
        yAxis = d3.svg.axis().scale(y)
            .orient("left").ticks(5);
        return yAxis
    }

    var _get_x_grid_lines = function() {
        // console.log('_get_x_grid_lines function triggered');
        xGridLines = d3.svg.axis().scale(x)
            .orient("bottom").ticks(5)
            .tickSize(-chartObject.height, 0, 0)
            .tickFormat("")
        return xGridLines
    }

    var _get_y_grid_lines = function() {
        // console.log('_get_y_grid_lines function triggered');
        yGridLines = d3.svg.axis().scale(y)
            .orient("left").ticks(5)
            .tickSize(-chartObject.width, 0, 0)
            .tickFormat("")

        return yGridLines
    }

    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        initialise_axes_for_chart: initialise_axes_for_chart
        // xt-public-pointers
    };

})();
