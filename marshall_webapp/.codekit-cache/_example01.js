var example01 = (function() {

    // Instantiation Code
    if ($("svg.example01").length === 0) {
        return
    }

    // Module Attributes

    // Create a chart object
    var chart = chartCanvas.set_canvas_element("svg.example01");
    // Initialise Axes object from canvas dimensions
    var axes = chartAxes.initialise_axes_for_chart(chart);

    // Setup the datalines
    var dataLineArray = new Array();

    var dataline = chartLine.initialise_path({
        axes: axes,
        chart: chart,
        xValues: "date",
        yValues: "close",
        color: "red",
        id: Math.floor((Math.random() * 10000) + 1).toString()
    });
    dataLineArray.push(dataline);

    var dataline = chartLine.initialise_path({
        axes: axes,
        chart: chart,
        xValues: "date",
        yValues: "open",
        color: "blue",
        id: Math.floor((Math.random() * 10000) + 1).toString()
    });
    dataLineArray.push(dataline);

    // console.log(dataLineArray);

    // updateCanvas(chart, axes, dataLineArray);
    updateCanvas(chart, axes, dataLineArray, "one");
    var inter = setInterval(function() {
        // console.log('\nrefresh ');

        updateCanvas(chart, axes, dataLineArray, "two");
    }, 5000);

    // Methods Methods

    // Reveal public pointers to
    // private methods and attributes
    return {
        // xt-public-pointers
    };

})();

function updateCanvas(chart, axes, dataLineArray, chartTitle) {

    // set the date format for incoming data
    var parseDate = d3.time.format("%d-%b-%y").parse;
    // Get the data
    d3.csv("/marshall/static/caches/data2b.csv", function(error, data) {
        data.forEach(function(d) {
            d.date = parseDate(d.date);
            d.close = +d.close;
            d.open = +d.open;
        });

        // scale the axes data ranges according to the data
        xRange = d3.extent(data, function(d) {
            return d.date;
        });
        yRange = [0, d3.max(data, function(d) {
            return Math.max(d["close"], d["open"]);
        })]

        // update the axes settings
        axes.update_settings({
            chartTitle: chartTitle,
            axes: axes,
            xRange: xRange,
            yRange: yRange,
            xTitle: "Date",
            yTitle: "Value",
            xLabelsRotate: -65,
            yLabelsRotate: -15,
            xTickFormat: d3.time.format("%Y-%m-%d"),
            yTickFormat: undefined
        });

        // console.log('axes.xLabelsRotate ' + axes.xLabelsRotate);
        // console.log('dataLineArray.length: ' + dataLineArray.length);

        for (i = 0; i < dataLineArray.length; i++) {
            var line = dataLineArray[i];
            // update the chart settings
            // console.log('line: ' + line + " number " + i);

            if (line !== undefined) {
                chart.update_settings({
                    chartTitle: chartTitle,
                    axes: axes,
                    dataline: {
                        dataline: line,
                        data: data
                    }
                });
            }

        }

    });

}
