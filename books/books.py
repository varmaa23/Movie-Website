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


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--author", action="store_true")
    group.add_argument("-t", "--title", action="store_true")
    group.add_argument("-y", "--year", action="store_true")
    parser.add_argument("Input", nargs="", type = str, help="The search string") 
    # parser.add_argument("Input", type=int, help="The search string", required=False) 
    args = parser.parse_args()

    if args.author:
        print(f'Author, the input is {args.Input}.')
        print(find_authors(str(args.Input)))
    elif args.title:
        print(f'Title, the input is {args.Input}.')
        print(find_titles(args.Input[0]))
    elif args.year:
        print(f'Year, the input is {args.Input[0]}.')
    else:
        print("What is this")

main()


