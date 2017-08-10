from utils.utils import *


class App:
    def __init__(self) -> None:
        self.persons_list: List[BasePerson] = None

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

            user_input: str = input('>')

            if user_input == '0':
                while True:
                    clear()
                    print('############ EXIT PROGRAM ############\n\n'
                          '1. Save changes and exit\n'
                          '2. Exit without saving\n'
                          '0. Cancel\n')
                    exit_input: str = input('>')

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
                    add_new_input: str = input('>')

                    if add_new_input == '0':
                        break
                    elif add_new_input == '1':
                        new_employee: Employee = add_new_employee()
                        self.persons_list.append(new_employee)
                        break
                    elif add_new_input == '2':
                        new_student: Student = add_new_student()
                        self.persons_list.append(new_student)
                        break
                    else:
                        continue

            elif user_input == '2':
                while True:
                    clear()
                    print('############ SEARCH ALL ENTRIES ############\n\n'
                          'Input a search query (min 3 symbols):\n')
                    search_all_query: str = input('>')
                    if len(search_all_query) < 3:
                        continue

                    list_of_finds: List[BasePerson] = [person for person in self.persons_list
                                                       if person.search_person(search_all_query)]

                    if not list_of_finds:
                        clear()
                        print('############ SEARCH ALL ENTRIES ############\n\n'
                              'No results found')
                        sleep(3)
                        break

                    search_results_manager(list_of_finds, self.persons_list)
                    break

            elif user_input == '3':
                while True:
                    clear()
                    print('############ SEARCH STUDENTS ONLY ############\n\n'
                          'Input a search query (min 3 symbols):\n')
                    search_students_query: str = input('>')
                    if len(search_students_query) < 3:
                        continue

                    list_of_finds: List[Student] = [person for person in self.persons_list
                                                    if isinstance(person, Student)
                                                    and person.search_person(search_students_query)]

                    if not list_of_finds:
                        clear()
                        print('############ SEARCH STUDENTS ONLY ############\n\n'
                              'No results found')
                        sleep(3)
                        break

                    search_results_manager(list_of_finds, self.persons_list)
                    break

            elif user_input == '4':
                while True:
                    clear()
                    print('############ SEARCH EMPLOYEES ONLY ############\n\n'
                          'Input a search query (min 3 symbols):\n')
                    search_employees_query: str = input('>')
                    if len(search_employees_query) < 3:
                        continue

                    list_of_finds: List[Employee] = [person for person in self.persons_list
                                                     if isinstance(person, Employee)
                                                     and person.search_person(search_employees_query)]

                    if not list_of_finds:
                        clear()
                        print('############ SEARCH EMPLOYEES ONLY ############\n\n'
                              'No results found')
                        sleep(3)
                        break

                    search_results_manager(list_of_finds, self.persons_list)
                    break

            elif user_input == '5':
                while True:
                    clear()
                    print('############ REFERENCE INFORMATION ############\n\n'
                          '1. Display unique positions\n'
                          '2. Display unique faculties\n'
                          '0. Cancel')
                    reference_input: str = input('>')

                    if reference_input == '0':
                        break

                    if reference_input == '1':
                        positions_set: set = set()
                        for person in self.persons_list:
                            if isinstance(person, Employee):
                                positions_set.add(person.get_specific_value('position'))

                        clear()
                        print('############ UNIQUE POSITIONS ############\n')
                        if positions_set:
                            for index, item in enumerate(positions_set, start=1):
                                print(f'{index}. {item}')
                        else:
                            print('Nothing to display')
                        print('\nPress Enter to continue...')
                        input('>')

                    if reference_input == '2':
                        faculties_set: set = set()
                        for person in self.persons_list:
                            faculties_set.add(person.get_specific_value('faculty'))

                        clear()
                        print('############ UNIQUE FACULTIES ############\n')
                        if faculties_set:
                            for index, item in enumerate(faculties_set, start=1):
                                print(f'{index}. {item}')
                        else:
                            print('Nothing to display')
                        print('\nPress Enter to continue...')
                        input('>')

            else:
                continue
