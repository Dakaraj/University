import time
import os
import sys
from csv import DictReader, DictWriter
import re
from typing import List, Dict, Optional, Tuple, Pattern
from base_classes.BasePerson import BasePerson
from base_classes.Employee import Employee
from base_classes.Student import Student

CLEAR_COMMAND: str = 'cls' if sys.platform == 'win32' else 'clear'
DATA_PATH: str = 'data'
FILE_NAME: str = 'persons.csv'
FIELD_NAMES: List[str] = ['name', 'last_name', 'middle_name', 'date_of_birth', 'faculty',
                          'address', 'phone_number', 'room', 'position', 'course', 'qualification']
QUALIFICATIONS: Dict[str, str] = {'student': 'I - IV', 'bachelor': 'V - VI', 'specialist': '-', 'master': '-', 'postgraduate': '-'}
DATE_OF_BIRTH_PATTERN: Pattern = re.compile(r'(0[1-9]|[1-2][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}')
PHONE_NUMBER_PATTERN: Pattern = re.compile(r'\+?(\d{1,3})[-\s]?\(?(\d\d)\)?[-\s]?(\d\d\d)[-\s]?(\d\d)[-\s]?(\d\d)')
ROOM_PATTERN: Pattern = re.compile(r'\d{3}')


def sleep(s: int) -> None:
    time.sleep(s)


def clear() -> None:
    os.system(CLEAR_COMMAND)


def load_from_csv() -> List[BasePerson]:
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    if not os.path.exists(DATA_PATH + os.sep + FILE_NAME):
        with open(DATA_PATH + os.sep + FILE_NAME, 'w') as csv_file:
            writer: DictWriter = DictWriter(csv_file, fieldnames=FIELD_NAMES)
            writer.writeheader()

    with open(DATA_PATH + os.sep + FILE_NAME, newline='') as csv_file:
        reader: DictReader = DictReader(csv_file, fieldnames=FIELD_NAMES)
        next(reader)  # type: ignore

        persons_list: List[BasePerson] = []
        for row in reader:
            if row['room']:
                persons_list.append(Employee(**row))
            else:
                persons_list.append(Student(**row))

        return persons_list


def save_data_and_exit(persons_list: List[BasePerson]) -> None:
    clear()
    print('Saving changes...')
    person_dicts_list: List[Dict[str, str]] = convert_classes_to_dicts(persons_list)
    write_csv(person_dicts_list)
    print('Save complete successfully')
    sleep(3)
    clear()
    print('Thank you for using this program')
    quit()


