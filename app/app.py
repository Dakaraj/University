from utils.utils import *


def main() -> None:
    clear()
    print('Welcome to university management application')
    sleep(2)
    print('Loading data from CSV...')
    persons_list = read_csv()
    print('Loading complete\n')
    sleep(2)

    while True:
        clear()
        print('############ PROGRAM MENU ############\n\n'
              '1. Add new entry\n'
              '2. Search all entries\n'
              '3. Search students only\n'
              '4. Search employees only\n'
              '5. Reference information\n'
              '0. Save all changes and exit\n')
        user_input = input('>')
        if user_input == '0':
            clear()
            print('Saving changes...')
            convert_classes_to_dicts(persons_list)
            print('Save complete successfully')

        break
