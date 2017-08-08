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
              '0. Exit program\n')

        user_input = input('>')

        if user_input == '0':
            while True:
                clear()
                print('############ EXIT PROGRAM ############\n\n'
                      '1. Save changes and exit\n'
                      '2. Exit without saving\n'
                      '0. Cancel\n')
                exit_input = input('>')

                if exit_input == '0':
                    break
                elif exit_input == '1':
                    clear()
                    print('Saving changes...')
                    person_list_dicts = convert_classes_to_dicts(persons_list)
                    write_csv(person_list_dicts)
                    print('Save complete successfully')
                    sleep(3)
                    clear()
                    print('Thank you for using this program')
                    quit()
                elif exit_input == '2':
                    clear()
                    print('Thank you for using this program')
                    quit()
                else:
                    continue
        break
