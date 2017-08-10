from typing import Dict


class BasePerson:
    """
    Base class for any person
    """
    def __init__(self, **kwargs: str) -> None:
        self._person_data: Dict[str, str] = {
            'name': kwargs['name'],
            'last_name': kwargs['last_name'],
            'middle_name': kwargs['middle_name'],
            'date_of_birth': kwargs['date_of_birth'],
            'faculty': kwargs['faculty'],
            'address': kwargs['address'],
            'phone_number': kwargs['phone_number']
        }

    def __str__(self):
        return self.__repr__()

    def search_person(self, input_data: str) -> bool:
        for value in self._person_data.values():
            if isinstance(value, str):
                if input_data.lower() in value.lower():
                    return True

        return False

    def update_person_data(self, key: str, value: str) -> None:
        self._person_data[key] = value

    def get_as_dict(self) -> Dict[str, str]:
        return self._person_data

    def get_specific_value(self, key: str) -> str:
        return self._person_data[key]
