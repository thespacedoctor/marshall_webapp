// _update_chart_element.js
// ==================
// Author: Dave Young
// Date created: June 12, 2014
// Summary: A module to update elements in a consistant way

var update_chart_element = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var init = true;
    var partentElement = undefined;
    var thisElement = undefined;
    var settings = undefined;
    // xt-initialise-variable

    // -------------- PUBLIC METHODS ---------------- //
    // xt-update-object-settings-method
    var update_chart_element = function(settings) {
        // xt-set-setting-if-defined
        partentElement = settings.parent_element;
        // SELECT THE ELEMENT(S) TO BE UPDATED
        _select_element(partentElement, settings, init)
        _assign_data_to_seleted_paths(thisElement, init, settings)
        _add_datapoints(thisElement, settings)
        _set_id_and_class(thisElement, settings)
        _update_titles_and_text(settings)

        // TRANSFORM THE ELEMENT
        if (settings.transform !== undefined) {
            thisElement.attr("transform", settings.transform)
        }
        // CALL THE ELEMENT
        if (settings.element_call !== undefined) {
            thisElement.call(settings.element_call)
        }

    }

    // -------------- PRIVATE HELPER METHODS ---------------- //
    var _select_element = function(partentElement, settings, init) {
        // INITIAL SELECT OF THE ELEMENT(S)
        if (settings.element_selector == "datapoint") {
            thisElement = partentElement.selectAll(settings.element_selector);
        } else {
            thisElement = partentElement.select(settings.elemet_selector);
        }

        // IF THE SELECTION NEEDS TO BE REMOVED THEN REMOVE IT
        if (!thisElement.empty()) {
            if (settings.remove_if !== undefined) {
                thisElement.remove()
                thisElement = partentElement.select(settings.element_selector)
            }
        }

        // ADD TRANSITION TO ANY CHANGES TO THE ELEMENTS
        if (!thisElement.empty()) {
            partentElement = settings.parent_element.transition()
            if (settings.element_selector == "datapoint") {
                thisElement = partentElement.selectAll(settings.element_selector).duration(750);
            } else {
                thisElement = partentElement.select(settings.element_selector).duration(750);
            }
            init = false;
        } else if (settings.element_type) {
            // IF ELEMENT DOES NOT EXIST CREATE IT
            thisElement = partentElement.append(settings.element_type).attr("class", settings.element_class)
        }
        return
    }

    var _assign_data_to_seleted_paths = function(thisElement, init, settings) {
        if (settings.element_data == undefined) {
            return
        }
        if (settings.element_data.data == undefined) {
            return
        }
        if (settings.element_selector == "datapoint") {
            return
        }

        // NON DATAPOINTS (LINES, AREA ETC)
        if (init) {
            thisElement.data([settings.element_data.data])
        }

        if (settings.element_data.attr !== undefined) {
            thisElement.attr("d", settings.element_data.attr);
        }
        return
    }

    var _add_datapoints = function(thisElement, settings) {
        if (settings.element_selector !== "datapoint") {
            return
        }

        thisElement.data(settings.element_data.datapoints.data)
            .enter().append(settings.element_data.datapoints.shape)
            .attr("r", settings.element_data.datapoints.attrs.radius)
            .attr("cx", settings.element_data.datapoints.datapoints.x)
            .attr("cy", settings.element_data.datapoints.datapoints.y);
    }

    var _set_id_and_class = function(thisElement, settings) {
        //   console.log('_set_id_and_class function triggered');
        // SET THE ID OF THE SINGLE ELEMENT
        if (settings.element_id !== undefined) {
            thisElement.attr("id", settings.element_id)
        }
    }

    var _update_titles_and_text = function(settings) {
        //   console.log('_update_titles_and_text function triggered');
        // set any extra attributes / styles / text ...
        if (settings.extras == undefined) {
            return
        }

        if (settings.extras.attr !== undefined) {
            var attrArry = settings.extras.attr;

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

    // xt-function-as-named-variable

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        update: update_chart_element
            // xt-public-pointers
    };

})();
