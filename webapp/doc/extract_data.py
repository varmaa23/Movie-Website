import csv


# for movies, 1) add movie to movies_table, 2) set ID of each movie, 
def get_data(file_name):
    movies_table = []
    with open(file_name, mode="r") as file:
        movie_data = csv.reader(file, delimiter=",")
        headers = next(movie_data)
        headers = remove_extra_line_info(headers)
        print(headers)
        for line in movie_data:
        	if remove_extra_line_info(line):
		        line = remove_extra_line_info(line)
		        movies_table.append(line)
        return movies_table

def remove_extra_line_info(line):
	count = 0
	
	if line[0] != 'False':
		return False
	if line[0] == 'False':
	    line2 = line[2:4] + line[6:8] + [line[9]] + line[11:18] + [line[20]] + [line[22]]
	    count += 1
	    return line2



def make_unique_movie():
    pass


def create_csv(table, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)


def main():
    movies = get_data('movies_metadata.csv')
    print(movies)

if __name__ == "__main__":
    results = main()
    print(results)