import os


def run_psn(category, pages):
    match category:
        case 'Bansa':
            os.system(f'scrapy crawl bansa -a pages={pages} -O ../csv_files/psn_bansa.csv')
        case 'Metro':
            os.system(f'scrapy crawl metro -a pages={pages} -O ../csv_files/psn_metro.csv')
        case 'Probinsya':
            os.system(f'scrapy crawl probinsya -a pages={pages} -O ../csv_files/psn_probinsya.csv')
        case 'Opinyon':
            os.system(f'scrapy crawl opinyon -a pages={pages} -O ../csv_files/psn_opinyon.csv')
        case 'Palaro':
            os.system(f'scrapy crawl palaro -a pages={pages} -O ../csv_files/psn_palaro.csv')


def run_abs():
    os.system('scrapy crawl abs-cbn -O ../csv_files/abs_cbn.csv')


def run_gma(pages):
    os.system(f'scrapy crawl gma -a pages={pages} -O ../csv_files/gma.csv')