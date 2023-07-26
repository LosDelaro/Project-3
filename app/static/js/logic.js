
  
  function doWork() {
    let url = "/api/v1.0/map_data";
  
    // make request
    d3.json(url).then(function (data) {
        console.log(data);
        createMap(data);
    });
  }
  
  function createMap(data) {
  
    // STEP 1: CREATE THE BASE LAYERS
  
    // Create the base layers.
    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })
  
    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });
  
    // STEP 2: CREATE THE OVERLAY LAYERS
  
    // Create an overlays object.
    let markers = L.markerClusterGroup();
    let coords = [];
    for (let i = 0; i < data.length; i++){
        let row = data[i];
  
     
        let coord = [row.Latitude, row.Longitude];
        let marker = L.marker(coord).bindPopup(`${row.Show}<hr>${row.Title}`);
        markers.addLayer(marker);

        coords.push(coord);
     
    }
  
    // create heatmap layer
    let heatLayer = L.heatLayer(coords, {
      radius: 20,
      blur: 1
    });
  
   
  
    // STEP 3: Build the Layer Controls
  
    // Create a baseMaps object.
    let baseMaps = {
      "Street Map": street,
      "Topographic Map": topo
    };
  
    let overlayMaps = {
      "Locations": markers,
      "Heat Map": heatLayer
    };
  
    // STEP 4: Init the Map
  
    // Create a new map.
    // Edit the code to add the earthquake data to the layers.
    let myMap = L.map("map", {
      center: [0, 0],
      zoom: 3,
      layers: [street, markers]
    });
  
    // STEP 5: Add the Layer Controls/Legend to the map
    // Create a layer control that contains our baseMaps.
    // Be sure to add an overlay Layer that contains the earthquake GeoJSON.
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);
  }
  

  
  // on page load
  doWork();
  