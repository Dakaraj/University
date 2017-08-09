from PersonClasses.BasePerson import BasePerson


class Student(BasePerson):
    """
    Student class. Extends BasePerson
    """
    def __init__(self, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self._person_data['course'] = kwargs['course']
        self._person_data['qualification'] = kwargs['qualification']

    def __repr__(self) -> str:
        return f'''Name: {self._person_data['name']} {self._person_data['middle_name']} {self._person_data['last_name']}:

Faculty: {self._person_data['faculty']}
Qualification: {self._person_data['qualification']}
Course: {self._person_data['course']}

Phone number: {self._person_data['phone_number']}
Address: {self._person_data['address']}
Date of birth: {self._person_data['date_of_birth']}'''
