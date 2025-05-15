function fetchData(service) {
    fetch(`/api/${service}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("response").innerHTML = `<div class="response-box"><p>${JSON.stringify(data)}</p></div>`;
        })
        .catch(error => {
            console.error("Error al obtener datos", error);
        });
}
