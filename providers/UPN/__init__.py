from faker.providers import BaseProvider
from typing import Any, Optional
from .upn import UPN, VALID_STARTING_LETTERS, UNKNOWN_CODES


class Provider(BaseProvider):
    def upn(
        self,
        temporary: Optional[bool] = False,
        check_letter: Optional[str] = None,
        la_code: Optional[str] = None,
        establishment_number: Optional[str] = None,
        year_allocation: Optional[str] = None,
        serial_number: Optional[str] = None,
    ) -> str:
        """
        Generates a random UPN string with valid check letter.
        Specification Taken From
        https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/807381/UPN_Guide_1.2.pdf

        :param temporary:
            Is this a temporary UPN that should end in a letter?
        :param check_letter: A check letter for checking the code's validity at the start of the string
            If specified, the UPN may not be valid
        :param la_code:
            A three-digit string that uniquely idenfities an LA
        :param establishment_number:
            A four-digit string that uniquely identifies a school/establishment
        :param year_allocation:
            A two-digit string that identifies the year (e.g. 2023 would be '23')
        :param serial_number:
            A three-digit string that uniquely identifies the pupil
        :return:
            A valid random 13-digit UPN string
        """
        if not la_code:
            la_code = self.bothify(text="###")
        if not establishment_number:
            establishment_number = self.bothify(text="####")
        if not year_allocation:
            year_allocation = self.bothify(text="##")
        if not serial_number:
            if temporary:
                serial_number = self.bothify(text="##?", letters=VALID_STARTING_LETTERS)
            else:
                serial_number = self.bothify(text="###")

        return UPN(
            la_code, establishment_number, year_allocation, serial_number, check_letter
        ).format()

    def upn_simple(self, temporary: Optional[bool] = False) -> str:
        """
        Generates a UPN-like string without concerns about validity (e.g. the check letter)
        :param temporary: Is this a temporary UPN that should end in a letter?
        :return: A UPN String
        """
        if temporary:
            return self.bothify(text="?###########?", letters=VALID_STARTING_LETTERS)
        else:
            return self.bothify(text="?############", letters=VALID_STARTING_LETTERS)
