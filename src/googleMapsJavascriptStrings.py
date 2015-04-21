# Hold the text for the Google maps HTML stuff

top = (
"""<!DOCTYPE html>
<html>
  <head>
    <meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\">
    <meta charset=\"utf-8\">
    <title>Simple markers</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src=\"https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true\"></script>
    <script>
function initialize() {"""
);

middle = (
"""var mapOptions = {
    zoom: 4,
    center: myLatlng0
  }
  var map = new google.maps.Map(document.getElementById(\'map-canvas\'), mapOptions);

  var marker = ["""
);

bottom = (
"""];
}

google.maps.event.addDomListener(window, \'load\', initialize);

    </script>
  </head>
  <body>
    <div id=\"map-canvas\"></div>
  </body>
</html>"""
);