function find_loc(){
  const options = {
    timeout: 5000,
    maximumAge: 0,
    // enableHighAccuracy: true
  };

  function success(pos) {
    const crd = pos.coords;
    // console.log('Your current position is:');
    // console.log(`Latitude : ${crd.latitude}`);
    // console.log(`Longitude: ${crd.longitude}`);
    // console.log(`More or less ${crd.accuracy} meters.`);
    // find_loc.latitude = crd.latitude;
    // find_loc.longitude = crd.longitude;
    // find_loc.accuracy = crd.accuracy;
    document.getElementById("location").value = `Lat: ${crd.latitude} - Long: ${crd.longitude}`
  }

  function error(err) {
    find_loc.error = 'Location not included';
  }

navigator.geolocation.getCurrentPosition(success, error, options);
  // return find_loc;
}

window.onload = find_loc();