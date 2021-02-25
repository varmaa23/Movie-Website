window.onload = initialize;

function initialize() {
    var input_value = document.getElementById('movie_input');

    var element = document.getElementById('dogs_button');
    if (element) {
        element.onclick = onDogsButton;
    }
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function onCatsButton() {
    var url = getAPIBaseURL() + '/cats/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(cats) {
        var listBody = '';
        for (var k = 0; k < cats.length; k++) {
            var cat = cats[k];
            listBody += '<li>' + cat['name']
                      + ', ' + cat['birth_year']
                      + '-' + cat['death_year']
                      + ', ' + cat['description'];
                      + '</li>\n';
        }

        var animalListElement = document.getElementById('animal_list');
        if (animalListElement) {
            animalListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function onDogsButton() {
    var url = getAPIBaseURL() + '/dogs/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(dogs) {
        var listBody = '';
        for (var k = 0; k < dogs.length; k++) {
            var dog = dogs[k];
            listBody += '<li>' + dog['name']
                      + ', ' + dog['birth_year']
                      + '-' + dog['death_year']
                      + ', ' + dog['description'];
                      + '</li>\n';
        }

        var animalListElement = document.getElementById('animal_list');
        if (animalListElement) {
            animalListElement.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}