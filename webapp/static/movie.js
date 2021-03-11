window.onload = initialize;

function initialize() {

var title= document.getElementById('title');
var rating = document.getElementById('rating');
var languages = document.getElementById('languages');
var genres = document.getElementById('genres');
var years = document.getElementById('years');
var runtime = document.getElementById('runtime');
var storyline = document.getElementById('storyline');
var revenue = document.getElementById('revenue');
var budget = document.getElementById('budget');
var country = document.getElementById('country');
var company = document.getElementById('company');



let url = window.location.search.split('?');
let values_url = url[1].split('=')

let id_value = values_url[1];

if (values_url){
    fetch_movies(id_value)
}
   
}


function get_api_base_url(){
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function fetch_movies(id_value) {
    
    var url = get_api_base_url() + `/movie/${id_value}`;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movie) {
       change_html(movie.title, movie.overview, movie.budget, movie.revenue, movie.rating, movie.runtime, movie.release_year, movie.genres, movie.languages, movie.companies, movie.countries)
    })

    .catch(function(error) {
        console.log(error);
    });
}


function change_html(movie_title, movie_overview, movie_budget, movie_revenue, movie_rating, movie_runtime, movie_years, movie_genres, movie_languages, movie_companies, movie_countries){
    title.innerText = movie_title
    storyline.innerText = movie_overview
    if (movie_revenue == 0) {
        movie_revenue = ' NULL'
    }
    revenue.innerText = movie_revenue
    if (movie_budget == 0) {
        movie_budget = ' NULL'
    }
    budget.innerText = movie_budget
    if (movie_rating == 0) {
        movie_rating = 'Unrated'
    }
    rating.innerText = movie_rating
    if (movie_runtime == 0) {
        movie_runtime = 'NULL'
    }
    runtime.innerText = movie_runtime
    years.innerText = movie_years
    genres.innerText = movie_genres
    languages.innerText = movie_languages
    companies.innerText = movie_companies
    countries.innerText = movie_countries
}