window.onload = function() {
  
  const options = {
    timeout: 5000,
    maximumAge: 0
  };
  
  function loc_success(pos) {
    var crd = pos.coords;
    console.log('Your current position is:');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude: ${crd.longitude}`);
    console.log(`More or less ${crd.accuracy} meters.`);
    return crd;
  }
  
  function loc_error(err) {
    return 'Location not included';
  }
  
  function find_loc(){
    loc = navigator.geolocation.getCurrentPosition(loc_success, loc_error, options);
    console.log(loc);
    return loc;
  }
  find_loc()
}


// window.onload = find_loc();