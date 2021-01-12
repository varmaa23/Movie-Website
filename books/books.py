import csv
import re

import argparse

BooksDataSet = []

with open('books.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:

        # we want the index of the string where the '(' starts

        print(row, len(row))
        row[2] = re.sub("\((.*)\)", "", row[2])

        # index = row[2].find('(')
        # row[2] = row[2][0: index-1]
        print(row, len(row))
        # then we want to delete that index and the rest of the string
        BooksDataSet.append(row)

    print(BooksDataSet)


