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

from create_queries import create_movie_table_query

def connect_database():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        return connection
    except Exception as e:
        print(e)
        exit()
    

@api.route('/movies') 
def get_movies():
    movies =[]
    # http://localhost:5000/api/movies?title=tes&language=es
    title = flask.request.args.get('title')
    budget = flask.request.args.get('budget')
    language = flask.request.args.get('languages')
    rating = flask.request.args.get('rating')
    company = flask.request.args.get('company')
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
        movies.rating
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
                'rating': float(row[3])
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
    movies = []
    connection = connect_database()
    query = '''SELECT * FROM movies WHERE id = {};'''.format(movie_id)

    try:
        cursor = connection.cursor()
        cursor.execute(query)
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
        movies.append(movie_dict)
            
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
    return flask.render_template('help.txt')
    

