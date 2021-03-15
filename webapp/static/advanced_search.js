// Authors: Valentina Guerrero and Aishwarya Varma

window.onload = initialize;

function initialize() {

    const category_labels = get_category_labels()

    for (label in category_labels) {    
        if (["genres", "languages", "countries"].includes(category_labels[label])) {
            fetch_dropdown_items(category_labels[label])
        } 
    }   

    var button = document.getElementById('submit');
    button.addEventListener('click', get_movies_with_advanced_filters);
    
}

function get_category_labels() {
    return ['genres', 'languages', 'countries', 'title', 'rating', 'revenue', 'budget', 'runtime', 'years']
}

function get_api_base_url(){
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

// Fetch the options for "genres", "language", and "countries" from the api
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

// Get all the filters that were provided by the user 
function get_filters(){
    filters_list = []

    category_labels = get_category_labels()
    for (label in category_labels){
        category_labels[label] = document.getElementById(`${category_labels[label]}`).value;
            filters_list.push(category_labels[label])
        
    }
    return filters_list

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

function capitalize_first_letter(string){
    string.charAt(0).toUpperCase() + string
    return string
}


// Get filters selected by user from Advanced search and go to results page
function get_movies_with_advanced_filters(event){
    event.preventDefault()
    
    filters_list = get_filters()
    category_labels = get_category_labels()
    endpoint_parameters = ``
    for (let i = 0; i < filters_list.length; i++){
        filter = capitalize_first_letter(filters_list[i]).replace('+','')
        label = category_labels[i]
        if (filter != 'All' && filter != ''){
            search_string = `${label}=${filter}&`
            endpoint_parameters += search_string 
        }
        
    }
    endpoint_parameters = endpoint_parameters.substring(0, endpoint_parameters.length - 1)

    protocol = window.location.protocol
    hostname = window.location.hostname
    port = window.location.port
    url = `${protocol}//${hostname}:${port}/results?${endpoint_parameters}`
    window.location.href = url
}
