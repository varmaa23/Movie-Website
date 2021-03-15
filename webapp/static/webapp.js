// Authors: Valentina Guerrero and Aishwarya Varma

window.onload = initialize;

function initialize() {
    var button = document.getElementById('submit_button');
    if (button) {
        
        button.addEventListener('click', display_movie_info);
    }
    
}


function display_movie_info(){
    const input_value = document.getElementById('input').value;
    fetch_information(input_value);
    delete_html();
}

function delete_html(){
    let main_content_div = document.getElementById('content-div');
    main_content_div.removeChild(main_content_div.childNodes[0]);    
}

function get_api_base_url(){
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function fetch_information(input_value) {
    var url = get_api_base_url() + `/movie/${input_value}`;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movie) {
       create_html(movie.title, movie.overview, movie.budget, movie.revenue, movie.imbd_id, movie.rating, movie.runtime, movie.release_year, movie.poster_path)
        
    })

    .catch(function(error) {
        console.log(error);
    });
}

function create_html(movie_title, movie_overview, movie_budget, movie_revenue, movie_imbd_id, movie_rating, movie_runtime, movie_release_year, movie_poster_path){
    let main_content_div = document.getElementById('content-div');
    let main_button = document.createElement('div');
    let title = document.createElement('p');
    let title_text = document.createTextNode('Title: ' + movie_title);
    title.appendChild(title_text); 
    main_button.appendChild(title);

    let overview = document.createElement('p');
    let overview_text = document.createTextNode('Overview: ' + movie_overview);
    overview.appendChild(overview_text); 
    main_button.appendChild(overview);
    
    let budget = document.createElement('p');
    let budget_text = document.createTextNode('Budget: ' + movie_budget);
    budget.appendChild(budget_text); 
    main_button.appendChild(budget);
    
    let revenue = document.createElement('p');
    let revenue_text = document.createTextNode('Revenue: ' + movie_revenue);
    revenue.appendChild(revenue_text); 
    main_button.appendChild(revenue);
    
    let imbd_id = document.createElement('p');
    let imbd_id_text = document.createTextNode('imbd_id: ' + movie_imbd_id);
    imbd_id.appendChild(imbd_id_text); 
    main_button.appendChild(imbd_id);
    
    let rating = document.createElement('p');
    let rating_text = document.createTextNode('Rating: ' + movie_rating);
    rating.appendChild(rating_text); 
    main_button.appendChild(rating);

    let runtime = document.createElement('p');
    let runtime_text = document.createTextNode('Runtime: ' + movie_runtime);
    runtime.appendChild(runtime_text); 
    main_button.appendChild(runtime);

    let release_year = document.createElement('p');
    let release_year_text = document.createTextNode('Release Year: ' + movie_release_year);
    release_year.appendChild(release_year_text); 
    main_button.appendChild(release_year);

    let poster_path = document.createElement('p');
    let poster_path_text = document.createTextNode('Poster Path: ' + movie_poster_path);
    poster_path.appendChild(poster_path_text); 
    main_button.appendChild(poster_path);
    
    main_content_div.appendChild(main_button);


}