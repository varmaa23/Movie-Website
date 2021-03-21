'''
    Authors:
    Valentina Guerrero
    Aishwarya Varma 
'''

def create_movie_table_query(items_dictionary):
    query_dictionary = {}
    language_string = ''
    numbers = ['rating', 'revenue', 'runtime', 'release_year', 'budget']
    for item in items_dictionary:
        if items_dictionary[item]:
            if item not in numbers:
                query_dictionary[item] = "LIKE '%{}%'".format(items_dictionary[item])
            else:
                if item in ['rating', 'revenue', 'budget']:
                    query_dictionary[item] = ">= '{}' AND movies.{} > 0".format(items_dictionary[item], item)
                elif item == 'runtime':
                    query_dictionary[item] = "<= '{}' AND movies.runtime > 0 ".format(items_dictionary[item])
                else:
                    query_dictionary[item] = "= '{}'".format(items_dictionary[item])
        else:
            query_dictionary[item] = 'IS NOT NULL'


    query_skeleton = '''
        movies.title {}
        AND
        movies.rating {}
        AND
        movies.revenue {}
        AND 
        movies.runtime {}
        AND
        movies.release_year {}
        AND 
        movies.budget {}
        AND
        languages.lang_full {}
        AND 
        countries.country_name {}
        AND
        companies.company_name {}
        AND
        genres.genre {}
        AND
        movie_langs.movie_id = movies.id
        AND 
        movie_langs.lang_id = languages.id
        AND
        movie_countries.movie_id = movies.id
        AND
        movie_countries.country_id = countries.id
        AND
        movie_companies.movie_id = movies.id
        AND
        movie_companies.company_id = companies.id
        AND
        movies.id = movie_genres.movie_id
        AND
        movie_genres.genre_id = genres.id
        

    '''.format(query_dictionary['title'], query_dictionary['rating'], query_dictionary['revenue'], query_dictionary['runtime'], query_dictionary['release_year'], query_dictionary['budget'],query_dictionary['language'], query_dictionary['country'], query_dictionary['company'], query_dictionary['genre'] )
    return query_skeleton

def create_genres_table_query(movie_id):
    query = '''
    SELECT genres.genre
    FROM 
    movies,
    genres,
    movie_genres
    WHERE
    movies.id = '{}'
    
    ;'''.format(movie_id)

    return query



def create_search_all_query(search_string):
    if search_string.isnumeric():
        int_keyword = "= '{}'".format(search_string)
        string_keyword = "LIKE '%{}%'".format(search_string)
        query_skeleton = '''
            release_year {int_key}
            OR
            rating {int_key}
            OR
            runtime {int_key}
            OR
            title {string_key}


        '''.format(int_key=  int_keyword, string_key = string_keyword)
    else:
        string_keyword = "LIKE '%{}%'".format(search_string)
        query_skeleton = '''
            title {string_key}

        '''.format(string_key = string_keyword)
    return query_skeleton


def create_genre_query(keyword):
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
    return genre_query
