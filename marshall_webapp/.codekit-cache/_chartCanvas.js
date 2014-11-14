// _chartCanvas.js
// ===============
// Author: Dave Young
// Date created: June 11, 2014  
// Summary: This is a module to setup and manipulate a d3 chart canvas.
//          In your code the canvas should first be created using `set_canvas_element` and then elements added to the canvas using the various set and add methods
//

var chartCanvas = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var xAxis = null;
    var yAxis = null;
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

    // -------------- Public Methods ---------------- //
    var set_canvas_element = function(aCanvasString) {

        // select the canvas element
        canvasString = aCanvasString
        canvasJQElement = $(canvasString);
        canvasElement = d3.select(canvasString);

        // grab the dimensions from HTML and CSS
        _set_canvas_dimensions(canvasElement, canvasJQElement);

        // setup the canvas element
        // console.log('here width' + canvasElement.attr("width"));
        // console.log('here width' + canvasElement.attr("height"));

        canvasElement = canvasElement
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");
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
            _set_x_axis(settings.axes);
            _set_y_axis(settings.axes);
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
        if (settings.axes !== undefined) {
            _set_x_gridlines(settings.axes.xGridlines);
            _set_y_gridlines(settings.axes.yGridlines);
        }
        if (settings.chartTitle !== undefined) {
            _set_title(settings.chartTitle);
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

    // -------------- Private Helper Methods ---------------- //
    var _set_x_axis = function(axes) {
        // console.log('_set_x_axis function triggered');

        update_chart_element.update({
            element_type: "g",
            element_selector: "g.xaxis",
            element_class: "xaxis axis",
            element_call: axes.xAxis,
            parent_element: canvasElement,
            transform: "translate(0," + _get_chart_height() + ")"
        });

        if (axes.xLabelsRotate !== undefined) {
            canvasElement.select("g.xaxis").selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.8em")
                .attr("dy", ".15em")
                .attr("transform", function(d) {
                    return "rotate(" + axes.xLabelsRotate + ")"
                });
        }

    }

    var _set_y_axis = function(axes) {
        // console.log('_set_x_axis function triggered');
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.yaxis",
            element_class: "yaxis axis",
            element_call: axes.yAxis,
            parent_element: canvasElement,
            update_if: (axes.dataline !== undefined)
        });

        if (axes.yLabelsRotate !== undefined) {
            canvasElement.select("g.yaxis").selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.1em")
                .attr("dy", ".7em")
                .attr("transform", function(d) {
                    return "rotate(" + axes.yLabelsRotate + ")"
                });
        }
    }

    var _set_x_gridlines = function(xGridlines) {
        // console.log('_set_x_gridlines function triggered');
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.xgrid",
            element_class: "grid xgrid",
            element_call: xGridlines,
            parent_element: canvasElement,
            transform: "translate(0," + _get_chart_height() + ")",
            update_if: true
        });

    }

    var _set_y_gridlines = function(yGridline) {
        // console.log('_set_y_gridlines function triggered');
        update_chart_element.update({
            element_type: "g",
            element_selector: "g.ygrid",
            element_class: "grid ygrid",
            element_call: yGridline,
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
        // console.log('setCanvasDimensions function triggered');
        canvasWidth = canvasJQElement.width();
        canvasElement.attr("width", canvasWidth);
        canvasHeight = canvasJQElement.height();
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
        _set_x_axis(aAxes.xAxis);
        _set_y_axis(aAxes.yAxis);
        _set_x_gridlines(aAxes.xGridlines);
        _set_y_gridlines(aAxes.yGridlines);
    }

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        set_canvas_element: set_canvas_element
        // xt-public-pointers
    };

})();

// var valueline = d3.svg.line()
//     .x(function(d) {
//         return x(d.date);
//     })
//     .y(function(d) {
//         return y(d.close);
//     });
