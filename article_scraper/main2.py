import os
from run_fns import run_abs, run_psn, run_gma
from gooey import Gooey, GooeyParser

@Gooey(program_name="Article Scraper")
def main():
    parser = GooeyParser()

    parser.add_argument('Company', choices=['Pilipino Star Ngayon', 'ABS-CBN', 'GMA (Balitambayan)'], help='Select company name')
    parser.add_argument('Pages', default=1, type=int, help='Number of news article pages to fetch from the news company')

    category = parser.add_argument_group("Category")
    category.add_argument('-c', '--category', choices=['Bansa', 'Metro', 'Probinsya', 'Opinyon', 'Palaro'], help='Select company name')

    args = parser.parse_args()

    match args.Company:
        case 'ABS-CBN':
            run_abs()
        case 'GMA (Balitambayan)':
            run_gma(args.Pages)




main()