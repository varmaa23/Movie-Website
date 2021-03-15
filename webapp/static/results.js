window.onload = initialize;

// Keeps track of 
results_to_display = 0
function initialize() {

    var refine_results_button = document.getElementById('submit');
    refine_results_button.addEventListener('click', delete_html);
    refine_results_button.addEventListener('click', get_movies_with_refine_filters);
    
    
    // In case there are query parameters in the URL
    if (window.location.search.split('?')){

        // IDs of the refine results inputs and dropdowns (each one also matches the name of a parameter in the API /movies endpoint)
        const category_labels = get_category_labels()

        // List with query parameters separated by "&"
         separate_parameters=  get_separate_categories()
         
         
         for (parameters in separate_parameters){
            
            parameter_category = get_search_categories(separate_parameters[parameters])
            parameter_value = get_search_category_value(separate_parameters[parameters])
            
            change_html_for_results_header(parameter_category, parameter_value)
           
         
            for (label in category_labels){
            // In case the label corresponds to a dropdown, fetch the dropdown items from the API
            if (["genres", "languages", "countries"].includes(category_labels[label])) {
                fetch_dropdown_items(category_labels[label], parameter_category, parameter_value)
               
            } 

            // If it not a dropdown fill the value of the input according to the URL parameters 
            else if(parameter_category == 'title' || parameter_category == 'years') {

            set_category_value_by_url(parameter_category, parameter_value)


            }
        
    }
         }
        
        // Fetch movies using the URL parameters
        fetch_movies(get_query_parameters())
            
        
    }
}



// Given a parameter from the URL (for example genre=Family) extract the category. In case of the example, genre
function get_search_categories(input) {
    
        let values_url = input.split('=')
        search_category = values_url[0]
            
            return search_category
 
}

// Given a parameter from the URL (for example genre=Family) extract the value. In case of the example, Family
function get_search_category_value(input){
    
    if (input.split('=')){
        let values_url = input.split('=')
        let search_category_value = values_url[1];
        // If there's an apostrophe in the title, double it so SQL knows that the apostrophe is part of the string
        let search_category_value_first_caps = ''
        // search_category_value_list = search_category_value.replace(/%20/g, " ").split(" ")
        search_category_value_list = decodeURIComponent(search_category_value).split(" ")
        search_category_value_list.forEach((value) => {
            value = value.charAt(0).toUpperCase() + value.slice(1).replace("'", "''")
            search_category_value_first_caps += value + " "
        })
        search_category_value_first_caps = search_category_value_first_caps.slice(0, -1)

       
        return search_category_value_first_caps
    }
}



// Split URL parameters 
function get_separate_categories(){
    let url = window.location.search.split('?');
    separate_parameters = url[1].split('&')
    
    return separate_parameters
}



// Get query parameters from the URL
function get_query_parameters(){
    separate_parameters=  get_separate_categories()
    query_parameters = ''

    for (parameters in separate_parameters){
       
       parameter_category = get_search_categories(separate_parameters[parameters])
       parameter_value = get_search_category_value(separate_parameters[parameters])
       query_parameters = query_parameters + parameter_category + '=' + parameter_value + '&'}

    return query_parameters
       

}


// In refine results, set the value = to what has been searched  (URL parameters)
function set_category_value_by_url(search_category, search_category_value_first_caps) {
   
    var initialized_category = document.getElementById(`${search_category}`)
    let value_string = ''
    search_category_value_list = decodeURIComponent(search_category_value_first_caps).split(" ")
    search_category_value_list.forEach((value) => {
        value = value.charAt(0).toUpperCase() + value.slice(1).replace("''", "'")
        value_string += value + " "
    })
   
    initialized_category.value = value_string.trim()
    
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
        console.log(dropdown_list, search_category_value)
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
        if (!fetched_dropdown_label_options[option].includes('?')){
            var option_element = document.createElement("option");
            option_element.text = fetched_dropdown_label_options[option];
            dropdown_element.options.add(option_element);
        } 
    }
}




