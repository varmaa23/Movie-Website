// Authors: Valentina Guerrero and Aishwarya Varma


window.onload = initialize;

function initialize() {

    var refine_results_button = document.getElementById('submit');
    refine_results_button.addEventListener('click', delete_html);
    refine_results_button.addEventListener('click', get_movies_with_refine_filters);

    let search_category = ''
    let search_category_value_first_caps = ''
    // split URL and get search values sent from homepage
    if (window.location.search.split('?')){
        let url = window.location.search.split('?');
        if (url[1].split('=')){
            let values_url = url[1].split('=')
        
        search_category = values_url[0]
        let search_category_value = values_url[1];
        search_category_value_first_caps = search_category_value.charAt(0).toUpperCase() + search_category_value.slice(1)
        let query_parameters = `${search_category}=${search_category_value_first_caps}`

        // if there are values in the url, fetch the movies that match that param 
        if (values_url){
            change_html_for_results_header(search_category, search_category_value_first_caps)
            if (search_category == 'all') {
                fetch_movies_all(search_category_value)
            } else {
                fetch_movies(query_parameters)
            }
            
        }
        }    
    }
    const category_labels = get_category_labels()

    for (label in category_labels) {    
        if (["genres", "languages", "countries"].includes(category_labels[label])) {
            fetch_dropdown_items(category_labels[label], search_category, search_category_value_first_caps)
        } else {
            set_category_value_by_url(search_category, search_category_value_first_caps)
        }
    }  
}


function set_category_value_by_url(search_category, search_category_value_first_caps) {
    var initialized_category = document.getElementById(`${search_category}`)
    initialized_category.value = search_category_value_first_caps
}
 
function get_category_labels() {
    return ['genres', 'languages', 'countries', 'title', 'years', 'rating']
}

