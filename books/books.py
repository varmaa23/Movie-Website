import csv
import re
import argparse
import sys

BooksDataSet = []
file_name = 'books.csv'


# This function populates the list BooksDataSet with title, publication year, and author(s) information from books.csv.
def fillBooksDataSet(file_name):
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            title = row[0]
            publicaton_year = row[1]
            author = row[2]
            # Regular expression to find and delete the author's lifespan in parentheses by replacing it with an
            # empty string.
            regex = "\s\((.*)\)"
            # Assuming that multiple authors will be separated by the word "and", create an additional array to
            # contain them
            if author.find(" and ") != -1:
                author = author.split(" and ")
                for i in range(0, len(author)):
                    author[i] = re.sub(regex, "", author[i])
            else:
                author = re.sub(regex, "", author)

            BooksDataSet.append([title, publicaton_year, author])


# This function converts a string to an integer, given that it's four digits long.
def convertStringToInt(year):
    if len(year) == 4:
        try:
            int_year = int(year)
            return int_year
        except:
            print("Please input two valid four-digit integers")
            sys.exit()


def isList(inputVar):
    return type(inputVar) is list


def isString(inputVar):
    return type(inputVar) is str


# In the case that there's more than one author, this function converts the list of authors into a single string.
def changeAuthorListToString(author_list):
    return_string = ""
    for elementIndex in range(0, len(author_list) - 1):
        return_string += author_list[elementIndex] + ", "
    return_string += author_list[elementIndex + 1]
    return return_string


# This function returns a list of all the books (title, publication year, author) that match the author_input string
def find_authors(author_input):
    authors_array = []
    for book in BooksDataSet:
        author = book[2]
        if isString(author) and author.lower().find(author_input.lower()) != -1:
            authors_array.append(book)
        # If author is a list there is more than one author
        elif isList(author):
            for authorIndex in range(len(author)):
                if author[authorIndex].lower().find(author_input.lower()) != -1:
                    authors_array.append(book)
    return authors_array


# This function returns a list of all the books (title, publication year, author) that match the title_input string
def find_titles(title_input):
    title_array = []
    for book in BooksDataSet:
        title = book[0]
        if isString(title) and title.lower().find(title_input.lower()) != -1:
            title_array.append(book)
    return title_array


# This function returns a list of all the books (title, publication year, author) that were published between the
# range of years given via year1 and year2
def find_years(year1, year2):
    books_array = []
    year1 = convertStringToInt(year1)
    year2 = convertStringToInt(year2)
    # If the conversion happened succesfully:
    if year1 and year2:
        for book in BooksDataSet:
            publicaton_year = book[1]
            if year1 <= int(publicaton_year) <= year2 or year2 <= int(publicaton_year) <= year1:
                books_array.append(book)
    return books_array


# Given a non-empty list of books, this method displays books in order from the most recent publication date to least
# recent.
def display_find_years_results(books_array, first_input, second_input):
    # If the find_years method found any matches and returned a not empty list:
    if books_array:
        print(f'Results for books published between: {first_input, second_input}')
        sorted_array = sorted(books_array, key=lambda x: x[1], reverse=True)
        for book in sorted_array:
            title = book[0]
            publication_year = book[1]
            author = book[2]
            if (isList(author)):
                author = changeAuthorListToString(author)
            print(f'{publication_year}: "{title}" by {author}')
    else:
        print("No matches.")

# Given a non-empty list of books, this method displays books in alphabetic order
def display_find_titles_results(title_array, input):
    # If the find_titles method found any matches and returned a not empty list:
    if title_array:
        print(f'Results for titles that match the following string: {input}')
        sorted_array = sorted(title_array, key=lambda x: x[0])
        for book in sorted_array:
            title = book[0]
            author = book[2]
            if (isList(author)):
                author = changeAuthorListToString(author)
            print(f'"{title}" by {author}')
    else:
        print("No matches.")

# Given a non-empty list of books, this method displays the authors and their books
def display_find_authors_results(author_array, input):
    if author_array:
        print(f'Results for authors that match the following string: {input} \n')
        for book in author_array:
            if (isList(book[2])):
                book[2] = changeAuthorListToString(book[2])
        sorted_array = sorted(author_array, key=lambda x: x[2])
        # If the book is the first book by an author, the author's name is printed and the book's title follows.
        # However, if the book is not the first (first = False), then the book is just printed under the other books
        # the author has written.
        first = True
        for index in range(len(sorted_array)):
            author = sorted_array[index][2]
            title = sorted_array[index][0]
            # As long as the index is not the last element of the array, we can reference element @ index+1
            if index < len(sorted_array) - 1:
                next_book_author = sorted_array[index + 1][2]
            else:
                next_book_author = sorted_array[index][2]

            if first:
                print(f'{author}')
                first = False

            print(f'{author}, "{title}"')
            if author != next_book_author:
                print(" ")
                first = True
    else:
        print("No matches.")


def main():
    fillBooksDataSet(file_name)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--author", action="store_true", help="Accepts a single search string. \n Print a list "
                                                                   "of authors whose names contain the search string  "
                                                                   "")
    group.add_argument("-t", "--title", action="store_true", help="Accepts a single search string. \n Print a list of "
                                                                  "books whose titles and their "
                                                                  "corresponding authors "
                                                                  "which contain the search string")
    group.add_argument("-y", "--year", action="store_true", help="Accepts two 4-digit integers. \n Print a list of "
                                                                 "books' titles and authors published between years A "
                                                                 "and B")
    parser.add_argument("Input", nargs="*", type=str, help="The search string")

    args = parser.parse_args()

    if len(args.Input) == 0:
        print("Error. Input is required. --help for more information")
        sys.exit()

    else:
        first_input = args.Input[0]

    if len(args.Input) == 1:
        if args.author:
            display_find_authors_results(find_authors(first_input), first_input)
        elif args.title:
            display_find_titles_results(find_titles(first_input), first_input)
        else:
            print("Use either --author or --title with one argument. For --year, you must provide two arguments")
    elif len(args.Input) == 2:
        if args.year:
            second_input = args.Input[1]
            display_find_years_results(find_years(first_input, second_input), first_input, second_input)
        else:
            print("The only command that accepts two arguments is --year")
    else:
        print("Error, too many inputs --help for more information")


main()