function create_load_more_button(endpoint){
    let main_content_div = document.getElementById('main-div');
    let button_div = document.createElement('div');
    button_div.setAttribute('id', 'button-div');
    let load_button = document.createElement('button');
    load_button.innerText = 'More results'
    load_button.classList.add('button', 'more-results')
    button_div.classList.add('center')
    button_div.appendChild(load_button)
    main_content_div.appendChild(button_div)


    load_button.addEventListener('click', function(){
        fetch_movies(get_query_parameters())
       
    })
   
    
}


function increase_results_to_display(){
    results_to_display += 10;
    return results_to_display
}

function load_results(movies) {

    if (results_to_display != 0){
        // In case the user has already perfomed a search and there is an existing button to load more results, remove that element
        remove_load_more_button()
    }

    updated_results_to_display = increase_results_to_display()
    
    if (movies.length <= updated_results_to_display) {
         // In case there are no more results to be displayed 
        max_results_displayed = movies.length
        for (let i = (updated_results_to_display - 10); i < max_results_displayed; i++){
            create_html(movies[i].title, movies[i].rating, movies[i].release_year, movies[i].id, movies[i].poster_path)
        }
    } 
     // In case there are results that have not been displayed 
    else{
    for (let i = (updated_results_to_display - 10); i < updated_results_to_display; i++){
        create_html(movies[i].title, movies[i].rating, movies[i].release_year, movies[i].id, movies[i].poster_path)
    }
    
    create_load_more_button()
}
}

// Fetches movies and loads results. In case there are no results, displays informative message
function fetch_movies(endpoint_parameters) {

    var url = get_api_base_url() + `/movies?${endpoint_parameters}`;


    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        if (movies[0]){
            load_results(movies)  
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
    
    // Set the URL according to the search performed by the user
    protocol = window.location.protocol
    hostname = window.location.hostname
    port = window.location.port
    url = `${protocol}//${hostname}:${port}/results?${endpoint_parameters}`
    window.location.href = url
  
    fetch_movies(endpoint_parameters, 'movies')
    change_html_for_results_header("", "")
   
}


function capitalize_first_letter(string){
    string.charAt(0).toUpperCase() + string
    return string
}

// Gets value associated with each category (could be either the default value or the value selected by the user) in refine results 
// Returns values in a list in the following order: 'genres', 'languages', 'countries', 'title', 'years', 'rating'
function get_filters(){
    filters_list = []

    category_labels = get_category_labels()
    for (label in category_labels){
        category_labels[label] = document.getElementById(`${category_labels[label]}`).value;
            filters_list.push(category_labels[label])
        
    }
    return filters_list

}

// Change the HTML so that it accurately displays what the user has searched for 
function change_html_for_results_header(key, input) {
    var results = document.getElementById('results_title'); 
    // Changing header after initial homepage user search 
    if (key != '' && input != '') {
        input = decodeURIComponent(input)
        // Replace double apostrophes used for the search query
        input = input.replace("''", "'");
        results.innerText = `Results for ${key}: "${input}"`
    } 
    // Changing the header after using refine results (if there's multiple query parameters)
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
    image.onerror = function() {
        image.src = '../static/null_movie.png'
    };
      

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
    
    movie_more.href = url
    movie_more.classList.add('view-more')
    let more_text = document.createTextNode('view more');
    
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
    // Reset results_to_display to start a fresh search and ensure load_results works properly 
    results_to_display = 0
    let myNode = document.getElementById('main-div');
    while (myNode.firstChild) {
        myNode.removeChild(myNode.lastChild);
      }
}


function remove_load_more_button(){
    let main_content_div = document.getElementById('main-div');
    let load_more_button = document.getElementById('button-div');
    main_content_div.removeChild(load_more_button)

}
// If there are no movies returned from the API call, display a helpful error message
function create_html_no_results() {
    let main_content_div = document.getElementById('main-div');
    let message = document.createElement('p');
    message.innerHTML = 'Sorry, it looks like there were no great matches for your search.<br><br> Try checking your spelling or searching for something else.';
    message.classList.add('instructions')
    
    main_content_div.appendChild(message);

}



