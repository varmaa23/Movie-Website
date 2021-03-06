// Authors: Valentina Guerrero and Aishwarya Varma


window.onload = initialize;

function initialize() {

var button = document.getElementById('submit');
button.addEventListener('click', delete_html);
button.addEventListener('click', get_movies);


if (window.location.search.split('?')){
    let url = window.location.search.split('?');
    if (url[1].split('=')){
        let values_url = url[1].split('=')
    
    let key_type = values_url[0]
    let key_value = values_url[1];
    const valueCapitalized = key_value.charAt(0).toUpperCase() + key_value.slice(1)
    let query_parameters = `${key_type}=${valueCapitalized}`

    if (values_url){
        fetch_movies(query_parameters)
    }

    }
    
}



const dropdown_keys = get_dropdown_keys()

for (key in dropdown_keys) {
    console.log(key)
    fetch_dropdown_items(dropdown_keys[key])
    
}

    
}

function get_dropdown_keys() {
    return ['genres', 'languages', 'countries']
}

function get_search_values() {
    return ['title', 'rating', 'release_year', 'genres', 'languages', 'countries']
}

function get_api_base_url(){
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}


function create_dropdown_options(item_id, item_list){
    var item_select = document.getElementById(`${item_id}`);
    var option_element = document.createElement("option");
    option_element.text = 'All';
    item_select.options.add(option_element);
    count = 0;
    for(item in item_list){
        var option_element = document.createElement("option");
        option_element.text = item_list[count];
        count = count + 1
        item_select.options.add(option_element);
    }

}


function fetch_dropdown_items(key) {
    var url = get_api_base_url() + `/${key}`;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(items) {
        create_dropdown_options(key, items)
    })

    .catch(function(error) {
        console.log(error);
    });
}


function fetch_movies(endpoint_parameters) {
    var url = get_api_base_url() + `/movies?${endpoint_parameters}`;
    console.log(url)

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        console.log(movies)
        for (let i = 0; i < 10; i++){
            create_html(movies[i].title, movies[i].genres, movies[i].rating, movies[i].release_year, movies[i].id)
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

// filters = ['genres']
function get_movies(){
    filters_list = get_filters()
    dropdown_keys = get_dropdown_keys()
    endpoint_parameters = ``
    for (let i = 0; i < filters_list.length; i++){
        filter = capitalize_first_letter(filters_list[i])
        console.log(filter)
        key = dropdown_keys[i]
        if (filter != 'All'){
            search_string = `${key}=${filter}&`
            endpoint_parameters += search_string 
        }
        
    }
    endpoint_parameters = endpoint_parameters.substring(0, endpoint_parameters.length - 1);

    fetch_movies(endpoint_parameters)
}

function capitalize_first_letter(string){
    string.charAt(0).toUpperCase() + string
    return string
}

function get_filters(){
    filters_list = []

    dropdown_keys = get_dropdown_keys()
    for (key in dropdown_keys){
            dropdown_keys[key] = document.getElementById(`${dropdown_keys[key]}`).value;
            filters_list.push(dropdown_keys[key])
        
    }
   
    return filters_list

}


function create_html(title, genres, rating, release_year, id){
    let main_content_div = document.getElementById('main-div');
    let card_div = document.createElement('div');
    card_div.setAttribute('id', 'card_div')
    let card = document.createElement('div');
    card.classList.add('movie-card')

    let image = document.createElement('div');
    image.classList.add('movie-image', 'secondary-color')

    let main_info = document.createElement('div');
    main_info.classList.add('movie-card-margin')

    let rating_div = document.createElement('div');

    let movie_title = document.createElement('h3');
    let title_text = document.createTextNode(title);
    movie_title.appendChild(title_text)
    main_info.appendChild(movie_title);

    let movie_genres = document.createElement('p');
    let genres_text = document.createTextNode(genres);
    movie_genres.appendChild(genres_text)
    main_info.appendChild(movie_genres);

    let movie_release_year = document.createElement('p');
    let year_text = document.createTextNode(release_year);
    movie_release_year.appendChild(year_text)
    main_info.appendChild(movie_release_year);


    protocol = window.location.protocol
    hostname = window.location.hostname
    port = window.location.port
    url = `${protocol}//${hostname}:${port}/movie?id=${id}`
    let movie_more = document.createElement('a');
    let more_text = document.createTextNode('View more');
    movie_more.href = url
    movie_more.appendChild(more_text)
    main_info.appendChild(movie_more);

    let movie_rating = document.createElement('p');
    let rating_text = document.createTextNode(rating);
    movie_rating.appendChild(rating_text)
    rating_div.appendChild(movie_rating);
    
    card.appendChild(image);
    card.appendChild(main_info);
    card.appendChild(rating_div);
    card_div.appendChild(card)
    main_content_div.appendChild(card_div)

}


function delete_html(){
    let myNode = document.getElementById('main-div');
    while (myNode.firstChild) {
        myNode.removeChild(myNode.lastChild);
      }
}

