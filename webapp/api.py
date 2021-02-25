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


@api.route('/hello/') 
def get_dogs():
    dogs = [{'name':'Ruby', 'birth_year':2003, 'death_year':2016, 'description':'a very good dog'},
            {'name':'Maisie', 'birth_year':2017, 'death_year':None, 'description':'a very good dog'}]
    return json.dumps(dogs)
