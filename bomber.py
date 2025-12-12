import csv
import sys
from SinCity.colors import RED, RESET, BOLD
from modules.helper import helper

def get_phone():
    phone = None
    try:
        phone = input('Phone: ')
    except KeyboardInterrupt:
        sys.exit(f'{RED}\nExit...{RESET}')
    except Exception as err:
        print(f'{BOLD}ERROR: {err}{RESET}')
    return phone

def main():
    params = sys.argv
    if len(params) == 3 and '--phone' in params[1]:
        phone = params[2].strip()
    else:
        phone = get_phone()

if __name__ == '__main__':
    main()
