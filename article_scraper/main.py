from psn import run_psn


def main():
    company = input('Enter company name (psn): ').lower()
    print('')

    match company:
        case 'psn':
            run_psn()

main()