from run_fns import run_abs, run_psn, run_gma, run_kami


def main():
    companies = ['Pilipino Star Ngayon', 'ABS-CBN', 'GMA (Balitambayan)', 'Kami']

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
        case 3:
            run_kami()

main()