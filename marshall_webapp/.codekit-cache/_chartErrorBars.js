// _chartErrorBars.js
// ==================
// Author: Dave Young
// Date created: April 13, 2015
// Summary: Errorbars for scatter plots

var chartErrorBars = function() {

    // -------------- INSTANTIATE MODULE ATTRIBUTES ---------------- // 
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    var init = function(settings) {
        // console.log('init function triggered' for chartErrorBars);

        return {
            line: _get_valueline(settings),
            data: _get_dataArray(settings)
        }
    }

    var update_attributes_via_json = function(settings) {
            // console.log('attributes function triggered for chartErrorBars');
            // xt-set-setting-if-defined
        }
        // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    var _get_valueline = function(settings) {
        // console.log('_get_valueline function triggered');

        var valueline = d3.svg.line()
            .interpolate("linear")
            .x(function(d) {
                return d.x;
            })
            .y(function(d) {
                return d.y;
            });

        valueline = {
            line: valueline,
            x1Values: "x",
            y1Values: "y",
            id: settings.id,
            color: settings.color,
            htmlclass: settings.htmlclass,
        }

        return valueline

    }

    var _get_dataArray = function(settings) {
        // console.log('_get_dataArray function triggered');

        // be careful with variable names for items went compiling JS
        var newArray = new Array();
        var array = settings.data;
        for (i = 0; i < array.length; i++) {
            var item = array[i];
            //console.log('item: ' + JSON.stringify(item));
            //console.log('item[settings.x1Values]: ' + JSON.stringify(item[settings.x1Values]));

            var thisData = [{
                "x": settings.axes.x1(item[settings.x1Values]),
                "y": settings.axes.y1(item[settings.y1Values] - item[settings.y1Errors])
            }, {
                "x": settings.axes.x1(item[settings.x1Values]),
                "y": settings.axes.y1(item[settings.y1Values] + item[settings.y1Errors])
            }];
            newArray.push(thisData);

            thisRange = settings.x1Range[0] - settings.x1Range[1]
            // console.log('settings.x1Range: ' + settings.x1Range);

            var topcap = [{
                "x": settings.axes.x1(item[settings.x1Values] - thisRange / 150),
                "y": settings.axes.y1(item[settings.y1Values] - item[settings.y1Errors])
            }, {
                "x": settings.axes.x1(item[settings.x1Values] + thisRange / 150),
                "y": settings.axes.y1(item[settings.y1Values] - item[settings.y1Errors])
            }];
            newArray.push(topcap);

            var bottomcap = [{
                "x": settings.axes.x1(item[settings.x1Values] - thisRange / 150),
                "y": settings.axes.y1(item[settings.y1Values] + item[settings.y1Errors])
            }, {
                "x": settings.axes.x1(item[settings.x1Values] + thisRange / 150),
                "y": settings.axes.y1(item[settings.y1Values] + item[settings.y1Errors])
            }];
            newArray.push(bottomcap);
        }

        return newArray

    }

    // xt-function-as-named-variable

    //--- REVEAL PUBLIC POINTERS TO PRIVATE METHODS AND ATTRIBUTES ---//
    return {
        init: init,
        update_attributes: update_attributes_via_json
            // xt-public-pointers
    };

};
