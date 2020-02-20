
var query_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
console.log(query_url)
d3.json(query_url,function(data)
{
   createFeatures(data.features);
   console.log(data.features)
});

function createFeatures(earthquakeData) {

  function onEachFeature(feature,layer) {
      layer.bindPopup("<h3>" + feature.properties.place + 
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
    }
    
  function radiusSize(magnitude) {
        return magnitude * 20000; 
    }

  function circleColor(magnitude) {
        if (magnitude < 1) {
          return "#0ee90"
        }
        else if (magnitude < 2) {
          return "#ffff00"
        }
        else if (magnitude < 3) {
          return "#ffa500"
        }
        else if (magnitude < 4) {
          return "#ff5349"
        }
        else if (magnitude < 5) {
          return "ff0000"
        }
        else {
          return "00ff00"
        }
      }
    var earthquakes = L.geoJSON(earthquakeData, {
        pointToLayer: function(earthquakeData, latlng) {
          return L.circle(latlng, {
            radius: radiusSize(earthquakeData.properties.mag),
            color: circleColor(earthquakeData.properties.mag),
            fillOpacity: 1
          });
        },
        onEachFeature: onEachFeature
      });

    function createMap() {

      var highContrastMap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.high-contrast',
            accessToken: 'pk.eyJ1Ijoib2xhd3JlbmNlNzk5IiwiYSI6ImNqZXZvcTBmdDBuY3oycXFqZThzbjc5djYifQ.-ChNrBxEIvInNJWiHX5pXg'
        });
    
      var streetMap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.streets',
            accessToken: 'pk.eyJ1IjoibmdqYW1lczA4IiwiYSI6ImNrNDV3bjZ2czBlMjAza3E3aThjYnJjOWMifQ.-W6ypusaKLOH6KsS1wWj4A'
        });
    
      var darkMap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.dark',
            accessToken: 'pk.eyJ1IjoibmdqYW1lczA4IiwiYSI6ImNrNDV3bjZ2czBlMjAza3E3aThjYnJjOWMifQ.-W6ypusaKLOH6KsS1wWj4A'
        });

      var satellite = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.satellite',
            accessToken: 'pk.eyJ1IjoibmdqYW1lczA4IiwiYSI6ImNrNDV3bjZ2czBlMjAza3E3aThjYnJjOWMifQ.-W6ypusaKLOH6KsS1wWj4A'
        });
    
    
      var baseLayers = {
            "High Contrast": highContrastMap,
            "Street": streetMap,
            "Dark": darkMap,
            "Satellite": satellite
        };
    
      var overlays = {
            "Earthquakes": earthquakes,
        };
    
      var mymap = L.map('mymap', {
            center: [40, -99],
            zoom: 4.3,
          
            layers: [streetMap, earthquakes]
        });
    
        L.control.layers(baseLayers, overlays).addTo(mymap);
     
    
      var legend = L.control({ position: 'bottomright' });
    
      legend.onAdd = function (map) {
    
        var div = L.DomUtil.create('div', 'info legend'),
                magnitude = [0, 1, 2, 3, 4, 5],
                labels = [];
    
        div.innerHTML += "<h4 style='margin:4px'>Magnitude</h4>"
    
          for (var i = 0; i < magnitude.length; i++) {
                div.innerHTML +=
                    '<i style="background:' + Color(magnitude[i] + 1) + '"></i> ' +
                    magnitude[i] + (magnitude[i + 1] ? '&ndash;' + magnitude[i + 1] + '<br>' : '+');
            }
    
            return div;
          };
        legend.addTo(mymap);
    }
  };
