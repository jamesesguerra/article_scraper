from run_fns import run_abs, run_psn, run_gma
from gooey import Gooey, GooeyParser

@Gooey(program_name="News Article Scraper")
def main():
    parser = GooeyParser()

    parser.add_argument('Company', choices=['Pilipino Star Ngayon', 'ABS-CBN', 'GMA (Balitambayan)'], help='News company name')
    parser.add_argument('Pages', default=1, type=int, help='Number of news article pages to fetch from the news company')

    category = parser.add_argument_group("Category (for Pilipino Star Ngayon only)")
    category.add_argument('-c', '--Category', choices=['Bansa', 'Metro', 'Probinsya', 'Opinyon', 'Palaro'], help='Pilipino Star Ngayon category')

    args = parser.parse_args()

    match args.Company:
        case 'ABS-CBN':
            run_abs()
        case 'GMA (Balitambayan)':
            run_gma(args.Pages)
        case 'Pilipino Star Ngayon':
            run_psn(args.Category, args.Pages)

main()