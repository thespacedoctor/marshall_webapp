// _pessto_create_new_ticket_form.js
// =================================
// Author: Dave Young
// Date created: November 4, 2014
// Summary: Function for the create new ticket form on the Marshall

var _pessto_create_new_ticket_form = (function() {

    var raInput = $("input[name='objectRa']");
    raInput.blur(function() {
        var thisRa = raInput.val();
        if (thisRa.indexOf(":") >= 0) {
            thisRa = ra_sex2degrees(thisRa);
        }
        if ($.isNumeric(thisRa)) {
            raInput.val(thisRa);
        }
    });

    var decInput = $("input[name='objectDec']");
    decInput.blur(function() {
        var thisDec = decInput.val();
        if (thisDec.indexOf(":") >= 0) {
            thisDec = dec_sex2degrees(thisDec);
        }
        if ($.isNumeric(thisDec)) {
            decInput.val(thisDec);
        }
    });

})();
