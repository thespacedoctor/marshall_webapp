// _chartCanvas.js
// ===============
// Author: Dave Young
// Date created: June 11, 2014  
// Summary: This is a module to setup and manipulate a d3 chart canvas.
//          In your code the canvas should first be created using `set_canvas_element` and then elements added to the canvas using the various set and add methods
//

var chartCanvas = function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var x1Axis = null;
    var y1Axis = null;
    var canvasElement = null;
    var canvasWidth = null;
    var canvasHeight = null;
    var chartWidth = null;
    var chartHeight = null;
    var canvasString = null;
    var chart = null;
    var margin = {
        top: null,
        right: null,
        bottom: null,
        left: null
    }
    var canvasJQElement = null;
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    var set_canvas_element = function(aCanvasString) {

        // select the canvas element
        canvasString = aCanvasString
        canvasJQElement = $(canvasString);
        canvasElement = d3.select(canvasString);

        // grab the dimensions from HTML and CSS
        _set_canvas_dimensions(canvasElement, canvasJQElement);

        // setup the canvas element
        //   console.log('canvas width' + canvasJQElement.attr("width"));
        //   console.log('canvas height' + canvasJQElement.attr("height"));

        canvasElement = canvasElement
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")")

        // rel="tooltip" data-container="body" data-placement="right" data-trigger="hover" data-original-title="move object to another list" data-delay="200" data-toggle="dropdown"
        // console.log("canvas element has been set");

        return {
            canvas: canvasElement,
            width: chartWidth,
            height: chartHeight,
            update_settings: update_settings_from_json_object
                // xt-key-and-value-in-json-object
        };
    }

    var update_settings_from_json_object = function(settings) {
        // console.log('update_settings_from_json_object function triggered');

        if (settings.axes !== undefined) {
            _set_x1_gridlines(settings.axes.x1Gridlines);
            _set_y1_gridlines(settings.axes.y1Gridlines);
        }

        if (settings.axes !== undefined) {
            _set_x1_axis(settings.axes);
            _set_y1_axis(settings.axes);
            _set_x2_axis(settings.axes);
            _set_y2_axis(settings.axes);
        }

        if (settings.dataline !== undefined && settings.dataline.dataline !== undefined) {
            if (settings.dataline.dataline.line !== undefined) {
                _add_path(settings.dataline);
            }
        }
        if (settings.dataline !== undefined && settings.dataline.dataline !== undefined) {
            if (settings.dataline.dataline.area !== undefined) {
                _add_area(settings.dataline);
            }
        }

        if (settings.chartTitle !== undefined) {
            _set_title(settings.chartTitle);
        }
        if (settings.datapoints !== undefined) {
            _add_datapoints(settings.datapoints);
        }

        if (settings.errorBars !== undefined) {
            _add_errorbars(settings.errorBars);
        }

        if (settings.tooltips !== undefined) {
            _add_tooltips(settings.tooltips);
        }

        // xt-set-setting-if-defined
        return {
            canvas: canvasElement,
            width: chartWidth,
            height: chartHeight,
            update_settings: update_settings_from_json_object
                // xt-key-and-value-in-json-object
        };
    }

    // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    var _set_x1_axis = function(axes) {
        // console.log('_set_x1_axis function triggered');

        update_chart_element.update({
            element_type: "g",
            element_selector: "g.x1axis",
            element_class: "x1axis axis",
            element_call: axes.x1Axis,
            parent_element: canvasElement,
            transform: "translate(0," + _get_chart_height() + ")"
        });

        if (axes.x1LabelsRotate !== undefined) {
            canvasElement.select("g.x1axis").selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.5em")
                .attr("dy", ".2em")
                .attr("transform", function(d) {
                    return "rotate(" + axes.x1LabelsRotate + ")"
                });
        } else {
            canvasElement.select("g.x1axis").selectAll("text").attr("dy", "1em");
        }

    }

    var _set_x2_axis = function(axes) {
        // console.log('_set_x2_axis function triggered');
        if (axes.x2Axis == undefined) {
            return
        }
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.x2axis",
            element_class: "x2axis axis",
            element_call: axes.x2Axis,
            parent_element: canvasElement,
            transform: "translate(0,0)"
        });

        if (axes.x2LabelsRotate !== undefined) {
            canvasElement.select("g.x2axis").selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.8em")
                .attr("dy", ".15em")
                .attr("transform", function(d) {
                    return "rotate(" + axes.x2LabelsRotate + ")"
                });
        } else {
            canvasElement.select("g.x2axis").selectAll("text").attr("dy", "-.4em")
        }

    }

    var _set_y1_axis = function(axes) {
        // console.log('_set_x1_axis function triggered');
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.y1axis",
            element_class: "y1axis axis",
            element_call: axes.y1Axis,
            parent_element: canvasElement,
            update_if: (axes.dataline !== undefined)
        });

        if (axes.y1LabelsRotate !== undefined && axes.y1LabelsRotate !== 0) {
            canvasElement.select("g.y1axis").selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.1em")
                .attr("dy", ".7em")
                .attr("transform", function(d) {
                    return "rotate(" + axes.y1LabelsRotate + ")"
                });
        } else {
            canvasElement.select("g.y1axis").selectAll("text").attr("dx", "-.1em");
        }
    }

    var _set_y2_axis = function(axes) {
        if (axes.y2Axis == undefined) {
            return
        }
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.y2axis",
            element_class: "y2axis axis",
            element_call: axes.y2Axis,
            parent_element: canvasElement,
            update_if: (axes.dataline !== undefined),
            transform: "translate(" + _get_chart_width() + ",0)"
        });

        if (axes.y2LabelsRotate !== undefined && axes.y1LabelsRotate !== 0) {
            canvasElement.select("g.y2axis").selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.1em")
                .attr("dy", ".7em")
                .attr("transform", function(d) {
                    return "rotate(" + axes.y2LabelsRotate + ")"
                });
        } else {
            canvasElement.select("g.y2axis").selectAll("text").attr("dx", "+.1em");
        }
    }

    var _set_x1_gridlines = function(x1Gridlines) {
        // console.log('_set_x1_gridlines function triggered');
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.x1grid",
            element_class: "grid x1grid",
            element_call: x1Gridlines,
            parent_element: canvasElement,
            transform: "translate(0," + _get_chart_height() + ")",
            update_if: true
        });

    }

    var _set_y1_gridlines = function(y1Gridline) {
        // console.log('_set_y1_gridlines function triggered');
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.y1grid",
            element_class: "grid y1grid",
            element_call: y1Gridline,
            parent_element: canvasElement,
            transform: undefined,
            update_if: true
        });

    }

    var _add_path = function(dataline) {
        update_chart_element.update({
            element_type: "path",
            element_selector: "path#line" + dataline.dataline.id,
            element_class: "line " + dataline.dataline.color,
            element_id: "line" + dataline.dataline.id,
            element_call: undefined,
            element_data: {
                data: dataline.data,
                attr: dataline.dataline.line
            },
            parent_element: canvasElement,
            transform: undefined
                // remove_if: true
        });

    }

    var _add_area = function(dataline) {
        // console.log('_add_area function triggered');

        update_chart_element.update({
            element_type: "path",
            element_selector: "path#area" + dataline.dataline.id,
            element_class: "area " + dataline.dataline.color,
            element_id: "area" + dataline.dataline.id,
            element_call: undefined,
            element_data: {
                data: dataline.data,
                attr: dataline.dataline.area
            },
            parent_element: canvasElement,
            transform: undefined
                // remove_if: true
        });
    }

    // xt-function-as-named-variable

    var _set_title = function(chartTitle) {
        // console.log('_set_title function triggered');
        update_chart_element.update({
            element_type: "text",
            element_selector: "text.chartTitle",
            element_class: "text chartTitle",
            extras: {
                attr: [{
                    attr: "x",
                    value: (canvasWidth / 3.)
                }, {
                    attr: "y",
                    value: 0 - (margin.top / 2)
                }],
                text: [chartTitle]
            },
            parent_element: canvasElement,
            transform: undefined
        });
    }

    var _set_canvas_dimensions = function(canvasElement, canvasJQElement) {
        // FUNCTION TO SET THE CANVAS SIZE, THE MARGINS AND THE CHART DIMENSIONS

        // console.log('setCanvasDimensions function triggered');
        canvasWidth = canvasJQElement.width();
        canvasElement.attr("width", canvasWidth);

        // IF HEIGHT = SQUARE IN HTML THEN MAKE HEIGHT == WIDTH
        if (canvasElement.classed("square", true)) {
            canvasHeight = canvasWidth;
        } else {
            canvasHeight = canvasJQElement.height();
        }
        canvasElement.attr("height", canvasHeight);

        margin.top = canvasHeight * 0.1;
        margin.bottom = canvasHeight * 0.2;
        margin.left = canvasWidth * 0.1;
        margin.right = canvasWidth * 0.1;
        chartWidth = _get_chart_width();
        chartHeight = _get_chart_height();
    }

    var _get_chart_width = function() {
        chartWidth = canvasWidth - margin.left - margin.right;
        return chartWidth
    }

    var _get_chart_height = function() {
        chartHeight = canvasHeight - margin.top - margin.bottom;
        return chartHeight
    }

    var _set_axes = function(aAxes) {
        // console.log('_set_axes function triggered');
        _set_x1_axis(aAxes.x1Axis);
        _set_y1_axis(aAxes.y1Axis);
        _set_x1_gridlines(aAxes.x1Gridlines);
        _set_y1_gridlines(aAxes.y1Gridlines);
    }

    var _add_datapoints = function(datapoints) {
        datapoints = datapoints.datapoints

        //   console.log('_add_datapoints function triggered');
        update_chart_element.update({
            element_selector: "datapoint",
            element_class: "datapoint " + datapoints.color,
            element_id: "datapoint" + datapoints.id,
            element_data: {
                datapoints: datapoints
            },
            element_call: undefined,
            parent_element: canvasElement,
            transform: undefined,
            parent_element: canvasElement,
            transform: undefined
        });

    }

    var _add_errorbars = function(errorBars) {
        // console.log('_add_errorbars function triggered');

        // be careful with variable names for items went compiling JS
        var array = errorBars.data;
        for (i = 0; i < array.length; i++) {
            var item = array[i];

            //console.log('item: ' + JSON.stringify(item));

            update_chart_element.update({
                element_type: "path",
                element_selector: "path#line" + errorBars.line.id,
                element_class: "line " + errorBars.line.color + " " + errorBars.line.htmlclass,
                element_id: "line" + errorBars.line.id,
                element_call: undefined,
                element_data: {
                    data: item,
                    attr: errorBars.line.line
                },
                parent_element: canvasElement,
                transform: undefined
                    // remove_if: true
            });

        }

    }

    var _add_tooltips = function(tooltips) {
        // console.log('_add_tooltips function triggered');

        // console.log('tooltips.data: ' + JSON.stringify(tooltips.data));

        //   console.log('_add_datapoints function triggered');
        update_chart_element.update({
            element_selector: "tooltips",
            element_class: "tooltips " + tooltips.color,
            element_id: "tooltips" + tooltips.id,
            element_data: {
                tooltips: tooltips
            },
            element_call: undefined,
            parent_element: canvasElement,
            transform: undefined,
            parent_element: canvasElement,
            transform: undefined
        });

    }

    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        set_canvas_element: set_canvas_element
            // xt-public-pointers
    };

};

// var valueline = d3.svg.line()
//     .x(function(d) {
//         return x(d.date);
//     })
//     .y(function(d) {
//         return y(d.close);
//     });