def write_csv(data: List[Dict[str, str]]) -> None:
    with open(DATA_PATH + os.sep + FILE_NAME, 'w', newline='') as csv_file:
        writer: DictWriter = DictWriter(csv_file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(data)


def convert_classes_to_dicts(persons_list: List[BasePerson]) -> List[Dict[str, str]]:
    person_dicts_list: List[Dict[str, str]] = [person.get_as_dict() for person in persons_list]

    return person_dicts_list


def get_user_input(class_type: str, variable: str, min_s: int = 1, max_s: int = 20) -> str:
    while True:
        clear()
        print('############ {}\'S {} ############\n'.format(class_type.upper(), variable.upper()))
        print(f'Input {class_type}\'s {variable}. Should be {min_s}-{max_s} symbols long')
        data_input: str = input('>')

        if min_s <= len(data_input) <= max_s:
            return data_input


def get_pattern_input(class_type: str, variable: str, pattern: Pattern, pattern_repr: str) -> str:
    while True:
        clear()
        print('############ {}\'S {} ############\n'.format(class_type.upper(), variable.upper()))
        print(f'Input {variable} in the following format: "{pattern_repr}"\n')
        patterned_input = input('>')

        if re.match(pattern, patterned_input):
            return patterned_input


def select_qualification() -> str:
    matcher: Dict[str, str] = {'1': 'Student', '2': 'Bachelor', '3': 'Specialist', '4': 'Master', '5': 'Postgraduate'}

    while True:
        clear()
        print('############ STUDENT\'S QUALIFICATION ############\n\n'
              'Chose a qualification from list below:\n'
              f'1. Student (courses: {QUALIFICATIONS["student"]})\n'
              f'2. Bachelor (courses: {QUALIFICATIONS["bachelor"]})\n'
              '3. Specialist\n'
              '4. Master\n'
              '5. Postgraduate\n')
        qualification_input: str = input('>')

        if qualification_input in matcher:
            return matcher[qualification_input]


def select_course(qualification: str) -> str:
    courses: str = QUALIFICATIONS[qualification]
    matcher: Dict[str, Dict[str, str]] = {
        'I - IV': {'1': 'I', '2': 'II', '3': 'III', '4': 'IV'},
        'V - VI': {'1': 'V', '2': 'VI'}
    }

    if courses == 'I - IV':
        while True:
            clear()
            print('############ STUDENT\'S COURSE ############\n\n'
                  'Chose a course from list below:\n'
                  '1. I\n'
                  '2. II\n'
                  '3. III\n'
                  '4. IV\n')
            course_1_4_input: str = input('>')

            if course_1_4_input in matcher:
                return matcher[courses][course_1_4_input]

    elif courses == 'V - VI':
        while True:
            clear()
            print('############ STUDENT\'S COURSE ############\n\n'
                  'Chose a course from list below:\n'
                  '1. V\n'
                  '2. VI\n')
            course_5_6_input: str = input('>')

            if course_5_6_input in matcher:
                return matcher[courses][course_5_6_input]

    else:
        return courses


def gather_general_inputs(class_type: str) -> Tuple[str, str, str, str, str, str, str]:
    name: str = get_user_input(class_type, 'name')
    last_name: str = get_user_input(class_type, 'last name')
    middle_name: str = get_user_input(class_type, 'middle name')
    date_of_birth: str = get_pattern_input(class_type, 'date of birth',
                                           DATE_OF_BIRTH_PATTERN, 'dd-mm-YYYY')
    faculty: str = get_user_input(class_type, 'faculty', 2, 50)
    address: str = get_user_input(class_type, 'address', 10, 50)
    phone_number: str = get_pattern_input(class_type, 'phone number', PHONE_NUMBER_PATTERN, '+380994596578 / 1 (33) 257-12-31')
    parts_list: str = PHONE_NUMBER_PATTERN.findall(phone_number)[0]
    phone_number = '+' + ''.join(parts_list)

    return name, last_name, middle_name, date_of_birth, faculty, address, phone_number


def add_new_employee() -> Optional[Employee]:
    name, last_name, middle_name, date_of_birth, faculty, address, phone_number = gather_general_inputs('employee')
    room: str = get_pattern_input('employee', 'room', ROOM_PATTERN, '123')
    position: str = get_user_input('employee', 'position', 2, 30)

    new_employee: Employee = Employee(name=name, last_name=last_name, middle_name=middle_name,
                                      date_of_birth=date_of_birth, faculty=faculty, address=address,
                                      phone_number=phone_number, room=room, position=position)

    return new_employee


def add_new_student() -> Optional[Student]:
    name, last_name, middle_name, date_of_birth, faculty, address, phone_number = gather_general_inputs('student')
    qualification: str = select_qualification()
    course: str = select_course(qualification)

    new_student: Student = Student(name=name, last_name=last_name, middle_name=middle_name,
                                   date_of_birth=date_of_birth, faculty=faculty, address=address,
                                   phone_number=phone_number, qualification=qualification, course=course)

    return new_student


def edit_person(person: BasePerson) -> None:
    while True:
        clear()
        print('############ EDIT ITEM ############\n')
        print(person)
        print('\nField to edit:\n'
              '1. Name\n'
              '2. Last name\n'
              '3. Middle name\n'
              '4. Date of birth\n'
              '5. Faculty\n'
              '6. Address\n'
              '7. Phone number')
        class_type: str = ''
        if isinstance(person, Employee):
            class_type = 'employee'
            print('8. Room\n9. Position')
        elif isinstance(person, Student):
            print('8. Qualification and Course')
            class_type = 'student'
        print('0. Cancel\n')
        edit_input: str = input('>')

        if edit_input == '0':
            break

        elif edit_input == '1':
            new_name: str = get_user_input(class_type, 'name')
            person.update_person_data('name', new_name)

        elif edit_input == '2':
            new_last_name: str = get_user_input(class_type, 'last name')
            person.update_person_data('last_name', new_last_name)

        elif edit_input == '3':
            new_middle_name: str = get_user_input(class_type, 'middle name')
            person.update_person_data('middle_name', new_middle_name)

        elif edit_input == '4':
            new_date_of_birth: str = get_pattern_input(class_type, 'date of birth', DATE_OF_BIRTH_PATTERN, 'dd-mm-YYYY')
            person.update_person_data('date_of_birth', new_date_of_birth)

        elif edit_input == '5':
            new_faculty: str = get_user_input(class_type, 'faculty', 2, 50)
            person.update_person_data('faculty', new_faculty)

        elif edit_input == '6':
            new_address: str = get_user_input(class_type, 'address', 10, 50)
            person.update_person_data('address', new_address)

        elif edit_input == '7':
            raw_phone_number: str = get_pattern_input(class_type, 'phone number', PHONE_NUMBER_PATTERN, '+380994596578 / 1 (33) 257-12-31')
            parts_list: List[str] = PHONE_NUMBER_PATTERN.findall(raw_phone_number)[0]
            new_phone_number: str = '+' + ''.join(parts_list)
            person.update_person_data('phone_number', new_phone_number)

        elif edit_input == '8' and isinstance(person, Student):
            new_qualification: str = select_qualification()
            new_course: str = select_course(new_qualification)
            person.update_person_data('qualification', new_qualification)
            person.update_person_data('course', new_course)

        elif edit_input == '8' and isinstance(person, Employee):
            new_room: str = get_pattern_input('employee', 'room', ROOM_PATTERN, '123')
            person.update_person_data('room', new_room)

        elif edit_input == '9' and isinstance(person, Employee):
            new_position = get_user_input(class_type, 'position', 2, 30)
            person.update_person_data('position', new_position)

        else:
            continue


def search_results_manager(search_results: List[BasePerson], all_persons_list: List[BasePerson]) -> None:
    index: int = 0
    while search_results:
        clear()
        print('############ SEARCH RESULTS ############\n\n'
              f'{len(search_results)} items found\n'
              f'Item {index + 1}/{len(search_results)}:\n')
        print(search_results[index])
        print('\nActions:')
        print('1. Previous item\n' if index != 0 else '', end='')
        print('2. Next item\n' if index != len(search_results) - 1 else '', end='')
        print('3. Edit item\n'
              '4. Delete item\n'
              '0. Cancel\n')
        results_input: str = input('>')

        if results_input == '0':
            break

        elif results_input == '1' and index != 0:
            index -= 1
            continue

        elif results_input == '2' and index != len(search_results) - 1:
            index += 1
            continue

        elif results_input == '3':
            person_to_edit: BasePerson = search_results[index]
            edit_person(person_to_edit)

        elif results_input == '4':
            current_object: BasePerson = search_results[index]
            del search_results[index]
            all_persons_list.remove(current_object)
            index -= 1

        else:
            continue
