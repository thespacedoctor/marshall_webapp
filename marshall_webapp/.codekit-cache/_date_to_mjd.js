// _date_to_mjd.js
// ===============
// Author: Dave Young
// Date created: April 14, 2015
// Summary: Convert date to MJD

var date_to_mjd = function(thisDate) {
    var mjd = (thisDate / 86400000) - (thisDate.getTimezoneOffset() / 1440) + 2440587.5 - 2400000.5;
    // console.log('thisDate: ' + JSON.stringify(thisDate));
    // console.log('mjd: ' + JSON.stringify(mjd));
    return mjd
}
