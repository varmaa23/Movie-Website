'''
    books_webapp.py
    Jeff Ondich, 25 April 2016
    Updated 4 November 2020

    Tiny Flask API to support the tiny books web application.
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

def connect_database():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        return connection
    except Exception as e:
        print(e)
        exit()
    

@api.route('/movies') 
def get_movies():
    # http://localhost:5000/api/movies?title=tes&language=es
    title = flask.request.args.get('title')
    language = flask.request.args.get('language')
    rating = flask.request.args.get('rating')
    company = flask.request.args.get('company')
    country = flask.request.args.get('country')
    years = flask.request.args.get('years')
    languages = flask.request.args.get('languages')
    renevue = flask.request.args.get('revenue')
    genre = flask.request.args.get('genre')

    message={
        'title': title,
        'language': language,
        'rating': rating,
        'company': company,
    }

    query = '''SELECT movies.movie_id, 
        movies.title,
        movies.poster_path,
        movies.year,
        movies.genre,
        movies.rating
        FROM 
            movies,
            languages,
            companies,
            countries,
            genres,
            movie_langs,
            movie_companies,
            movie_countries,
            movie_genres
        WHERE 
        
        
        ;'''

    return json.dumps(message)

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


