from faker.providers import BaseProvider
from typing import Optional
from .ethnicities import ETHNICITY_CODES


class Provider(BaseProvider):
    def ethnicity_code(
        self, length: Optional[int] = 1, codes: Optional[list] = ETHNICITY_CODES
    ) -> str:
        res = self.random_elements(
            elements=codes, length=length, unique=False, use_weighting=True
        )
        if length == 1:
            return res[0]
        else:
            return res
