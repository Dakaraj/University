import time
import os
import sys
import csv
import re
from typing import List, Dict, Optional, Tuple
from PersonClasses.BasePerson import BasePerson
from PersonClasses.Employee import Employee
from PersonClasses.Student import Student

CLEAR_COMMAND = 'cls' if sys.platform == 'win32' else 'clear'
FILE_PATH = 'data/persons.csv'
FIELD_NAMES = ('name', 'last_name', 'middle_name', 'date_of_birth', 'faculty',
               'address', 'phone_number', 'room', 'position', 'course', 'qualification')
QUALIFICATIONS = {'student': 'I - IV', 'bachelor': 'V - VI', 'specialist': '-', 'master': '-', 'postgraduate': '-'}


def sleep(s: int) -> None:
    time.sleep(s)


def clear() -> None:
    os.system(CLEAR_COMMAND)


def load_from_csv() -> List[BasePerson]:
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, 'w').close()

    with open(FILE_PATH, newline='') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=FIELD_NAMES)
        next(reader)

        persons_list = []
        for row in reader:
            if row['room']:
                persons_list.append(Employee(**row))
            else:
                persons_list.append(Student(**row))

        return persons_list


def save_data_and_exit(persons_list: List[BasePerson]) -> None:
    clear()
    print('Saving changes...')
    person_dicts_list = convert_classes_to_dicts(persons_list)
    write_csv(person_dicts_list)
    print('Save complete successfully')
    sleep(3)
    clear()
    print('Thank you for using this program')
    quit()


def write_csv(data: List[Dict[str, str]]) -> None:
    with open(FILE_PATH, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(data)


def convert_classes_to_dicts(persons_list: List[BasePerson]) -> List[Dict[str, str]]:
    person_dicts_list = [person.get_as_dict() for person in persons_list]

    return person_dicts_list


def get_user_input(class_type: str, variable: str, min_s: int = 1, max_s: int = 20) -> str:
    while True:
        clear()
        print('############ ADD NEW {} ############\n'.format(class_type.upper()))
        print(f'Input {class_type}\'s {variable}. Should be {min_s}-{max_s} symbols long')
        data_input = input('>')
        if min_s <= len(data_input) <= max_s:
            return data_input


def get_pattern_input(class_type: str, variable: str, pattern: str, pattern_repr: str) -> str:
    while True:
        clear()
        print('############ ADD NEW {} ############\n'.format(class_type.upper()))
        print(f'Input {variable} in the following format: "{pattern_repr}"\n')
        patterned_input = input('>')
        if re.match(pattern, patterned_input):
            return patterned_input


def select_qualification() -> str:
    matcher = {'1': 'student', '2': 'bachelor', '3': 'specialist', '4': 'master', '5': 'postgraduate'}

    while True:
        clear()
        print('############ ADD NEW STUDENT ############\n\n'
              'Chose a qualification from list below:\n'
              f'1. Student (courses: {QUALIFICATIONS["student"]})\n'
              f'2. Bachelor (courses: {QUALIFICATIONS["bachelor"]})\n'
              '3. Specialist\n'
              '4. Master\n'
              '5. Postgraduate\n')
        qualification_input = input('>')

        if qualification_input in matcher:
            return matcher[qualification_input]


def select_course(qualification: str) -> str:
    courses = QUALIFICATIONS[qualification]
    if courses == '-':
        return courses

    if courses == 'I - IV':
        matcher = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV'}
        while True:
            clear()
            print('############ ADD NEW STUDENT ############\n\n'
                  'Chose a course from list below:\n'
                  '1. I\n'
                  '2. II\n'
                  '3. III\n'
                  '4. IV\n')
            course_input = input('>')
            if course_input in matcher:
                return matcher[course_input]

    elif courses == 'V - VI':
        matcher = {'1': 'V', '2': 'VI'}
        while True:
            clear()
            print('############ ADD NEW STUDENT ############\n\n'
                  'Chose a course from list below:\n'
                  '1. IV\n'
                  '2. V\n')
            course_input = input('>')
            if course_input in matcher:
                return matcher[course_input]


def gather_general_inputs(class_type: str) -> Tuple[str, str, str, str, str, str, str]:
    name = get_user_input(class_type, 'name')
    last_name = get_user_input(class_type, 'last name')
    middle_name = get_user_input(class_type, 'middle name')
    date_of_birth = get_pattern_input(class_type, 'date of birth',
                                      r'(0[1-9]|[1-2][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}', 'dd-mm-YYYY')
    faculty = get_user_input(class_type, 'faculty', 2, 50)
    address = get_user_input(class_type, 'address', 10, 50)
    phone_pattern = r'\+?(\d{1,3})[-\s]?\(?(\d\d)\)?[-\s]?(\d\d\d)[-\s]?(\d\d)[-\s]?(\d\d)'
    phone_number = get_pattern_input(class_type, 'phone number', phone_pattern, '+380994596578 / 380 (66) 257-12-31')
    parts_list = re.findall(phone_pattern, phone_number)[0]
    phone_number = '+' + ''.join(parts_list)

    return name, last_name, middle_name, date_of_birth, faculty, address, phone_number


def add_new_employee() -> Optional[Employee]:
    name, last_name, middle_name, date_of_birth, faculty, address, phone_number = gather_general_inputs('employee')
    room = get_pattern_input('employee', 'room', r'\d{3}', '123')
    position = get_user_input('employee', 'position', 3, 30)

    new_employee = Employee(name=name, last_name=last_name, middle_name=middle_name,
                            date_of_birth=date_of_birth, faculty=faculty, address=address,
                            phone_number=phone_number, room=room, position=position)

    return new_employee


def add_new_student() -> Optional[Student]:
    name, last_name, middle_name, date_of_birth, faculty, address, phone_number = gather_general_inputs('student')
    qualification = select_qualification()
    course = select_course(qualification)

    new_student = Student(name=name, last_name=last_name, middle_name=middle_name,
                          date_of_birth=date_of_birth, faculty=faculty, address=address,
                          phone_number=phone_number, qualification=qualification, course=course)

    return new_student
