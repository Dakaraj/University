from PersonClasses.BasePerson import BasePerson
from datetime import date


class Employee(BasePerson):
    """
    Employee class. Extends BasePerson
    """
    def __init__(self, name: str, last_name: str, middle_name: str, date_of_birth: date,
                 faculty: str, address: str, phone_number: str, room: str, position: str) -> None:
        super().__init__(name, last_name, middle_name, date_of_birth, faculty, address, phone_number)
        self._person_data['room'] = room
        self._person_data['position'] = position

    def __repr__(self) -> str:
        return f'''{self._person_data['name']} {self._person_data['middle_name']} {self._person_data['last_name']}:
\tFaculty: {self._person_data['faculty']}
\tPosition: {self._person_data['position']}
\tRoom: {self._person_data['room']}

\tPhone number: {self._person_data['phone_number']}
\tAddress: {self._person_data['address']}
\tDate of birth: {self._person_data['date_of_birth']:%d-%m-%Y}'''
