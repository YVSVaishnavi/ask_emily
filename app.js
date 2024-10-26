async function fetchCampgrounds() {
    const location = document.getElementById("location").value;
    const preferences = document.getElementById("preferences").value;
    const response = await fetch(`/campgrounds?location=${location}&preferences=${preferences}`);
    const data = await response.json();
    
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = '';
    
    if (data.campgrounds) {
        data.campgrounds.forEach(campground => {
            const div = document.createElement("div");
            div.innerText = `Name: ${campground.name}, Location: ${campground.location}`;
            resultsDiv.appendChild(div);
        });
    } else {
        resultsDiv.innerText = "No campgrounds found.";
    }
}

async function calculateRoute() {
    const start = document.getElementById("start").value;
    const destination = document.getElementById("destination").value;
    const rig_size = document.getElementById("rig_size").value;

    const response = await fetch('/route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ start, destination, rig_size })
    });
    const data = await response.json();
    
    const routeResultsDiv = document.getElementById("routeResults");
    routeResultsDiv.innerHTML = JSON.stringify(data, null, 2);
}

async function findTechnicians() {
    const techLocation = document.getElementById("techLocation").value;
    const issue = document.getElementById("issue").value;

    const response = await fetch(`/technicians?location=${techLocation}&issue=${issue}`);
    const data = await response.json();
    
    const techResultsDiv = document.getElementById("techResults");
    techResultsDiv.innerHTML = '';
    
    if (data.technicians) {
        data.technicians.forEach(tech => {
            const div = document.createElement("div");
            div.innerText = `Name: ${tech.name}, Location: ${tech.location}`;
            techResultsDiv.appendChild(div);
        });
    } else {
        techResultsDiv.innerText = "No technicians found.";
    }
}
