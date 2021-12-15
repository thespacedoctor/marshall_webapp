var ra_sex2degrees = function(ra) {

  ra = ra.replace(/ /g, ":");
  ra = ra.replace(/h/g, ":");
  ra = ra.replace(/m/g, ":");
  ra = ra.replace(/s/g, "");
  var parts = ra.split(':');
  //var parts = dec.split(' ');

  var ra_d = parseInt(parts[0], 10) * 15.0;
  var ra_m = parseInt(parts[1], 10) * 15.0;
  var ra_s = parseFloat(parts[2], 10) * 15.0;

  var decimalDegrees = (ra_d + (ra_m / 60.0) + (ra_s / 3600.0));
  return decimalDegrees;
}
