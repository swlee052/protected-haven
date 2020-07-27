var options = {
    timeout: 5000,
    maximumAge: 0
  };
  
  function success(pos) {
    var crd = pos.coords;
    return crd;
    // console.log('Your current position is:');
    // console.log(`Latitude : ${crd.latitude}`);
    // console.log(`Longitude: ${crd.longitude}`);
    // console.log(`More or less ${crd.accuracy} meters.`);
  }
  
  function error(err) {
    return 'Location not included';
  }
  
  function location(){
      loc = navigator.geolocation.getCurrentPosition(success, error, options);
      return loc;
  }