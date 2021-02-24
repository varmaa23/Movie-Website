import csv


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


def create_csv(table, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)


def main():
    movies = get_data('movies_metadata.csv')
    create_csv(create_movies_table(movies), 'movies.csv')

if __name__ == "__main__":
    results = main()