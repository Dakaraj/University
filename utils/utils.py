import time
import os
import sys
import csv
from typing import List, Dict
from datetime import datetime
from PersonClasses.BasePerson import BasePerson
from PersonClasses.Employee import Employee
from PersonClasses.Student import Student

sys_os = sys.platform
FILE_PATH = 'data/persons.csv'
FIELD_NAMES = ('name', 'last_name', 'middle_name', 'date_of_birth', 'faculty',
               'address', 'phone_number', 'room', 'position', 'course', 'qualification')


def sleep(s: int) -> None:
    time.sleep(s)


def clear() -> None:
    if sys_os == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def read_csv() -> List[BasePerson]:
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


def write_csv(data: List[Dict[str, str]]) -> None:
    with open(FILE_PATH, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(data)


def convert_classes_to_dicts(persons_list: List[BasePerson]) -> List[Dict[str, str]]:
    person_dicts_list = [person.get_as_dict() for person in persons_list]

    return person_dicts_list
