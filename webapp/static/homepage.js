
// Authors: Valentina Guerrero and Aishwarya Varma
window.onload = initialize;

function initialize() {
    let button = document.getElementById('button');
    let search_all = document.getElementById('all');
    let title = document.getElementById('title');
    let genre = document.getElementById('genre');
    let language = document.getElementById('language');
    let company = document.getElementById('company');
    let year = document.getElementById('year');
    let input = document.getElementById('input');
    
    input.addEventListener('input', (event) => {
        
        header_html_dict = {
            'All: ': all,
            'Title: ': title,
            'Genre: ': genre,
            'Language: ': language,
            'Production: ': company,
            'Year: ': year
        }
        change_inner_text(event, header_html_dict)
        
        
    });

    search_all.addEventListener('click', function() {
        set_url('all')
    })

    title.addEventListener('click', function(){
        set_url('title')
    })
    genre.addEventListener('click', function(){
        set_url('genres')
    })
    language.addEventListener('click', function(){
        set_url('languages')
    })
    company.addEventListener('click', function(){
        set_url('companies')
    })
    year.addEventListener('click', function(){
        set_url('years')
    })



}


const change_inner_text = (event, header_html_dict) => {
    for (let [key, value] of Object.entries(header_html_dict)) {
        value.classList.add('show')
        value.innerHTML = `${key}` +  event.target.value
    }
}



function set_url (endpoint){
    let url_input =  input.value;
    protocol = window.location.protocol
    hostname = window.location.hostname
    port = window.location.port

    url = `${protocol}//${hostname}:${port}/results?${endpoint}=${url_input}`
   
    window.open(url, "_self")

}




