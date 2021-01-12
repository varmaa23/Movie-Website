import csv
import re
import argparse

BooksDataSet = []

with open('books.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:

        # we want the index of the string where the '(' starts
        # find a better solution?
        regex = "\s\((.*)\)"
        if(row[2].find(" and ") == -1):
            row[2] = re.sub(regex, "", row[2])
        else:
            row[2] = row[2].split(" and ")
            for i in range(0, len(row[2])):
                row[2][i] = re.sub(regex, "", row[2][i])

        BooksDataSet.append(row)

def find_authors(author_input):
    # quality check--> make sure that data is surrounded by quotes
    # take whatever's inside the quotes
    # write a loop that searches for matches inside the booksdataset, find() for every book title
    # return a list of authors + their book titles that match the string


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--author", action="store_true")
    group.add_argument("-t", "--title", action="store_true")
    group.add_argument("-y", "--year", action="store_true")
    parser.add_argument("Input", type=str, help="The search string")
    args = parser.parse_args()

    if args.author:
        print(f'Author, the input is {args.Input}.')
        # get the returned value and print it here
    elif args.title:
        print(f'Title, the input is {args.Input}.')
    elif args.year:
        print(f'Year, the input is {args.Input}.')
    else:
        print("What is this")

main()


