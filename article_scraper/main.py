from run_fns import run_abs, run_psn, run_gma


def main():
    companies = ['Pilipino Star Ngayon', 'ABS-CBN', 'GMA (Balitambayan)']

    for i in range(len(companies)):
        print(f"{companies[i]} [{i}]")

    company = int(input('Enter company number: '))
    print('')

    match company:
        case 0:
            run_psn()
        case 1:
            run_abs()
        case 2:
            run_gma()

main()