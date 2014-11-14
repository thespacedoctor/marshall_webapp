// _update_chart_element.js
// ==================
// Author: Dave Young
// Date created: June 12, 2014
// Summary: A module to update elements in a consistant way

// xjs-ready-event-function
// xjs-get-json-response-from-python-script

var update_chart_element = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable

    // -------------- Public Methods ---------------- //
    // xt-update-object-settings-method
    var update_chart_element = function(settings) {
        // console.log('update function triggered');

        // xt-set-setting-if-defined

        // test for existance
        var partentElement = settings.parent_element
        var thisElement = partentElement.select(settings.element_selector)
        if (!thisElement.empty()) {
            if (settings.remove_if !== undefined) {
                thisElement.remove()
                thisElement = partentElement.select(settings.element_selector)
            }
        }
        var init = true

        if (!thisElement.empty()) {
            var partentElement = settings.parent_element.transition()
            var thisElement = partentElement.select(settings.element_selector).duration(750);
            init = false
        } else {
            // if element does not exist create it
            var thisElement = partentElement.append(settings.element_type).attr("class", settings.element_class)
        }

        if (settings.element_id !== undefined) {
            thisElement.attr("id", settings.element_id)
        }
        if (settings.transform !== undefined) {
            thisElement.attr("transform", settings.transform)
        }
        if (settings.element_call !== undefined) {
            thisElement.call(settings.element_call)
        }
        if (settings.element_data !== undefined) {
            if (settings.element_data.data !== undefined) {
                if (init) {
                    thisElement.data([settings.element_data.data])
                }
                // console.log('updated line: ' + settings.element_data.attr);

                thisElement.attr("d", settings.element_data.attr);
            }
        }

        // set any extra attributes / styles / text ...
        if (settings.extras !== undefined) {
            if (settings.extras.attr !== undefined) {
                var attrArry = settings.extras.attr;
                // console.log('array.length: ' + attrArry.length);

                for (aa = 0; aa < attrArry.length; aa++) {
                    var thisAttr = attrArry[aa];
                    // console.log('thisAttr: ' + thisAttr.attr);

                    thisElement.attr(thisAttr.attr, thisAttr.value);
                }
            }

            if (settings.extras.text !== undefined) {
                var textArray = settings.extras.text;
                for (ta = 0; ta < textArray.length; ta++) {
                    var thisText = textArray[ta];
                    thisElement.text(thisText);
                }
            }
        }
        // xt-set-setting-if-defined

        // } else {
        //     var transElement = settings.parent_element.transition();
        //     var tmpObject = transElement.select(settings.element_selector).duration(750)
        //   // console.log("tmpObject:" + tmpObject);

        //     if (settings.element_call !== undefined) {
        //         tmpObject.call(settings.element_call)
        //     }
        //     if (settings.element_data !== undefined) {
        //         if (settings.element_data.data !== undefined) {
        //             tmpObject
        //                 .attr("d", settings.element_data.attr);
        //         }
        //     }
        //     if ()
        // }

    }

    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        update: update_chart_element
        // xt-public-pointers
    };

})();
