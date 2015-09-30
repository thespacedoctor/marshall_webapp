// ============  CODEKIT IMPORTS  =========== //
//@codekit-prepend "utils/dryxAladin_utils.js";
//@codekit-prepend "aladinSourceCode/cds.js"
//@codekit-prepend "aladinSourceCode/json2.js"
//@codekit-prepend "aladinSourceCode/Logger.js"
//@codekit-prepend "aladinSourceCode/jquery.mousewheel.js"
//@codekit-prepend "aladinSourceCode/RequestAnimationFrame.js"
//@codekit-prepend "aladinSourceCode/Stats.js"
//@codekit-prepend "aladinSourceCode/healpix.min.js"
//@codekit-prepend "aladinSourceCode/astroMath.js"
//@codekit-prepend "aladinSourceCode/projection.js"
//@codekit-prepend "aladinSourceCode/coo.js"
//@codekit-prepend "aladinSourceCode/CooConversion.js"
//@codekit-prepend "aladinSourceCode/Sesame.js"
//@codekit-prepend "aladinSourceCode/HealpixCache.js"
//@codekit-prepend "aladinSourceCode/Utils.js"
//@codekit-prepend "aladinSourceCode/Color.js"
//@codekit-prepend "aladinSourceCode/AladinUtils.js"
//@codekit-prepend "aladinSourceCode/ProjectionEnum.js"
//@codekit-prepend "aladinSourceCode/CooFrameEnum.js"
//@codekit-prepend "aladinSourceCode/Downloader.js"
//@codekit-prepend "aladinSourceCode/CooGrid.js"
//@codekit-prepend "aladinSourceCode/Footprint.js"
//@codekit-prepend "aladinSourceCode/Popup.js"
//@codekit-prepend "aladinSourceCode/Circle.js"
//@codekit-prepend "aladinSourceCode/Polyline.js"
//@codekit-prepend "aladinSourceCode/Overlay.js"
//@codekit-prepend "aladinSourceCode/Source.js"
//@codekit-prepend "aladinSourceCode/ProgressiveCat.js"
//@codekit-prepend "aladinSourceCode/Catalog.js"
//@codekit-prepend "aladinSourceCode/Tile.js"
//@codekit-prepend "aladinSourceCode/TileBuffer.js"
//@codekit-prepend "aladinSourceCode/ColorMap.js"
//@codekit-prepend "aladinSourceCode/HpxImageSurvey.js"
//@codekit-prepend "aladinSourceCode/HealpixGrid.js"
//@codekit-prepend "aladinSourceCode/Location.js"
//@codekit-prepend "aladinSourceCode/View.js"
//@codekit-prepend "aladinSourceCode/Aladin.js"

// dryxAladin.js
// =============
// Author: Dave Young
// Date created: September 22, 2015
// Summary: Aladin Features for webapps

function dryxAladin(thisObject) {

    // GET URL FOR JSON DATA FROM HTML OBJECT
    var dataUrl = $(thisObject).attr("data");

    $.getJSON(dataUrl, function(data) {
        var coords = $(thisObject).attr("coords");
        var survey = $(thisObject).attr("survey");
        var parameters = data["aladin_parameters"];
        var catalogues = data["catalogues"]
        var catalogueOrder = data["catalogueOrder"]
        var tranName = $(thisObject).attr("transient");

        var aladin = A.aladin(thisObject, {
            cooFrame: "J2000",
            showReticle: false,
            showZoomControl: true,
            showShareControl: false,
            showCooGrid: false,
            showFullscreenControl: true,
            showFrameChoice: false,
            showLayersControl: true,
            showGotoControl: false,
            showFrame: true,
            fullScreen: false,
            reticleColor: "#dc322f",
            reticleSize: 50,
            survey: survey,
            fov: parameters["FOV"],
            target: coords
        });

        aladin.getBaseImageLayer().getColorMap().reverse(1);

        // be careful with variable names for items went compiling JS
        var sourceOverlays = new Array();
        for (var j = 0; j < catalogueOrder.length; j++) {
            var cat = catalogueOrder[j];
            if (catalogues.hasOwnProperty(cat)) {

                // CIRCLES
                var overlay = A.graphicOverlay({
                    name: "search areas",
                    color: catalogues[cat]["color"],
                    lineWidth: parameters["search_perimeter_width"]
                });
                aladin.addOverlay(overlay);

                // LABELS
                var labelCat = A.catalog({
                    name: cat,
                    shape: "square",
                    sourceSize: 0,
                    labelFont: "20px dryx_icon_font",
                    displayLabel: true,
                    color: catalogues[cat]["color"],
                    labelColumn: "mainId",
                    colorColumn: "color"
                });
                aladin.addCatalog(labelCat);

                // MARKERS
                var markerCat = A.catalog({
                    name: cat + " markers",
                    sourceSize: 0,
                    color: catalogues[cat]["color"]
                });
                aladin.addCatalog(markerCat);

                var catData = catalogues[cat]["data"];
                for (var i = 0; i < catData.length; i++) {

                    // CIRCLE
                    overlay.add(A.circle(catData[i]["catalogue_object_ra"], catData[i]["catalogue_object_dec"], catData[i]["original_search_radius_arcsec"] / 3600., {
                        color: catData[i]["radius_color"],
                        fillOpacity: 0.1
                    }));

                    markerCat.addSources([A.marker(catData[i]["catalogue_object_ra"], catData[i]["catalogue_object_dec"], {
                        popupTitle: catData[i]["catalogue_object_id"],
                        popupDesc: catData[i]["details"]
                    })]);

                    labelCat.addSources(A.source(catData[i]["catalogue_object_ra"], catData[i]["catalogue_object_dec"], {
                        "mainId": catData[i]["label"],
                        "color": catData[i]["radius_color"]
                    }));

                }
            }
        }

        // TRANSIENT LOCATION
        var transOverlay = A.catalog({
            name: "transient",
            sourceSize: 18,
            color: "#dc322f"
        });
        aladin.addCatalog(transOverlay);
        var raDec = coords.split(" ");
        transOverlay.addSources([A.marker(raDec[0], raDec[1], {
            popupTitle: tranName
        })]);

        aladin.setImageSurvey("P/DSS/color");

        setTimeout(function() {
            aladin.setImageSurvey(survey);
        }, 200);

    });

    // var galaxyCat = A.catalog(shape = "square", color = "#268bd2", sourceSize = 50, labelColumn = "nice", labelColor = "#268bd2")
    // aladin.addCatalog(galaxyCat)

    // -------------- PUBLIC METHODS ---------------- //
    var init = function(settings) {
        console.log('init function triggered for dryxAladin');

        return {
            // xt-public-pointers
        }
    }

    var update_attributes_via_json = function(settings) {
            console.log('attributes function triggered for dryxAladin');
            // xt-set-setting-if-defined
        }
        // xt-function-as-named-variable

    // -------------- PRIVATE HELPER METHODS ---------------- //
    // xt-function-as-named-variable

    //--- REVEAL PUBLIC POINTERS TO PRIVATE METHODS AND ATTRIBUTES ---//
    return {
        init: init,
        update_attributes: update_attributes_via_json
            // xt-public-pointers
    };

};
