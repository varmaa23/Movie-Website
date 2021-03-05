
// Authors: Valentina Guerrero and Aishwarya Varma
window.onload = initialize;

function initialize() {
    let button = document.getElementById('button');
    let title = document.getElementById('title');
    let genre = document.getElementById('genre');
    let language = document.getElementById('company');
    let input = document.getElementById('input');
    let url_input =  capitalize_first_letter(input.value);
    //genre.href = `${url}:${port}/results?genre=${input.value}`;
    input.addEventListener('input', (event) => {
        console.log(event.target.value)
        //title.classList.add('show')
        genre.classList.add('show')
        language.classList.add('show')
        //title.innerText = 'Title: ' + event.target.value
        genre.innerText = 'Genre: ' + event.target.value
        language.innerText = 'Language: ' + event.target.value

        //title.addEventListener('click', get_movies);
        genre.addEventListener('click', search_by_genre);
        //language.addEventListener('click', get_movies);

    });

    
}


const capitalize_first_letter = (string) => {
    string.charAt(0).toUpperCase() + string
    return string
}

function search_by_genre(){
    let url_input =  capitalize_first_letter(input.value);
    protocol = window.location.protocol
    hostname = window.location.hostname
    port = window.location.port
    value = capitalize_first_letter(input.value)

    url = `${protocol}//${hostname}:${port}/results?genres=${url_input}`
   
    window.open(url, "_self")

}




