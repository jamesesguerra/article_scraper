import os


def run_psn():
    categories = ['Bansa', 'Metro', 'Probinsya', 'Opinyon', 'Palaro']

    for i in range(len(categories)):
        print(f"{categories[i]} [{i}]")
    
    print('')
    category = int(input('Enter category number: '))
    print('')
    pages = input('Enter number of pages to fetch (5 articles per page): ')

    match category:
        case 0:
            os.system(f'scrapy crawl bansa -a pages={pages} -O ../csv_files/psn_bansa.csv')
        case 1:
            os.system(f'scrapy crawl metro -a pages={pages} -O ../csv_files/psn_metro.csv')
        case 2:
            os.system(f'scrapy crawl probinsya -a pages={pages} -O ../csv_files/psn_probinsya.csv')
        case 3:
            os.system(f'scrapy crawl opinyon -a pages={pages} -O ../csv_files/psn_opinyon.csv')
        case 4:
            os.system(f'scrapy crawl palaro -a pages={pages} -O ../csv_files/psn_palaro.csv')


def run_abs():
    os.system('scrapy crawl abs-cbn -O ../csv_files/abs_cbn.csv')


def run_gma():
    print('* Current limit of pages to fetch: 102')
    pages = input('Enter number of pages to fetch (50 articles per page): ')
    os.system(f'scrapy crawl gma -a pages={pages} -O ../csv_files/gma.csv')