// _chartDataTooltips.js
// =====================
// Author: Dave Young
// Date created: April 14, 2015
// Summary: The tooltips for the data

var chartDataTooltips = function() {

    // -------------- INSTANTIATE MODULE ATTRIBUTES ---------------- // 
    var div = undefined;
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    var init = function(settings) {
        // console.log('init function triggered' for chartDataTooltips);

        return {
            div: _tooltipDiv(),
            tooltipContents: settings.tooltipContents,
            datapoints: _get_hoverpoints(settings),
            id: settings.id,
            color: settings.color,
            shape: settings.shape,
            attrs: _get_hoverpoint_attrs(settings),
            data: settings.data
        }
    }

    var update_attributes_via_json = function(settings) {
            // console.log('attributes function triggered for chartDataTooltips');
            // xt-set-setting-if-defined
        }
        // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    var _tooltipDiv = function() {
        // console.log('_tooltipDiv function triggered');
        var div = d3.select("body").append("div")
            .attr("class", "tooltip-data")
            .style("opacity", 0);
        return div
    }

    var _get_hoverpoints = function(settings) {
        // console.log('_get_hoverpoints function triggered');
        // Create a path to add to the chart

        // Add the scatterplot
        hoverpoints = {
            x: function(d) {
                return settings.axes.x1(d[settings.x1Values]);
            },
            y: function(d) {
                return settings.axes.y1(d[settings.y1Values]);
            },
            tooltip: function(d) {
                return d['tooltip'];
            }
        }
        return hoverpoints
    }

    var _get_hoverpoint_attrs = function(settings) {
        var attrs = {}
        if (settings.shape == "circle") {
            attrs = {
                radius: settings.radius
            }
        }
        return attrs
    }

    // xt-function-as-named-variable

    //--- REVEAL PUBLIC POINTERS TO PRIVATE METHODS AND ATTRIBUTES ---//
    return {
        init: init,
        update_attributes: update_attributes_via_json
            // xt-public-pointers
    };

};
