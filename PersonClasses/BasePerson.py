from datetime import date
from typing import Any


class BasePerson:
    """
    Base class for any person
    """
    _person_data = {}

    def __init__(self, name: str, last_name: str, middle_name: str, date_of_birth: date,
                 faculty: str, address: str, phone_number: str) -> None:
        self._person_data['name'] = name
        self._person_data['last_name'] = last_name
        self._person_data['middle_name'] = middle_name
        self._person_data['date_of_birth'] = date_of_birth
        self._person_data['faculty'] = faculty
        self._person_data['address'] = address
        self._person_data['phone_number'] = phone_number

    def _search_base(self, input_data: str) -> Any:
        for value in self._person_data.values():
            if input_data.lower() in value.lower():
                return self

    def update_person_data(self, key: str, value: str) -> None:
        self._person_data[key] = value
