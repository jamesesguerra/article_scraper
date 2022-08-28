import os

def run_psn():
    print('Bansa (1)')
    print('Metro (2)')
    print('Probinsya (3)')
    print('Opinyon (4)')
    print('Palaro (5)')
    category = int(input('Enter category number: '))
    print('')
    pages = input('Enter number of pages to fetch (5 articles per page): ')

    match category:
        case 1:
            os.system(f'scrapy crawl bansa -a pages={pages} -O ../csv_files/psn_bansa.csv')
        case 2:
            os.system(f'scrapy crawl metro -a pages={pages} -O ../csv_files/psn_metro.csv')
        case 3:
            os.system(f'scrapy crawl probinsya -a pages={pages} -O ../csv_files/psn_probinsya.csv')
        case 4:
            os.system(f'scrapy crawl opinyon -a pages={pages} -O ../csv_files/psn_opinyon.csv')
        case 5:
            os.system(f'scrapy crawl palaro -a pages={pages} -O ../csv_files/psn_palaro.csv')
