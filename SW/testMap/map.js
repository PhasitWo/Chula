var map

function init() {
    // mockup
    places = [
        { name: "MBK", location: { lat:13.745258, lon:100.529962 } },
        { name: "National Stadium", location: { lat:13.744320, lon:100.528117 }},
        { name: "คณะเภสัชศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย", location: { lat:13.743723, lon:100.531126 }},
        {name:"คณะอักษร จุฬาลงกรณ์มหาวิทยาลัย", location: {lat:13.739005, lon:100.534176}}
    ]
    let listbox = document.getElementById("destination")
    listbox.onchange = clearOverlay
    places.forEach(place => {
        option = document.createElement('option')
        option.appendChild(document.createTextNode(place.name))
        option.location = place.location;
        listbox.add(option)
    })
    // setup map
    map = new longdo.Map({
        placeholder: document.getElementById('map')
    });
    map.Layers.setBase(longdo.Layers.GRAY);
    const origin = { lat:13.742548, lon:100.527334 }
    map.location(origin, true);
    map.zoom(15, true);
    map.Route.placeholder(document.getElementById('result'));
    map.Route.mode(longdo.RouteMode.Cost)
    
}

function findRoute() {
    clearOverlay()
    let list = document.getElementById("list");
    list.innerHTML = ''
    let start = { lat:13.732189, lon:100.525671 }
    listbox = document.getElementById("destination")
    let dest = listbox.options[listbox.selectedIndex].location
    // mock up db
    db = [
        {
            name: 'สาย A',
            nodes: [{ lat: 13.734125050183566, lon: 100.52886254670416 }, { lat: 13.736216, lon: 100.529187 },
            { lat: 13.738086033382466, lon: 100.52941224076183 }, { lat: 13.741230, lon: 100.529930 },
            { lat: 13.744437, lon: 100.530428 }, {lat:13.747453, lon:100.530851}]
        },
        {
            name: 'สาย B',
            nodes: [{lat:13.733065, lon:100.527754},{lat:13.733570, lon:100.526541},
                {lat:13.734876, lon:100.523361}, {lat:13.736318, lon:100.521674}, {lat:13.738430, lon:100.522057},
                {lat:13.741994, lon:100.522726}, {lat:13.744905, lon:100.523249}, {lat:13.746923, lon:100.523635},
                {lat:13.747134, lon:100.526024}, {lat:13.746489, lon:100.529591}, {lat:13.746098, lon:100.531986}]
        },
        {
            name: 'สาย C',
            nodes: [{lat:13.732444, lon:100.529985}, {lat:13.731222, lon:100.532901},
                {lat:13.733152, lon:100.533883}, {lat:13.737681, lon:100.534544}, {lat:13.742121, lon:100.535190},
                {lat:13.744826, lon:100.535655}, {lat:13.745496, lon:100.534691}, {lat:13.745925, lon:100.531954},
                {lat:13.744880, lon:100.530682}, {lat:13.742521, lon:100.530342}, {lat:13.739154, lon:100.529813},
                {lat:13.734160, lon:100.529068}]
        }
    ]
    // find route
    let choice = []
    db.forEach(bus_route => {
        var route = {name:bus_route.name, walk_start_to_node:0, walk_node_to_dest:0, nodes:[]}
        threshold = 2000
        let closest_node_to_start = null
        let closest_node_to_dest = null
        let min_distance_from_start = threshold
        let min_distance_from_dest = threshold
        // find closest nodes
        bus_route.nodes.forEach(node => {
            s_d = distance(node, start)
            d_d = distance(node, dest)
            if (s_d < min_distance_from_start) {
                closest_node_to_start = node
                min_distance_from_start = s_d
            }
            if (d_d < min_distance_from_dest) {
                closest_node_to_dest = node
                min_distance_from_dest = d_d
            }
        })
        // add nodes that are in between
        if (closest_node_to_start != null && closest_node_to_dest != null) {
            route.nodes.push(closest_node_to_start)
            cntd_index = bus_route.nodes.indexOf(closest_node_to_dest)
            let i = (bus_route.nodes.indexOf(closest_node_to_start) + 1) % bus_route.nodes.length
            while (i != cntd_index) {
                console.log(i)
                route.nodes.push(bus_route.nodes[i])
                i = (i + 1) % bus_route.nodes.length
            }
            route.nodes.push(closest_node_to_dest)
            route.walk_start_to_node = Math.round(min_distance_from_start)
            route.walk_node_to_dest = Math.round(min_distance_from_dest)
            choice.push(route)
        }
    })
   
    // display choice
    if (choice.length == 0) {
        list.innerHTML = "ระยะเดินเกินกำหนด"
        return
    }
    choice.sort((a,b) => (a.walk_start_to_node + a.walk_node_to_dest) - (b.walk_start_to_node + b.walk_node_to_dest))
    choice.forEach(bus_route => {
        entry = document.createElement('li');
        content = document.createElement('a');
        sum_walk = bus_route.walk_start_to_node + bus_route.walk_node_to_dest
        content.appendChild(document.createTextNode(bus_route.name +" (เดิน " + sum_walk + "เมตร)"));
        content.href = "#"
        content.onclick = () =>{
            // draw walk line
            clearOverlay()
            map.Overlays.add(new longdo.Marker(start));
            map.Overlays.add(new longdo.Marker(dest, {icon: {
                url: 'https://map.longdo.com/mmmap/images/pin_mark.png',
                offset: { x: 12, y: 45 }
            }}));
            dashline1 = new longdo.Polyline([start, bus_route.nodes[0]], {lineStyle: longdo.LineStyle.Dashed, lineColor:"green", label:bus_route.walk_start_to_node+" ม."})
            dashline2 = new longdo.Polyline([dest, bus_route.nodes[bus_route.nodes.length - 1]], {lineStyle: longdo.LineStyle.Dashed, lineColor:"green", label:bus_route.walk_node_to_dest+" ม."})
            map.Overlays.add(dashline1)
            map.Overlays.add(dashline2)
            displayRoute(bus_route.nodes)
        }
        entry.appendChild(content)
        list.appendChild(entry);
    })
    
}

function displayRoute(nodes) {
    nodes.forEach(node => {
        map.Route.add(node)
    });
}

function clearOverlay() {
    map.Overlays.clear();
    map.Route.clear()
}

function distance(place1, place2) {

    lon1 = place1.lon * Math.PI / 180;
    lon2 = place2.lon * Math.PI / 180;
    lat1 = place1.lat * Math.PI / 180;
    lat2 = place2.lat * Math.PI / 180;

    // Haversine formula 
    let dlon = lon2 - lon1;
    let dlat = lat2 - lat1;
    let a = Math.pow(Math.sin(dlat / 2), 2)
        + Math.cos(lat1) * Math.cos(lat2)
        * Math.pow(Math.sin(dlon / 2), 2);

    let c = 2 * Math.asin(Math.sqrt(a));

    // Radius of earth in kilometers. Use 3956 
    // for miles
    let r = 6371;

    // calculate the result
    return (c * r * 1000);
}
