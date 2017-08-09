from PersonClasses.BasePerson import BasePerson


class Employee(BasePerson):
    """
    Employee class. Extends BasePerson
    """
    def __init__(self, **kwargs: str) -> None:
        super().__init__(**kwargs)
        self._person_data['room'] = kwargs['room']
        self._person_data['position'] = kwargs['position']

    def __repr__(self) -> str:
        return f'''{self._person_data['name']} {self._person_data['middle_name']} {self._person_data['last_name']}:
\tFaculty: {self._person_data['faculty']}
\tPosition: {self._person_data['position']}
\tRoom: {self._person_data['room']}

\tPhone number: {self._person_data['phone_number']}
\tAddress: {self._person_data['address']}
\tDate of birth: {self._person_data['date_of_birth']}'''
