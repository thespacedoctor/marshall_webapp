// _chartPath.js
// =============
// Author: Dave Young
// Date created: June 11, 2014
// Summary: Chart Line Based on the chartData object

// xjs-ready-event-function
// xjs-get-json-response-from-python-script

var chartPath = function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var settings = null;
    var area = null;
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    var initialise_path_for_chart = function(settings) {
        // console.log('initialise_path_for_chart function triggered');

        // console.log('settings.x1Values: ' + settings.x1Values);

        // xt-set-setting-if-defined
        if (settings.area) {
            area = _get_area(settings);
        } else {
            area = undefined;
        }

        return {
            line: _get_valueline(settings),
            area: area,
            x1Values: settings.x1Values,
            y1Values: settings.y1Values,
            id: settings.id,
            color: settings.color,
            htmlclass: settings.htmlclass,
        }
    }

    var update_line_settings_via_json = function(settings) {
        // console.log('update_line_settings_via_json function triggered');
        // xt-set-setting-if-defined
    }

    var _get_valueline = function(settings) {
        // console.log('_get_valueline function triggered');
        // Create a path to add to the chart
        valueline = d3.svg.line()
            .interpolate("basis")
            .x(function(d) {
                return settings.axes.x1(d[settings.x1Values]);
            })
            .y(function(d) {
                return settings.axes.y1(d[settings.y1Values]);
            });
        return valueline
    }

    var _get_area = function(settings) {
        // console.log('_get_area function triggered');
        area = d3.svg.area()
            .interpolate("basis")
            .x(function(d) {
                return settings.axes.x1(d[settings.x1Values]);
            })
            .y0(settings.chart.height)
            .y1(function(d) {
                return settings.axes.y1(d[settings.y1Values]);
            });
        return area
    }

    // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        initialise_path: initialise_path_for_chart
            // xt-public-pointers
    };

};
