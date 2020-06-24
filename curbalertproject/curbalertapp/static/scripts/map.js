var myalertmap = L.map('curbalertmapid').setView([-100, 40.3], 20);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibW9sbGllZ29mb3J0aCIsImEiOiJja2J0dnlramowY3p3Mnpud2llcW1hNjJkIn0.LLfgC5JgkPmJ-_5bYiOqZg'
}).addTo(mymap);
