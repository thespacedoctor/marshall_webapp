var example10 = (function() {

    // Instantiation Code
    if ($("svg.example10").length === 0) {
        return
    }

    // Module Attributes
    var map = L.map('map').setView([-41.2858, 174.7868], 13);
    mapLink =
        '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer(
        'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
        }).addTo(map);

    // Add an SVG element to Leaflet’s overlay pane
    var svg = d3.select(map.getPanes().overlayPane).append("svg"),
        g = svg.append("g").attr("class", "leaflet-zoom-hide");

    d3.json("data/rectangle.json", function(geoShape) {

        //  create a d3.geo.path to convert GeoJSON to SVG
        var transform = d3.geo.transform({
                point: projectPoint
            }),
            path = d3.geo.path().projection(transform);

        // create path elements for each of the features
        d3_features = g.selectAll("path")
            .data(geoShape.features)
            .enter().append("path");

        map.on("viewreset", reset);

        reset();

        // fit the SVG element to leaflet's map layer
        function reset() {

            bounds = path.bounds(geoShape);

            var topLeft = bounds[0],
                bottomRight = bounds[1];

            svg.attr("width", bottomRight[0] - topLeft[0])
                .attr("height", bottomRight[1] - topLeft[1])
                .style("left", topLeft[0] + "px")
                .style("top", topLeft[1] + "px");

            g.attr("transform", "translate(" + -topLeft[0] + "," + -topLeft[1] + ")");

            // initialize the path data 
            d3_features.attr("d", path)
                .style("fill-opacity", 0.7)
                .attr('fill', 'blue');
        }

        // Use Leaflet to implement a D3 geometric transformation.
        function projectPoint(x, y) {
            var point = map.latLngToLayerPoint(new L.LatLng(y, x));
            this.stream.point(point.x, point.y);
        }

    })

    // Methods Methods

    // Reveal public pointers to
    // private methods and attributes
    return {
        // xt-public-pointers
    };

})();
