'''
    Authors:
    Valentina Guerrero
    Aishwarya Varma 
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

from config import password
from config import database
from config import user

from create_queries import create_movie_table_query, create_genres_table_query, create_search_all_query

def connect_database():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        return connection
    except Exception as e:
        print(e)
        exit()
    
@api.route('movies/all/<keyword>') 
def search_all(keyword):
    movies =[]

    where_portion = create_search_all_query(keyword)
    query = '''SELECT id, title, release_year, rating, poster_path FROM movies WHERE {};'''.format(where_portion)
    
    genre_query = ''' 
    SELECT 
    movies.id, movies.title, movies.release_year, movies.rating, movies.poster_path
    FROM 
    movies,
    genres,
    movie_genres
    WHERE
    genres.genre LIKE '%{}%'
    AND
    movies.id = movie_genres.movie_id
    AND
    movie_genres.genre_id = genres.id
    '''.format(keyword)

    language_query = ''' 
    SELECT 
    movies.id, movies.title, movies.release_year, movies.rating, movies.poster_path
    FROM 
    movies,
    languages,
    movie_langs
    WHERE
    languages.lang_full LIKE '%{}%'
    AND
    movies.id = movie_langs.movie_id
    AND
    movie_langs.lang_id = languages.id
    '''.format(keyword)

    countries_query = ''' 
    SELECT 
    movies.id, movies.title, movies.release_year, movies.rating, movies.poster_path
    FROM 
    movies,
    countries,
    movie_countries
    WHERE
    countries.country_name LIKE '%{}%'
    AND
    movies.id = movie_countries.movie_id
    AND
    movie_countries.country_id = countries.id
    '''.format(keyword)

    companies_query = ''' 
    SELECT 
    movies.id, movies.title, movies.release_year, movies.rating, movies.poster_path
    FROM 
    movies,
    companies,
    movie_companies
    WHERE
    companies.company_name LIKE '%{}%'
    AND
    movies.id = movie_companies.movie_id
    AND
    movie_companies.company_id = companies.id
    '''.format(keyword)


    movies_results = run_query(query, movies)
    movies_updated_genre = run_query(genre_query, movies_results)
    movies_updated_languages = run_query(language_query,movies_updated_genre )
    movies_updated_countries = run_query(countries_query, movies_updated_languages)
    movies_updated_companies = run_query(companies_query, movies_updated_countries)

   
    return json.dumps(movies_updated_companies)



def run_query(query, results_list):
    
    connection = connect_database()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            movie_dict = {
                'id': row[0],
                'title': row[1],
                'release_year': row[2],
                'rating': float(row[3]),
                'poster_path': str(row[4])
            }
            results_list.append(movie_dict)
            
    except Exception as e:
        print(e)
        exit()
    return results_list

@api.route('/movies') 
def get_movies():
    movies =[]
    # http://localhost:5000/api/movies?title=tes&language=es
    title = flask.request.args.get('title')
    budget = flask.request.args.get('budget')
    language = flask.request.args.get('languages')
    rating = flask.request.args.get('rating')
    company = flask.request.args.get('companies')
    country = flask.request.args.get('countries')
    release_year = flask.request.args.get('years')
    revenue = flask.request.args.get('revenue')
    runtime = flask.request.args.get('runtime')
    genre = flask.request.args.get('genres')

    connection = connect_database()

    where_portion = create_movie_table_query({
        'title': title,
        'rating': rating,
        'revenue': revenue,
        'runtime': runtime,
        'release_year': release_year,
        'budget': budget,
        'language': language,
        'country': country,
        'company': company,
        'genre': genre
    })
    print(where_portion)
    
    query = '''SELECT DISTINCT
        movies.id, 
        movies.title,
        movies.release_year,
        movies.rating,
        movies.poster_path
        FROM 
        movies,
        languages,
	    movie_langs,
        countries,
        movie_countries,
        companies,
        movie_companies,
        genres,
        movie_genres
        WHERE {}
        ORDER BY movies.release_year DESC
        ;'''.format(where_portion)

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            movie_dict = {
                'id': row[0],
                'title': row[1],
                'release_year': row[2],
                'rating': float(row[3]),
                'poster_path': str(row[4])
            }
            movies.append(movie_dict)
            
    except Exception as e:
        print(e)
        exit()

    return json.dumps(movies)

@api.route('/hello') 
def get_hello():
    message = 'hey there'
    return json.dumps(message)



@api.route('/movie/<movie_id>') 
def get_movie(movie_id):
    movie_dict = {}
    connection = connect_database()

    genre_query = '''
    SELECT genres.genre
    FROM 
    movies,
    genres,
    movie_genres
    WHERE
    movies.id = {}
    AND
    movies.id = movie_genres.movie_id
    AND
    movie_genres.genre_id = genres.id
    ;'''.format(movie_id)

    language_query = '''
    SELECT languages.lang_full
    FROM 
    movies,
    languages,
    movie_langs
    WHERE 
    movies.id = {}
    AND
    movies.id = movie_langs.movie_id
    AND
    movie_langs.lang_id = languages.id
    ;'''.format(movie_id)

    countries_query = '''
    SELECT countries.country_name
    FROM 
    countries,
    movies,
    movie_countries
    WHERE 
    movies.id = {}
    AND 
    movies.id = movie_countries.movie_id
    AND
    movie_countries.country_id = countries.id
    ;'''.format(movie_id)

    companies_query = '''
    SELECT companies.company_name
    FROM 
    companies,
    movies,
    movie_companies
    WHERE 
    movies.id = {}
    AND 
    movies.id = movie_companies.movie_id
    AND
    movie_companies.company_id = companies.id
    ;'''.format(movie_id)

    movie_query = '''SELECT * FROM movies WHERE id = {};'''.format(movie_id)



    try:
        cursor = connection.cursor()
        cursor.execute(movie_query)
        
       
        for row in cursor:
            movie_dict = { 
            'id': row[0],
            'title': row[1],
            'overview': row[2],
            'budget': float(row[3]),
            'revenue': float(row[4]),
            'imbd_id':row[5],
            'rating': float(row[6]),
            'runtime': float(row[7]),
            'release_year': int(row[8]),
            'poster_path': row[9]
            }

        cursor.execute(genre_query)
        genres = []
        for row in cursor:
            genres.append(row)
        movie_dict['genres'] = genres

        cursor.execute(language_query)
        languages = []
        for row in cursor:
            languages.append(row)
        movie_dict['languages'] = languages

        cursor.execute(countries_query)
        countries = []
        for row in cursor:
            countries.append(row)
        movie_dict['countries'] = countries

        cursor.execute(companies_query)
        companies = []
        for row in cursor:
            companies.append(row)
        movie_dict['companies'] = companies
            
    except Exception as e:
        print(e)
        exit()

    return json.dumps(movie_dict)


@api.route('/genres') 
def get_genres():
    genres = []
    connection = connect_database()
    query = '''SELECT * FROM genres;'''

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            genres.append(row[1])
            
    except Exception as e:
        print(e)
        exit()

    return json.dumps(genres)


@api.route('/languages') 
def get_languages():
    languages = []
    connection = connect_database()
    query = '''SELECT * FROM languages;'''

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            languages.append(row[2])
            
    except Exception as e:
        print(e)
        exit()

    return json.dumps(languages)

@api.route('/countries') 
def get_countries():
    countries = []
    connection = connect_database()
    query = '''SELECT * FROM countries;'''

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            countries.append(row[1])
            
    except Exception as e:
        print(e)
        exit()

    return json.dumps(countries)

@api.route('/help') 
def display_help():
    return flask.render_template('help.html')
    

