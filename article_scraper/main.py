import os


def run():
    pages = input('Enter number of pages to fetch: ')
    os.system(f"source ../scripts/psn.sh {pages}")

run()