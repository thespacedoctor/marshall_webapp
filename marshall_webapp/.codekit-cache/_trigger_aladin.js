//@codekit-prepend "dryxAladin.js"

// _trigger_aladin.js
// ==================
// Author: Dave Young
// Date created: September 29, 2015
// Summary: Trigger Aladin with context tab selected

$(function() {
    $("a[data-toggle='tab']").bind("click", function(event) {

        if ($(this).text().indexOf("context") >= 0) {
            var thisId = $(this).attr('href');
            var aladinDiv = $("div" + thisId).find("div.aladin-hide");
            aladinDiv.attr('class', "aladin");
            dryxAladin(aladinDiv);
        }

    });
});
