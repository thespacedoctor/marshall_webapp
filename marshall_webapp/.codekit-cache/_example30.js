var example30 = (function() {

    // Instantiation Code
    if ($("svg.example30").length === 0) {
        return
    }

    // Module Attributes
    var margin = {
            top: 20,
            right: 20,
            bottom: 70,
            left: 40
        },
        width = 600 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

    // Parse the date / time
    var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

    var y = d3.scale.linear().range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10);

    var svg = d3.select("svg.example30")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/sofi_imaging_fwhm_binned_J_band.csv", function(error, data) {

        data.forEach(function(d) {
            d.bin = +d.bin;
            d.count = +d.count;
        });

        x.domain(data.map(function(d) {
            return d.bin;
        }));
        y.domain([0, d3.max(data, function(d) {
            return d.count;
        })]);

        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "+.2em")
            .attr("dy", "+0.8em")
            .attr("transform", "rotate(-30)")

        svg.select("g.x").append("text")
            .attr("x", width * 0.8)
            .attr("dy", height * 0.25)
            .text("FWHM (arcsec)")

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Number of Images");

        svg.select("g.y").append("text")
            .attr("dy", -height * 0.05)
            .attr("x", width * 0.9)
            .text("J Band")

        svg.selectAll("bar")
            .data(data)
            .enter().append("rect")
            .style("fill", "#b58900")
            .attr("x", function(d) {
                return x(d.bin);
            })
            .attr("width", x.rangeBand())
            .attr("y", function(d) {
                return y(d.count);
            })
            .attr("height", function(d) {
                return height - y(d.count);
            });

    });

    // Methods Methods

    // Reveal public pointers to
    // private methods and attributes
    return {
        // xt-public-pointers
    };

})();

var example31 = (function() {

    // Instantiation Code
    if ($("svg.example31").length === 0) {
        return
    }

    // Module Attributes
    var margin = {
            top: 20,
            right: 20,
            bottom: 70,
            left: 40
        },
        width = 600 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

    // Parse the date / time
    var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

    var y = d3.scale.linear().range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10);

    var svg = d3.select("svg.example31")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/sofi_imaging_fwhm_binned_H_band.csv", function(error, data) {

        data.forEach(function(d) {
            d.bin = +d.bin;
            d.count = +d.count;
        });

        x.domain(data.map(function(d) {
            return d.bin;
        }));
        y.domain([0, d3.max(data, function(d) {
            return d.count;
        })]);

        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "+.2em")
            .attr("dy", "+0.8em")
            .attr("transform", "rotate(-30)")

        svg.select("g.x").append("text")
            .attr("x", width * 0.8)
            .attr("dy", height * 0.25)
            .text("FWHM (arcsec)")

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Number of Images");

        svg.select("g.y").append("text")
            .attr("dy", -height * 0.05)
            .attr("x", width * 0.9)
            .text("H Band")

        svg.selectAll("bar")
            .data(data)
            .enter().append("rect")
            .style("fill", "#cb4b16")
            .attr("x", function(d) {
                return x(d.bin);
            })
            .attr("width", x.rangeBand())
            .attr("y", function(d) {
                return y(d.count);
            })
            .attr("height", function(d) {
                return height - y(d.count);
            });

    });

    // Methods Methods

    // Reveal public pointers to
    // private methods and attributes
    return {
        // xt-public-pointers
    };

})();

var example32 = (function() {

    // Instantiation Code
    if ($("svg.example32").length === 0) {
        return
    }

    // Module Attributes
    var margin = {
            top: 20,
            right: 20,
            bottom: 70,
            left: 40
        },
        width = 600 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

    // Parse the date / time
    var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

    var y = d3.scale.linear().range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(10);

    var svg = d3.select("svg.example32")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/sofi_imaging_fwhm_binned_Ks_band.csv", function(error, data) {

        data.forEach(function(d) {
            d.bin = +d.bin;
            d.count = +d.count;
        });

        x.domain(data.map(function(d) {
            return d.bin;
        }));
        y.domain([0, d3.max(data, function(d) {
            return d.count;
        })]);

        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "+.2em")
            .attr("dy", "+0.8em")
            .attr("transform", "rotate(-30)")

        svg.select("g.x").append("text")
            .attr("x", width * 0.8)
            .attr("dy", height * 0.25)
            .text("FWHM (arcsec)")

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Number of Images");

        svg.select("g.y").append("text")
            .attr("dy", -height * 0.05)
            .attr("x", width * 0.9)
            .text("Ks Band")

        svg.selectAll("bar")
            .data(data)
            .enter().append("rect")
            .style("fill", "#dc322f")
            .attr("x", function(d) {
                return x(d.bin);
            })
            .attr("width", x.rangeBand())
            .attr("y", function(d) {
                return y(d.count);
            })
            .attr("height", function(d) {
                return height - y(d.count);
            });

    });

    // Methods Methods

    // Reveal public pointers to
    // private methods and attributes
    return {
        // xt-public-pointers
    };

})();
