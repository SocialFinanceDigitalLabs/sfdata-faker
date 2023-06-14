from faker.providers import BaseProvider
from typing import Optional, Dict, Union
from .child import SEX_LITERAL, SEX_OPTIONS
from datetime import date


class Provider(BaseProvider):
    def child(
        self, sex: Optional[SEX_LITERAL] = None, age: Optional[int] = None
    ) -> Dict[str, Union[str, date, SEX_LITERAL]]:
        sex_ = self.random_element(SEX_OPTIONS) if sex is None else sex
        if sex_ == "F":
            first_name = self.generator.first_name_female()
        elif sex_ == "M":
            first_name = self.generator.first_name_male()
        else:
            first_name = self.generator.first_name()

        if age:
            date_of_birth = self.generator.date_of_birth(
                minimum_age=age, maximum_age=age
            )
        else:
            date_of_birth = self.generator.date_of_birth(minimum_age=0, maximum_age=17)

        return {
            "first_name": first_name,
            "last_name": self.generator.last_name(),
            "ethnicity": self.fake.ethnicity_code(),
            "sex": sex_,
            "upn": self.fake.upn(),
            "birthdate": date_of_birth,
        }

    def child_id(self, min: Optional[int] = 0, max: Optional[int] = 1000000) -> int:
        return self.random_int(min=min, max=max)
