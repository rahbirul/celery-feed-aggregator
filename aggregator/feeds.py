import os

from csvreader import get_csv_rows
from tasks import download, parse

abspath = lambda filename: os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)

CSV_FILEPATH = os.path.join('..', 'feeds.csv')


def run():
    for row in get_csv_rows(abspath(CSV_FILEPATH)):
        #Download the feed asynchronously, set the parse() task as callback
        download.apply_async(args=[row['URL']], link=parse.s())

if __name__ == '__main__':
    run()
