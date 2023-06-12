from faker.providers import BaseProvider
from faker.providers.address import BaseProvider as AddressProvider
from typing import Optional
from .placement import PLACE_CHANGE_CODES, PLACEMENT_TYPE_CODES, PLACEMENT_CODES
from faker import Faker


class Provider(BaseProvider):
    fake = Faker()
    fake.add_provider(AddressProvider)

    def place_change_reason_code(
        self, length: Optional[int] = 1, codes: Optional[list] = PLACE_CHANGE_CODES
    ) -> str:
        res = self.random_elements(
            elements=codes, length=length, unique=False, use_weighting=True
        )
        if length == 1:
            return res[0]
        else:
            return res

    def placement_type(self, age: Optional[int] = None):
        if age and age < 5:
            search_key = "probability_age_5"
        elif age and age < 16:
            search_key = "probability_age_16"
        else:
            search_key = "probability"

        types = [
            (key, value.get(search_key))
            for key, value in PLACEMENT_TYPE_CODES.items()
            if value.get(search_key, 0) > 0
        ]
        return self.random_elements(elements=types, length=1, use_weighting=True)[0][0]

    def placement(self) -> list:
        urn = self.placement_provider_urn()
        place_postcode = self.fake.postcode()
        home_postcode = self.fake.postcode()
        placement_type = self.placement_type()
        placement_code = self._placement_type_to_code(placement_type)
        return placement_type, placement_code, home_postcode, place_postcode, urn

    def placement_provider_urn(self) -> str:
        # This is the 7-digit social care URN specified by
        # https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1066288/
        # Children_looked_after_by_local_authorities_in_England_-_guide_to_the_SSDA903_collection_1_April_2021_to_31_March_2022.pdf
        return self.bothify(text="#######")

    def _placement_type_to_code(self, placement_type) -> str:
        if placement_type in ["A3", "A4", "A5", "A6"]:
            return self.random_elements(
                elements=PLACEMENT_CODES["even"], use_weighting=True, length=1
            )[0][0]
        elif placement_type in ["P1"]:
            return "PR0"
        elif placement_type in ["R2", "R3", "R5", "P3"]:
            return "PR3"
        elif placement_type in ["U1", "U2", "U3"]:
            return "PR1"
        elif placement_type in ["U4", "U5", "U6"]:
            return self.random_elements(
                elements=PLACEMENT_CODES["even"], use_weighting=True, length=1
            )[0][0]
        elif placement_type in ["R1", "K2", "S1", "P2", "H5"]:
            return self.random_elements(
                elements=PLACEMENT_CODES["weighted"], use_weighting=True, length=1
            )[0][0]
        else:
            return "PR4"
