# Authors: Valentina Guerrero and Aishwarya Varma 
import csv
import json
import re

def get_data(file_name):
    movies_dictionary = {}
    with open(file_name, mode="r") as file:
        movie_data = csv.reader(file, delimiter=",")
        headers = remove_extra_line_info(next(movie_data))

        count = 0
        for line in movie_data:
            if remove_extra_line_info(line) and remove_extra_line_info(line) != None:
                movie_dictionary = {}
                line = remove_extra_line_info(line)
                for i in range(len(line)):
                    if headers[i] == 'release_date':
                        line[i] = clean_release_year(line[i])
                    if headers[i] == 'runtime' and line[i] == '':
                        line[i] = 0
                    movie_dictionary[headers[i]] = line[i]
                movies_dictionary[count] = movie_dictionary
                count += 1
        return movies_dictionary

def remove_extra_line_info(line):
    count = 0
    count += 1
    return line[2:4] + line[6:8] + [line[9]] + line[11:18] + [line[20]] + [line[22]]

def clean_release_year(year):
    if year == '':
        return 0
    return year[:4]

def create_movies_table(movies_dictionary):
    movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        overview = movies_dictionary.get(movie_id).get('overview')
        budget = int(movies_dictionary.get(movie_id).get('budget'))
        revenue = int(movies_dictionary.get(movie_id).get('revenue'))
        imdb_id = movies_dictionary.get(movie_id).get('imdb_id')
        rating = float(movies_dictionary.get(movie_id).get('vote_average'))
        runtime = int(float(movies_dictionary.get(movie_id).get('runtime')))
        release_year = int(movies_dictionary.get(movie_id).get('release_date'))
        poster_path = movies_dictionary.get(movie_id).get('poster_path')
        movies_table.append([movie_id, title, overview, budget, revenue, imdb_id, rating, runtime, release_year, poster_path])
    return movies_table



def create_table_from_list(movies_list):
    output_list = []
    for item in movies_list:
        for genre in item[2]:
            output_list.append([item[0], genre])
    return output_list


def get_movie_genres_table(movies_dictionary):
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('genres')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\'", "\"", element)
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('id')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('id')
                        genres_table.append([genre_id, genre_name])
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_movies_table

def create_genres_table(movies_dictionary):
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('genres')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\'", "\"", element)
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('id')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('id')
                        genres_table.append([genre_id, genre_name])
                       
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_table


def get_productioncountry_movies_table(movies_dictionary):
    count = 0
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('production_countries')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\'", "\"", element)
                    
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('iso_3166_1')
                    genre_name = genre_dict.get('name')
                    movie_genres.append(genre_name)
                    
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('iso_3166_1')
                        genres_table.append([count, genre_name])
                        count = count + 1
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_movies_table

def create_production_country_table(movies_dictionary):
    count = 0
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('production_countries')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:  
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\'", "\"", element)
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('iso_3166_1')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('iso_3166_1')
                        genres_table.append([count, genre_name])
                        count = count + 1
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_table

def get_companies_table(movies_dictionary):
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('production_companies')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                print(element)
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\(", " ", element)
                    element = re.sub("\)", " ", element)
                    string_double_quotes = re.findall('"(.*?)"', element)
                    changed = True
                    if (string_double_quotes):
                        string_single_quote = re.findall("\'", string_double_quotes[0])
                        if (string_single_quote):
                            changed = False
                            print('strange')
                            clean_string = re.sub("\'", " ", string_double_quotes[0])
                            print(clean_string)
                            element = re.sub(string_double_quotes[0], clean_string, element)

                    werid_name = re.findall("'(.*?)'", element)

                    if (werid_name and changed):
                        print('we')
                        clean_string_2 = re.sub("\"", " ", werid_name[1])
                        print(clean_string_2)
                        element = re.sub(werid_name[1], clean_string_2, element)

                    element = re.sub("\'", "\"", element)
                    print(element)
                    print('-------------')
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('id')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('id')
                        genres_table.append([genre_id, genre_name])
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_movies_table

def create_companies_table(movies_dictionary):
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('production_companies')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                print(element)
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\(", " ", element)
                    element = re.sub("\)", " ", element)
                    string_double_quotes = re.findall('"(.*?)"', element)
                    changed = True
                    if (string_double_quotes):
                        string_single_quote = re.findall("\'", string_double_quotes[0])
                        if (string_single_quote):
                            changed = False
                            print('strange')
                            clean_string = re.sub("\'", " ", string_double_quotes[0])
                            print(clean_string)
                            element = re.sub(string_double_quotes[0], clean_string, element)

                    werid_name = re.findall("'(.*?)'", element)

                    if (werid_name and changed):
                        print('we')
                        clean_string_2 = re.sub("\"", " ", werid_name[1])
                        print(clean_string_2)
                        element = re.sub(werid_name[1], clean_string_2, element)

                    element = re.sub("\'", "\"", element)
                    print(element)
                    print('-------------')
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('id')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('id')
                        genres_table.append([genre_id, genre_name])
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_table

def create_languages_table(movies_dictionary):
    count = 0
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('spoken_languages')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\'", "\"", element)
                    
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('iso_639_1')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('iso_639_1')
                        genres_table.append([count, genre_id, genre_name])
                        count = count + 1
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_table


def get_languages_table(movies_dictionary):
    count = 0
    dictionary = {}
    genres_table = []
    genres_movies_table = []
    for movie_id in movies_dictionary:
        title = movies_dictionary.get(movie_id).get('title')
        movie_genres = []
        genres = movies_dictionary.get(movie_id).get('spoken_languages')
        genres = genres[1:-1]
        regex = '(?<={ )(.*)(?=} )'
        regular = re.split(regex, genres)
        for genre in regular:
            test = genre.split(', {')
            for element in test:
                
                if element != '':
                    if element[0] != '{':
                        element = '{' + element
                    element = re.sub("\'", "\"", element)
                    genre_dict= json.loads(element) 
                    genre_id = genre_dict.get('iso_639_1')
                    movie_genres.append(genre_id)
                    genre_name = genre_dict.get('name')
                    
                    try:
                        dictionary[genre_name]
                    except:
                        dictionary[genre_name] = genre_dict.get('iso_639_1')
                        genres_table.append([count, genre_id, genre_name])
                        count = count + 1
        genres_movies_table.append([movie_id, title, movie_genres])
    return genres_movies_table

def create_csv(table, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)


def main():
    movies = get_data('movies_metadata.csv')
    create_csv(create_movies_table(movies), 'movies.csv')
    movie_genres_table = get_movie_genres_table(movies)
    movie_prodcountries_table = get_productioncountry_movies_table(movies)
    movie_languages_table = get_languages_table(movies)
    movie_companies = get_companies_table(movies)
    create_csv(create_genres_table(movies),'genres.csv')
    create_csv(create_production_country_table(movies),'countries.csv')
    create_csv(create_languages_table(movies), 'languages.csv')
    create_csv(create_companies_table(movies), 'companies.csv')
    create_csv(create_table_from_list(movie_genres_table), 'genres_movies.csv')
    create_csv(create_table_from_list(movie_prodcountries_table), 'countries_movies.csv')
    create_csv(create_table_from_list(movie_languages_table), 'languages_movies.csv')
    create_csv(create_table_from_list(movie_companies), 'companies_movies.csv')

if __name__ == "__main__":
    main()