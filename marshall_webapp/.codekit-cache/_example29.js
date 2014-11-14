var example29 = (function() {

    // Instantiation Code
    if ($("svg.example29").length === 0) {
        return
    }

    // -------------- Instantiate Module Attributes ---------------- // 
    // xt-initialise-variable

    // -------------- Public Methods ---------------- //
    // xt-update-object-settings-method
    // xt-function-as-named-variable

    // -------------- Private Helper Methods ---------------- //
    // xt-function-as-named-variable

    var width = 900,
        height = 900,
        radius = Math.min(width, height) / 3;

    // var color = d3.scale.ordinal()
    //     .range(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2"]);
    var color = d3.scale.category20c();

    var arc = d3.svg.arc()
        .outerRadius(radius - 10)
        .innerRadius(radius - 200);

    var textarc = d3.svg.arc()
        .outerRadius(radius * 1.25 - 10)
        .innerRadius(radius * 1.25 - 70);

    var pie = d3.layout.pie()
        .sort(null)
        .value(function(d) {
            return d.count;
        });

    var svg = d3.select("svg.example29")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    // add table
    var columns = ["classification", "count"];

    var table = d3.select("div.example29Extras").append("table").attr("class", "table"),
        thead = table.append("thead"),
        tbody = table.append("tbody");

    d3.csv("/assets/csv/pessto_followup_classification_breakdown.csv", function(error, data) {

        totalCount = 0
        data.forEach(function(d) {
            d.count = +d.count;
            totalCount += d.count;
        });

        var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        var thisColor = function(d) {
            return color(d.data.classification);
        };
        var thisCellColor = function(d) {
            return color(d.data.classification);
        };

        // console.log('thisColor: ' + thisColor);

        g.append("path")
            .attr("d", arc)
            .style("fill", thisColor);

        g.append("text")
            .attr("transform", function(d) {
                return "translate(" + textarc.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .style("text-anchor", "middle")
            .text(function(d) {
                if (d.data.count > 1) {
                    return d.data.classification;
                } else {
                    return
                }
            });

        data.push({
            classification: "TOTAL",
            count: totalCount
        });

        // append the header row
        thead.append("tr")
            .selectAll("th")
            .data(columns)
            .enter()
            .append("th")
            .text(function(column) {
                return column;
            });

        // create a row for each object in the data
        var rows = tbody.selectAll("tr")
            .data(data)
            .enter()
            .append("tr").style("background-color", function(e) {
                if (e.classification === "TOTAL") {
                    return "#D2D1D1"
                }
                return color(e.classification);
            });

        // create a cell in each row for each column
        var cells = rows.selectAll("td")
            .data(function(row) {
                return columns.map(function(column) {
                    return {
                        column: column,
                        value: row[column],
                    };
                });
            })
            .enter()
            .append("td")
            .text(function(e) {
                return e.value;
            }).style("color", "black");

    });

    //--- Reveal public pointers to private methods and attributes ---//
    return {
        // xt-public-pointers
    };

})();
