var dec_sex2degrees = function(dec) {
  var sgn;
  dec = dec.replace(/ /g, ":");
  dec = dec.replace(/d/g, ":");
  dec = dec.replace(/m/g, ":");
  dec = dec.replace(/s/g, "");
  var parts = dec.split(':');
  //var parts = dec.split(' ');

  if (parts[0][0] == "-") {
    sgn = -1;
  } else {
    sgn = 1;
  }

  var dec_d = parseInt(parts[0], 10);
  var dec_m = parseInt(parts[1], 10);
  var dec_s = parseFloat(parts[2], 10);

  dec_d = Math.abs(dec_d);
  var decimalDegrees = (dec_d + (dec_m / 60.0) + (dec_s / 3600.0)) * sgn;

  return decimalDegrees;
}