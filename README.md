# Movie-Website
## Authors: Aishwarya Varma and Valentina Guerrero

## Dataset:  
<https://www.kaggle.com/rounakbanik/the-movies-dataset/>
<br/>
License: CC0: Public Domain
<br/>
In order to view the dataset, click the link and download movies_metadata.csv.
This dataset contains information about a list of around 45,000 movies, including information about their genre, production companies, revenue, languages, spoken languages, release dates, ratings, movie posters, and a synopsis.

## How to use
1. cd into /webapp
2. run `psql` in the terminal
3. create movies database in psql using\
`CREATE DATABASE movies;`
3. quit out of psql\
`\q`
4. Dump our data into your recently created database\
`psql -U YOURUSER movies < data.sql`
5. Fill in your psql user, password, and the name of the database that you just created in config.py\
e.g.\
`user = 'test_user'`\
`password = '1234'`\
`database = 'movies'`
6. Run the program using the following command:\
`python3 app.py localhost 5010`

## Features 
* Home Page allows you to filter through title, genre, production company, country, languages, and release year fields to find a particular movie. You can also search all of these fields using the 'All' option.
* Results Page filters through list of movies correctly.
* Use Refine Results Page also properly filters through results.
* Advanced Search correctly allows you to filter through all the fields (title, genre, production company, languages, country, runtime, budget, revenue, and release year)
* When you click 'view more', you can see the individual fields for a movie.

## Images
![Home](home.png?raw=true "HomePage Search")\
![Results](results.png?raw=true "Results Page")\
![Movie](movie.png?raw=true "Individual Movie")\
![Advances Search](advances.png?raw=true "Advanced Search")


