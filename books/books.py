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
        if(author.find(" and ") == -1):
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
        except:
            print("Please input an integer")
        return int_year
    return


def find_authors(author_input):
    authors_array = []
    for book in BooksDataSet:
        author = book[2]
        title = book[0]
        if (type(author) is str and author.lower().find(author_input.lower()) != -1):

            authors_array.append([author, title])
        elif (type(author) is list):
            for authorIndex in range(len(author)):
                if (author[authorIndex].lower().find(author_input.lower()) != -1):
                    authors_array.append([author, title])
    return authors_array

def find_titles(title_input):
    print(title_input, type(title_input))
    title_array = []
    for book in BooksDataSet:
        title = book[0]
        if (type(title) is str and title.lower().find(title_input.lower()) != -1):
            title_array.append(title)
    return title_array   

def find_years(year1, year2):
    year1 = convertStringToInt(year1)
    year2 = convertStringToInt(year2)
    # for book in BooksDataSet:
    #     title = book[0]
    #     if (type(title) is str and title.lower().find(title_input.lower()) != -1):
    #         title_array.append(title)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--author", action="store_true")
    group.add_argument("-t", "--title", action="store_true")
    group.add_argument("-y", "--year", action="store_true")
    parser.add_argument("Input", nargs="*", type = str, help="The search string") 
    # parser.add_argument("Input", type=int, help="The search string", required=False) 
    args = parser.parse_args()
    
    first_input = args.Input[0]
        

    if len(args.Input) == 1:
        if args.author:
            print(find_authors(str(args.Input)))
        elif args.title:
            print(find_titles(first_input))
        else:
            print("Use either --author or --title")
    elif len(args.Input) == 2:
        if args.year:
            second_input = args.Input[1]
            print(f'Year, the input is {first_input, second_input}.')
            find_years(first_input, second_input)
        else:
            print("For two arguments, you must use --year")
    else:
        print("Error")

main()


