def create_movie_table_query(items_dictionary):
    query_dictionary = {}
    for item in items_dictionary:
        if items_dictionary[item]:
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
    '''.format(query_dictionary['title'], query_dictionary['rating'], query_dictionary['revenue'], query_dictionary['runtime'], query_dictionary['release_year'], query_dictionary['budget'])
    
    return query_skeleton




        