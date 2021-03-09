def create_movie_table_query(items_dictionary):
    query_dictionary = {}
    language_string = ''
    numbers = ['rating', 'revenue', 'runtime', 'release_year', 'budget']
    for item in items_dictionary:
        if items_dictionary[item]:
            if item not in numbers:
                query_dictionary[item] = "LIKE '%{}%'".format(items_dictionary[item])
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
    print(query_skeleton)
    return query_skeleton

def create_genres_table_query(movie_title):
    query = '''
    SELECT genres.genre
    FROM 
    movies,
    genres,
    movie_genres
    WHERE
    movies.title {}
    AND
    movies.id = movie_genres.movie_id
    AND 
    movie_genres.genre_id = genres.id
    ;'''.format(movie_title)

    return query



        