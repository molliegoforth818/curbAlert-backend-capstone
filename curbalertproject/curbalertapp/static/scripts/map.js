var available_donations = JSON.parse(document.getElementById('available_donations').textContent);

function map_init(map,options){
    available_donations.forEach(donation => {
        marker= L.marker([donation.latitude, donation.longitude]).addTo(map);
        marker.bindPopup(`Description: ${donation.description}</br><a href=/donation/detail/>${donation.id}> Go to Donation</a>`);
 
    }); 
   }
