function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

url = "https://search.longdo.com/mapsearch/json/search?"
params = "area=10&limit=10&keyword=chula&key=fe75c23350d22e5b0ff781a28a09aaf5"
httpGetAsync(url + params, response => {
    response = JSON.parse(response)
    console.log(response)
    response.data.forEach(place => {
        if (place.type == "other")
            return
        entry = document.createElement("li")
        entry.innerHTML = place.name + "<br>" + place.address + "<br>" + place.lat +", "+place.lon
        document.getElementById("listbox").appendChild(entry)
    })
});
