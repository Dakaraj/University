from utils.utils import *


class App:
    def __init__(self) -> None:
        self.persons_list = []

    def main_loop(self) -> None:
        clear()
        print('Welcome to university management application')
        sleep(2)
        print('Loading data from CSV...')
        self.persons_list = load_from_csv()
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
                        save_data_and_exit(self.persons_list)
                    elif exit_input == '2':
                        clear()
                        print('Thank you for using this program')
                        quit()
                    else:
                        continue

            elif user_input == '1':

                while True:
                    clear()
                    print('############ ADD NEW ENTRY ############\n\n'
                          '1. Add new employee\n'
                          '2. Add new student\n'
                          '0. Cancel\n')
                    add_new_input = input('>')

                    if add_new_input == '0':
                        break
                    elif add_new_input == '1':
                        new_employee = add_new_employee()
                        self.persons_list.append(new_employee)
                        break
                    elif add_new_input == '2':
                        new_student = add_new_student()
                        self.persons_list.append(new_student)
                        break
                    else:
                        continue

            elif user_input == '2':

                while True:
                    clear()
                    print('############ SEARCH ALL ENTRIES ############\n\n'
                          'Input a search query (min 3 symbols):\n')
                    search_all_query = input('>')
                    if len(search_all_query) < 3:
                        continue

                    list_of_finds = []
                    for person in self.persons_list:
                        result = person.search_person(search_all_query)
                        if result:
                            list_of_finds.append(result)

                    if not list_of_finds:
                        clear()
                        print('############ SEARCH ALL ENTRIES ############\n\n'
                              'No results found')
                        sleep(3)
                        break

                    search_results_manager(list_of_finds, self.persons_list)
                    break

            elif user_input == '3':
                pass

            elif user_input == '4':
                pass

            elif user_input == '5':
                pass

            else:
                continue
