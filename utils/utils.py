import time
import os
import sys
import csv
from typing import List, Dict

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


def read_csv():
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, 'w').close()

    with open(FILE_PATH) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELD_NAMES)
        for row in reader:
            print(row)


def write_csv(data: List[Dict[str, str]]):
    with open(FILE_PATH, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(data)

