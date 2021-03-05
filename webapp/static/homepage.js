// Authors: Valentina Guerrero and Aishwarya Varma
window.onload = initialize;

function initialize() {
    let button = document.getElementById('button');
    let title = document.getElementById('title');
    let genre = document.getElementById('genre');
    let company = document.getElementById('company');
    let input = document.getElementById('input');
    input.addEventListener('input', (event) => {
        console.log(event.target.value)
        title.classList.add('show')
        genre.classList.add('show')
        company.classList.add('show')
        title.innerText = 'Title: ' + event.target.value
        genre.innerText = 'Genre: ' + event.target.value
        company.innerText = 'Company: ' + event.target.value
    });

    
}