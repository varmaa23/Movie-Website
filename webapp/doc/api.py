'''
    books_webapp.py
    Jeff Ondich, 25 April 2016
    Updated 4 November 2020

    Tiny Flask API to support the tiny books web application.
'''
import sys
import flask
import json
#import config
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
    

@api.route('/movie/movie_id') 
def get_movie(movie_id):
    connection = connect_database()
    query = '''SELECT * FROM movies WHERE movie_id = {};'''.format(movie_id)

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor
    except Exception as e:
        print(e)
        exit()

    return json.dumps("hello2")
