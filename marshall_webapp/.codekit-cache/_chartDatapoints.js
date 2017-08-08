// _chartDatapoints.js
// ===================
// Author: Dave Young
// Date created: March 24, 2015
// Summary: Create a datapoint set to be added to the chart canvas

var chartDatapoints = function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var settings = null;
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    var init = function(settings) {
        // console.log('init function triggered for chartDatapoints');

        // xt-set-setting-if-defined
        return {
            datapoints: _get_datapoints(settings),
            id: settings.id,
            color: settings.color,
            shape: settings.shape,
            attrs: _get_datapoint_attrs(settings),
            data: settings.data
        }
    }

    //     svgElement.selectAll("dot").data(data).enter().append("circle").attr("r", 3.5).attr("cx", function(d) {
    //     return x(d.magnitude);
    // }).attr("cy", function(d) {
    //     return y(d.observationDate);
    // });

    var update_settings_via_json = function(settings) {
        // console.log('update_settings_via_json function triggered');
        // xt-set-setting-if-defined
    }

    var _get_datapoints = function(settings) {
        // console.log('_get_datapoints function triggered');
        // Create a path to add to the chart

        // Add the scatterplot
        datapoints = {
            x: function(d) {
                return settings.axes.x1(d[settings.x1Values]);
            },
            y: function(d) {
                return settings.axes.y1(d[settings.y1Values]);
            }
        }

        return datapoints
    }

    var _get_datapoint_attrs = function(settings) {
        var attrs = {}
        if (settings.shape == "circle") {
            attrs = {
                radius: settings.radius
            }
        }
        return attrs
    }

    // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        init: init,
        update_settings: update_settings_via_json
            // xt-public-pointers
    };

};