function get_api_base_url(){
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

// Fetch the options for "genres", "language", and "countries" from the api
function fetch_dropdown_items(key, search_category, search_category_value) {
    var url = get_api_base_url() + `/${key}`;
    let dropdown_list = []
    fetch(url, {method: 'get'})

    .then((response) => response.json())

 
    .then(function(items) {
        dropdown_list = items
        create_dropdown_options(key, items)
    })

    .then(function() {
        if (dropdown_list.includes(search_category_value)) {
            set_category_value_by_url(search_category, search_category_value)
        }
    })

    .catch(function(error) {
        console.log(error);
    });

}

// Use the categories fetched from the api to populate the "genres", "language", and "countries" dropwdowns
function create_dropdown_options(dropdown_label, fetched_dropdown_label_options){
    var dropdown_element = document.getElementById(`${dropdown_label}`);
    var option_element = document.createElement("option");
    // this is the default value for all dropdowns
    option_element.text = 'All';
    dropdown_element.options.add(option_element);
    for(option in fetched_dropdown_label_options){
        var option_element = document.createElement("option");
        option_element.text = fetched_dropdown_label_options[option];
        dropdown_element.options.add(option_element);
    }
}

function fetch_movies_all(endpoint_parameters) {
    var url = get_api_base_url() + `/movies/all/${endpoint_parameters}`;
    console.log(url)

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        num_results_displayed = 11
        if (movies.length <= 10) {
            num_results_displayed = movies.length
        } 
        // Make global variable timesCLicked that is the amount of times the loadmore button is clicked
        // create the button and add an event listener that increments timesClicked -> load_more_Results()
        // every time timesClicked is incremented, load_more_results i_Start += 10 IF the movies remaining >= 11
        // load_more_results(0, movies)
        for (let i = 0; i < num_results_displayed; i++){
            create_html(movies[i].title, movies[i].rating, movies[i].release_year, movies[i].id, movies[i].poster_path)
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}


function load_more_results(i_start, movies) {
    num_results_displayed = 11
    if (movies.length <= 10) {
        num_results_displayed = movies.length
    } 
    for (let i = i_start; i < num_results_displayed; i++){
        create_html(movies[i].title, movies[i].rating, movies[i].release_year, movies[i].id, movies[i].poster_path)

    }
}

// Fetches the movies that match the corresponding endpoint paramters for /movies and call create_html
function fetch_movies(endpoint_parameters) {
    var url = get_api_base_url() + `/movies?${endpoint_parameters}`;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        if (movies[0]){
            for (let i = 0; i < 20; i++){
                create_html(movies[i].title, movies[i].rating, movies[i].release_year, movies[i].id, movies[i].poster_path)
            }
        } 
        else{
            create_html_no_results()
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}


// Get filters selected by user from refine results, create revised endpoint parameters, and call fetch_movies()
function get_movies_with_refine_filters(){
    filters_list = get_filters()
    category_labels = get_category_labels()
    endpoint_parameters = ``
    for (let i = 0; i < filters_list.length; i++){
        filter = capitalize_first_letter(filters_list[i])
        label = category_labels[i]
        if (filter != 'All' && filter != ''){
            search_string = `${label}=${filter}&`
            endpoint_parameters += search_string 
        }
        
    }
    endpoint_parameters = endpoint_parameters.substring(0, endpoint_parameters.length - 1);
    fetch_movies(endpoint_parameters)
    change_html_for_results_header("", "")
    
}


function capitalize_first_letter(string){
    string.charAt(0).toUpperCase() + string
    return string
}

// Gets value associated with each category in refine results and returns it as a list in the following order: 'genres', 'languages', 'countries', 'title', 'years', 'rating'
function get_filters(){
    filters_list = []

    category_labels = get_category_labels()
    for (label in category_labels){
        category_labels[label] = document.getElementById(`${category_labels[label]}`).value;
            filters_list.push(category_labels[label])
        
    }
    return filters_list

}


function change_html_for_results_header(key, input) {
    var results = document.getElementById('results_title'); 
    // Changing header after initial homepage user search 
    if (key != '' && input != '') {
        input = input.replace(/%20/g, " ");
        results.innerText = `Results for ${key}: "${input}"`
    } 
    // Changing the header after using refine results
    else {
        results.innerText = `Refined Results`
    }
    
}

// For one movie, create a card with the title, rating, release year, and the image (poster path) and add CSS properties
function create_html(title, rating, release_year, id, poster_path){
    let main_content_div = document.getElementById('main-div');
    let card_div = document.createElement('div');
    card_div.setAttribute('id', 'card_div')
    let card = document.createElement('div');
    card.classList.add('movie-card')

    let image = document.createElement('img');
    image.classList.add('movie-image', 'secondary-color')
    image.src = `https://image.tmdb.org/t/p/w185${poster_path}`

    let main_info = document.createElement('div');
    main_info.classList.add('movie-card-margin')

    let rating_div = document.createElement('div');

    let movie_title = document.createElement('h3');
    let title_text = document.createTextNode(title);
    movie_title.appendChild(title_text)
    main_info.appendChild(movie_title);

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
    if (rating == 0) {
        rating = 'Unrated'
    }
    let rating_text = document.createTextNode(rating);
    movie_rating.appendChild(rating_text)
    rating_div.appendChild(movie_rating);
    
    card.appendChild(image);
    card.appendChild(main_info);
    card.appendChild(rating_div);
    card_div.appendChild(card)
    main_content_div.appendChild(card_div)

}

// Delete all current card movies (triggered after the user hits search button)
function delete_html(){
    let myNode = document.getElementById('main-div');
    while (myNode.firstChild) {
        myNode.removeChild(myNode.lastChild);
      }
}

// If there are no movies returned from the API call, display a helpful error message
function create_html_no_results() {
    let main_content_div = document.getElementById('main-div');
    let message = document.createElement('p');
    message.innerHTML = 'Sorry, it looks like there were no great matches for your search.<br><br> Try checking your spelling or searching for something else.';
    message.classList.add('instructions')

   
    // message.appendChild(message_text)
    main_content_div.appendChild(message);

}

