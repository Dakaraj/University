from PersonClasses.BasePerson import BasePerson
from typing import Dict


class Student(BasePerson):
    """
    Student class. Extends BasePerson
    """
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        super().__init__(**kwargs)
        self._person_data['course'] = kwargs['course']
        self._person_data['qualification'] = kwargs['qualification']

    def __repr__(self) -> str:
        return f'''{self._person_data['name']} {self._person_data['middle_name']} {self._person_data['last_name']}:
\tFaculty: {self._person_data['faculty']}
\tQualification: {self._person_data['qualification']}
\tCourse: {self._person_data['course']}

\tPhone number: +{self._person_data['phone_number']}
\tAddress: {self._person_data['address']}
\tDate of birth: {self._person_data['date_of_birth']}'''
