var example33 = (function() {

    // Instantiation Code
    if ($("svg.example33").length === 0) {
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

    var svg = d3.select("svg.example33")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/efosc_imaging_fwhm_binned_B639_band.csv", function(error, data) {

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
            .text("B Band")

        svg.selectAll("bar")
            .data(data)
            .enter().append("rect")
            .style("fill", "#268bd2")
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

var example34 = (function() {

    // Instantiation Code
    if ($("svg.example34").length === 0) {
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

    var svg = d3.select("svg.example34")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/efosc_imaging_fwhm_binned_V641_band.csv", function(error, data) {

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
            .text("V Band")

        svg.selectAll("bar")
            .data(data)
            .enter().append("rect")
            .style("fill", "#859900")
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

var example35 = (function() {

    // Instantiation Code
    if ($("svg.example35").length === 0) {
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

    var svg = d3.select("svg.example35")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/efosc_imaging_fwhm_binned_R642_band.csv", function(error, data) {

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
            .text("R Band")

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

var example36 = (function() {

    // Instantiation Code
    if ($("svg.example36").length === 0) {
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

    var svg = d3.select("svg.example36")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    d3.csv("/assets/csv/efosc_imaging_fwhm_binned_i705_band.csv", function(error, data) {

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
            .text("i Band")

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
