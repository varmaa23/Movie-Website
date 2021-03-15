
// Authors: Valentina Guerrero and Aishwarya Varma

window.onload = initialize;

function initialize() {
    let button = document.getElementById('button');
    let all = document.getElementById('all');
    let title = document.getElementById('title');
    let genres = document.getElementById('genres');
    let languages = document.getElementById('languages');
    let companies = document.getElementById('companies');
    let years = document.getElementById('years');
    let input = document.getElementById('input');

    let dropdown_list = [all, title, genres, languages, companies, years]

    dropdown_list_index = 0
    dropdown_list[dropdown_list_index].classList.add('select')

    // Down and up arrow functionality for the input bar
    input.addEventListener('keydown', (event) => {
        dropdown_list[dropdown_list_index].classList.remove('select')
        // Down
        if (event.keyCode == 40) {
            dropdown_list_index = (dropdown_list_index + 1) % dropdown_list.length
        }
        // Up
        else if (event.keyCode == 38) {
            if (dropdown_list_index - 1 < 0) {
                dropdown_list_index = dropdown_list.length
            }
            dropdown_list_index = (dropdown_list_index - 1) % dropdown_list.length
        }
        dropdown_list[dropdown_list_index].classList.add('select')
    })

    // Enter key for input
    input.addEventListener('keypress', function (event) {
        if (event.keyCode === 13 && input.value) {
          event.preventDefault();
          dropdown_list.forEach((dropdown) => {
              if (dropdown.classList.contains('select')) {
                  set_url(dropdown.id)
              }
          })
        }
    });

    // Change the text inside the bar that appears under input for each category
    input.addEventListener('input', (event) => {
        
        header_html_dict = {
            'All: ': all,
            'Title: ': title,
            'Genre: ': genres,
            'Language: ': languages,
            'Production: ': companies,
            'Year: ': years
        }
        if (event.target.value) {
            change_inner_text(event, header_html_dict, true)
        } else {
            change_inner_text(event, header_html_dict, false)
        }
        
    });

    // Search Button takes whatever option is 'hovered' over and uses that to search
    button.addEventListener('click', (event) => {
        event.preventDefault()
        dropdown_list.forEach((dropdown) => {
            if (dropdown.classList.contains('select')) {
                set_url(dropdown.id)
            }
        })
    })

    // The following allows click functionality for each option as well:
    all.addEventListener('click', function() {
        set_url('all')
    })

    title.addEventListener('click', function(){
        set_url('title')
    })
    genres.addEventListener('click', function(){
        set_url('genres')
    })
    languages.addEventListener('click', function(){
        set_url('languages')
    })
    companies.addEventListener('click', function(){
        set_url('companies')
    })
    years.addEventListener('click', function(){
        set_url('years')
    })



}


const change_inner_text = (event, header_html_dict, isValue) => {
    for (let [key, value] of Object.entries(header_html_dict)) {
        if (isValue){
            value.classList.add('show')
            value.innerHTML = `${key}` +  event.target.value
        } else {
            value.classList.remove("show");
            value.classList.add('home-dropdown')
        }
        
    }
}


// Set url based on the values provided in input and load the results page accordingly
function set_url (endpoint){
    let url_input =  input.value;
    protocol = window.location.protocol
    hostname = window.location.hostname
    port = window.location.port

    url = `${protocol}//${hostname}:${port}/results?${endpoint}=${url_input}`
   
    window.open(url, "_self")

}




