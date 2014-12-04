// ============  CODEKIT IMPORTS  =========== //
//@codekit-prepend "utils/dryxPlotting_utils.js";
//@codekit-prepend "_initialise_chart.js";

// Initialisation Code
$(function() {
    if ($("svg.chart").length > 0) {
        initialise_chart;
    }
});
