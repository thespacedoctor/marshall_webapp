// _chartAxes.js
// =============
// Author: Dave Young
// Date created: June 11, 2014
// Summary: Use this module to setup axes for your plots - first setup the canvas using the `chartCanvas` module and use the new canvas to determine the dimensions of the axes required using `initialise_axes_for_chart`
//          Once the axes have been created, add them to the canvas using the `chartCanvas` object methods

var chartAxes = function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var chartObject = undefined;
    var canvasWidth = undefined;
    var canvasHeight = undefined;
    var x1GridLines = undefined;
    var y1GridLines = undefined;
    var x1LabelsRotate = undefined;
    var y1LabelsRotate = undefined;
    var x1TickFormat = undefined;
    var y1TickFormat = undefined;
    var x1 = undefined;
    var y1 = undefined;
    var x2LabelsRotate = undefined;
    var y2LabelsRotate = undefined;
    var x2TickFormat = undefined;
    var y2TickFormat = undefined;
    var x2 = undefined;
    var y2 = undefined;
    var x1TickSize = 1;
    var x2TickSize = 1;
    var xy1TickSize = 1;
    var y2TickSize = 1;
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    var initialise_axes_for_chart = function(aChartObject) {
        // console.log('initialise_axes_for_chart function triggered');

        chartObject = aChartObject;

        return {
            y1: get_y1(),
            x1: get_x1(),
            y1Axis: _get_y1_axis(),
            x1Axis: _get_x1_axis(),
            y1Gridlines: _get_y1_grid_lines(),
            x1Gridlines: _get_x1_grid_lines(),
            x1LabelsRotate: x1LabelsRotate,
            y1LabelsRotate: y1LabelsRotate,
            y2: get_y2(),
            x2: get_x2(),
            y2Axis: _get_y2_axis(),
            x2Axis: _get_x2_axis(),
            y2Gridlines: _get_y2_grid_lines(),
            x2Gridlines: _get_x2_grid_lines(),
            x2LabelsRotate: x2LabelsRotate,
            y2LabelsRotate: y2LabelsRotate,
            update_settings: update_axes_settings_via_json
        };
    }

    var get_x1 = function() {
        // console.log('_getX function triggered');
        x1 = d3.time.scale().range([0, chartObject.width]);
        return x1
    }

    var get_y1 = function() {
        // console.log('get_y function triggered');
        y1 = d3.scale.linear().range([chartObject.height, 0]);
        return y1
    }

    var get_x2 = function() {
        // console.log('_getX function triggered');
        x2 = d3.time.scale().range([0, chartObject.width]);
        return x2
    }

    var get_y2 = function() {
        // console.log('get_y function triggered');
        y2 = d3.scale.linear().range([chartObject.height, 0]);
        return y2
    }

    var update_axes_settings_via_json = function(settings) {
        // console.log('update_axes_settings_via_json function triggered');
        if (settings.x1Range !== undefined) {
            _set_x1_range(settings.x1Range);
        }
        if (settings.y1Range !== undefined) {
            _set_y1_range(settings.y1Range);
        }
        if (settings.x1Title !== undefined) {
            _set_x1_title(settings.x1Title);
        }
        if (settings.y1Title !== undefined) {
            _set_y1_title(settings.y1Title);
        }
        if (settings.x1LabelsRotate !== undefined) {
            settings.axes.x1LabelsRotate = +settings.x1LabelsRotate
        }
        if (settings.y1LabelsRotate !== undefined) {
            settings.axes.y1LabelsRotate = +settings.y1LabelsRotate
        }
        if (settings.y1TickFormat !== undefined) {
            settings.axes.y1Axis.tickFormat(settings.y1TickFormat);
        }
        if (settings.x1TickFormat !== undefined) {
            settings.axes.x1Axis.tickFormat(settings.x1TickFormat);
        }

        if (settings.x2Range !== undefined) {
            _set_x2_range(settings.x2Range);
        }
        if (settings.y2Range !== undefined) {
            _set_y2_range(settings.y2Range);
        }
        if (settings.x2Title !== undefined) {
            _set_x2_title(settings.x2Title);
        }
        if (settings.y2Title !== undefined) {
            _set_y2_title(settings.y2Title);
        }
        if (settings.x2LabelsRotate !== undefined) {
            settings.axes.x2LabelsRotate = +settings.x2LabelsRotate;
        }
        if (settings.y2LabelsRotate !== undefined) {
            settings.axes.y2LabelsRotate = +settings.y2LabelsRotate
        }
        if (settings.y2TickFormat !== undefined) {
            settings.axes.y2Axis.tickFormat(settings.y2TickFormat);
        }
        if (settings.x2TickFormat !== undefined) {
            settings.axes.x2Axis.tickFormat(settings.x2TickFormat);
        }

        if (settings.x1TickSize !== undefined) {
            settings.axes.x1Axis.tickSize(-settings.x1TickSize);
        }
        if (settings.x2TickSize !== undefined) {
            settings.axes.x2Axis.tickSize(-settings.x2TickSize);
        }
        if (settings.y1TickSize !== undefined) {
            settings.axes.y1Axis.tickSize(-settings.y1TickSize);
        }
        if (settings.y2TickSize !== undefined) {
            settings.axes.y2Axis.tickSize(-settings.y2TickSize);
        }
        // xt-set-setting-if-defined
    }

    // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    var _set_x1_range = function(range) {
        x1.domain(range);
    }

    var _set_y1_range = function(range) {
        y1.domain(range);
    }

    var _set_x2_range = function(range) {
        x2.domain(range);
    }

    var _set_y2_range = function(range) {
        y2.domain(range);
    }

    var _set_x1_title = function(x1Title) {
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.x1Title",
            element_class: "text x1Title",
            extras: {
                attr: [{
                    attr: "x",
                    value: chartObject.width / 2
                }, {
                    attr: "y",
                    value: chartObject.height * 1.07
                }],
                text: [x1Title]
            },
            parent_element: chartObject.canvas,
            transform: undefined
        });
    }

    var _set_y1_title = function(y1Title) {
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.y1Title",
            element_class: "text y1Title",
            extras: {
                attr: [{
                    attr: "x",
                    value: 0 - (chartObject.height / 2)
                }, {
                    attr: "y",
                    value: 0 - chartObject.width * 0.07
                }, {
                    attr: "dy",
                    value: "0em"
                }, {
                    attr: "dx",
                    value: "-3em"
                }],
                text: [y1Title]
            },
            parent_element: chartObject.canvas,
            transform: "rotate(-90)"
        });
    }

    var _set_x2_title = function(x2Title) {
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.x2Title",
            element_class: "text x2Title",
            extras: {
                attr: [{
                    attr: "x",
                    value: chartObject.width / 2
                }, {
                    attr: "y",
                    value: chartObject.height * 1.15
                }],
                text: [x1Title]
            },
            parent_element: chartObject.canvas,
            transform: undefined
        });
    }

    var _set_y2_title = function(y2Title) {
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.y2Title",
            element_class: "text y2Title",
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
                text: [y1Title]
            },
            parent_element: chartObject.canvas,
            transform: "rotate(-90)"
        });
    }

    var _get_x1_axis = function() {
        x1Axis = d3.svg.axis().scale(x1)
            .orient("bottom").ticks(5);
        return x1Axis
    }

    var _get_y1_axis = function() {
        y1Axis = d3.svg.axis().scale(y1)
            .orient("left").ticks(5);
        return y1Axis
    }

    var _get_x2_axis = function() {
        x2Axis = d3.svg.axis().scale(x2)
            .orient("top").ticks(5);
        return x2Axis
    }

    var _get_y2_axis = function() {
        y2Axis = d3.svg.axis().scale(y2)
            .orient("right").ticks(5);
        return y2Axis
    }

    var _get_x1_grid_lines = function() {
        x1GridLines = d3.svg.axis().scale(x1)
            .orient("bottom").ticks(5)
            .tickSize(-chartObject.height, 0, 0)
            .tickFormat("")
        return x1GridLines
    }

    var _get_y1_grid_lines = function() {
        y1GridLines = d3.svg.axis().scale(y1)
            .orient("left").ticks(5)
            .tickSize(-chartObject.width, 0, 0)
            .tickFormat("")

        return y1GridLines
    }

    var _get_x2_grid_lines = function() {
        x2GridLines = d3.svg.axis().scale(x2)
            .orient("top").ticks(5)
            .tickSize(-chartObject.height, 0, 0)
            .tickFormat("")
        return x2GridLines
    }

    var _get_y2_grid_lines = function() {
        y2GridLines = d3.svg.axis().scale(y2)
            .orient("right").ticks(5)
            .tickSize(-chartObject.width, 0, 0)
            .tickFormat("")

        return y2GridLines
    }

    // xt-function-as-named-variable

    //--- REVEAL PUBLIC POINTERS TO PRIVATE METHODS AND ATTRIBUTES ---//
    return {
        initialise_axes_for_chart: initialise_axes_for_chart
            // xt-public-pointers
    };

};
