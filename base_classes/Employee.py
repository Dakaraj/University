from base_classes.BasePerson import BasePerson


class Employee(BasePerson):
    """
    Employee class. Extends BasePerson
    """
    def __init__(self, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self._person_data['room'] = kwargs['room']
        self._person_data['position'] = kwargs['position']

    def __repr__(self) -> str:
        return f'''Name: {self._person_data['name']} {self._person_data['middle_name']} {self._person_data['last_name']}:

Faculty: {self._person_data['faculty']}
Position: {self._person_data['position']}
Room: {self._person_data['room']}

Phone number: {self._person_data['phone_number']}
Address: {self._person_data['address']}
Date of birth: {self._person_data['date_of_birth']}'''
