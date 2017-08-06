from typing import Any, Dict


class BasePerson:
    """
    Base class for any person
    """
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        self._person_data: Dict[str, str] = {
            'name': kwargs['name'],
            'last_name': kwargs['last_name'],
            'middle_name': kwargs['middle_name'],
            'date_of_birth': kwargs['date_of_birth'],
            'faculty': kwargs['faculty'],
            'address': kwargs['address'],
            'phone_number': kwargs['phone_number']
        }

    def search_person(self, input_data: str) -> Any:
        for value in self._person_data.values():
            print(value)
            if isinstance(value, str):
                if input_data.lower() in value.lower():
                    return self

    def update_person_data(self, key: str, value: str) -> None:
        self._person_data[key] = value

    def get_as_dict(self) -> Dict[str, str]:

        return self._person_data
