// JavaScript код для показа/скрытия подменю


/* Переписали Котлин на JavaScript */
const Rp = 6356.8        // km. Not used
const Re = 6378.0        // km. Not used
const earthRadius = 6371

function Pifagor(p1, p2) {   // p.x, p.y, p.z
  return Math.sqrt(
    (p1.z - p2.z) * (p1.z - p2.z) +
    (p1.x - p2.x) * (p1.x - p2.x) +
    (p1.y - p2.y) * (p1.y - p2.y))
}

// Стрелочные функции конверсии в радианы и градусы
const degreesToRadians = degrees => degrees * (Math.PI / 180);
const radiansToDegrees = radians => radians * (180 / Math.PI);

function loc_to_sphere(location) {   // location: longitude, latitude, altitude
  console.log(location);
  const alt = location.altitude / 1000.0         // km

  const lon = degreesToRadians(location.longitude)  
  const lat = degreesToRadians(location.latitude)

  // To Spherical coordinates
  const cl = Math.cos(lat)
  const R  = earthRadius + alt  // km
  return {
    z: R * Math.sin(lat),
    x: R * cl * Math.cos(lon),
    y: R * cl * Math.sin(lon)
  }
}

function distance(location1, location2) {
  return Pifagor(
    loc_to_sphere(location1),
    loc_to_sphere(location2)
  )
}

// Координаты городов
const cities = {
  'Москва': {
    latitude: 55.755826,
    longitude: 37.6173,
    altitude: earthRadius
  },
  'Санкт-Петербург': {
    latitude: 59.934280,
    longitude: 30.335086,
    altitude: earthRadius
  },
  'Казань':{
    latitude: 55.797104,
    longitude: 49.114209,
    altitude: earthRadius
  },
  'Краснодар': {
    latitude: 45.040233,
    longitude: 38.976286,
    altitude: earthRadius
  }
};



function calc() {
  let result = Math.round(80*distance(cities[way_1.value], cities[way_2.value]));
  final_price.innerHTML = result;
}


function work_but (){
    var pogruz = way1
    var razgruz = way2

    var all_dist = way1 / way2

};


function count_st() {

  const centralSubtendedAngle = (locationX, locationY) => {
    const locationXLatRadians = degreesToRadians(locationX.latitude);
    const locationYLatRadians = degreesToRadians(locationY.latitude);
  return radiansToDegrees(
      Math.acos(
        Math.sin(locationXLatRadians) * Math.sin(locationYLatRadians) +
          Math.cos(locationXLatRadians) *
            Math.cos(locationYLatRadians) *
            Math.cos(
              degreesToRadians(
                Math.abs(locationX.longitude - locationY.longitude)
              )
        )
      )
    );
  }

  2 * Math.PI * {earthRadius} * ({central_subtended, angle} / 360);


  
  const greatCircleDistance = angle => 2 * Math.PI * earthRadius * (angle / 360);
  const distanceBetweenLocations = (locationX, locationY) =>
    greatCircleDistance(centralSubtendedAngle(locationX, locationY));

  const Moscow = {latitude: 55.755826, longitude: 37.6173};
  const Saint_Petersbutg = {latitude: 59.934280, longitude: 30.335086};
  console.log(distanceBetweenLocations(Moscow, Saint_Petersbutg));
}