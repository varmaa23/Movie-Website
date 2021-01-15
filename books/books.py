import csv
import re
import argparse

BooksDataSet = []

with open('books.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:

        title = row[0]
        publicaton_year = row[1]
        author = row[2]

        regex = "\s\((.*)\)"
        if (author.find(" and ") == -1):
            author = re.sub(regex, "", author)
        else:
            author = author.split(" and ")
            for i in range(0, len(author)):
                author[i] = re.sub(regex, "", author[i])

        BooksDataSet.append([title, publicaton_year, author])


def convertStringToInt(year):
    if len(year) == 4:
        try:
            int_year = int(year)
            return int_year
        except:
            print("Please input an integer")


def find_authors(author_input):
    authors_array = []
    for book in BooksDataSet:
        author = book[2]
        title = book[0]
        if type(author) is str and author.lower().find(author_input.lower()) != -1:
            authors_array.append([author, title])
        elif type(author) is list:
            for authorIndex in range(len(author)):
                if author[authorIndex].lower().find(author_input.lower()) != -1:
                    authors_array.append(book)
    return authors_array


def find_titles(title_input):
    title_array = []
    for book in BooksDataSet:
        title = book[0]
        if type(title) is str and title.lower().find(title_input.lower()) != -1:
            title_array.append(book)
    return title_array


def find_years(year1, year2):
    books_array = []
    year1 = convertStringToInt(year1)
    year2 = convertStringToInt(year2)
    for book in BooksDataSet:
        publicaton_year = book[1]
        if year1 <= int(publicaton_year) <= year2 or year2 <= int(publicaton_year) <= year1:
            books_array.append(book)
    return books_array


def display_find_years_results(books_array):
    sorted_array = sorted(books_array, key=lambda x: x[1], reverse=True)
    for book in sorted_array:
        print(f'{book[1]}: "{book[0]}" by {book[2]}')


def display_find_titles_results(title_array):
    sorted_array = sorted(title_array, key=lambda x: x[0])
    for book in sorted_array:
        print(f'"{book[0]}" by {book[2]}')


def display_find_authors_results(author_array):
    sorted_array = sorted(author_array, key=lambda x: x[0])
    first = True
    for index in range(len(sorted_array)-1):
        author = sorted_array[index][0]
        title = sorted_array[index][1]
        next_book_author = sorted_array[index+1][0]
        if first:
            print(f'{author}')
            first = False

        print(f'{author}, "{title}"')
        if author != next_book_author:
            print("")
            first = True




def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--author", action="store_true")
    group.add_argument("-t", "--title", action="store_true")
    group.add_argument("-y", "--year", action="store_true")
    parser.add_argument("Input", nargs="*", type=str, help="The search string")
    # parser.add_argument("Input", type=int, help="The search string", required=False)
    args = parser.parse_args()

    first_input = args.Input[0]

    if len(args.Input) == 1:
        if args.author:
            display_find_authors_results(find_authors(first_input))
        elif args.title:
            print(f'Results for titles that match the following string: {first_input}')
            display_find_titles_results(find_titles(first_input))
        else:
            print("Use either --author or --title")
    elif len(args.Input) == 2:
        if args.year:
            second_input = args.Input[1]
            print(f'Results for books published between: {first_input, second_input}')
            display_find_years_results(find_years(first_input, second_input))
        else:
            print("For two arguments, you must use --year")
    else:
        print("Error")


main()


