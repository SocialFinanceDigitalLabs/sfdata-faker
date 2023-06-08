from typing import Any, Optional

UNKNOWN_CODES = []
VALID_STARTING_LETTERS = "ABCDEFGHJKLMNPQRTUVWXYZ"


class UPN:
    MAX_LENGTH = 13

    def __init__(
        self,
        la_code: str,
        establishment_number: str,
        year_allocation: str,
        serial_number: str,
        check_letter: Optional[str] = None,
    ):
        if len(la_code) != 3 or not la_code.isnumeric():
            raise ValueError("The LA Code must be three digits long")
        if len(establishment_number) != 4 or not establishment_number.isnumeric():
            raise ValueError("The Establishment Number must be four digits long")
        if len(year_allocation) != 2 or not year_allocation.isnumeric():
            raise ValueError(
                "The Year Allocation must be the last two digits of the year (e.g. 20xx)"
            )
        if len(serial_number) != 3:
            raise ValueError(
                "The Serial Number must be three characters long, with at least the first two being numbers"
            )

        self.la_code = la_code
        self.establishment_number = establishment_number
        self.year_allocation = year_allocation
        self.serial_number = serial_number

        if not check_letter:
            self.check_letter = self._check_letter()
        else:
            self.check_letter = check_letter

    def _check_letter(self):
        total = 0
        base_upn = (
            self.la_code
            + self.establishment_number
            + self.year_allocation
            + self.serial_number
        )
        for idx, item in enumerate(base_upn):
            if item.isnumeric():
                total += (idx + 2) * int(item)
            else:
                value = self._temporary_letter_to_value(item)
                total += (idx + 2) * int(value)
        remainder = total % 23
        return self._remainder_to_check_letter(remainder)

    def _temporary_letter_to_value(self, letter):
        return VALID_STARTING_LETTERS.index(letter) + 2

    def _remainder_to_check_letter(self, remainder: int) -> str:
        return VALID_STARTING_LETTERS[remainder]

    def format(self) -> str:
        return "".join(
            [
                self.check_letter,
                self.la_code,
                self.establishment_number,
                self.year_allocation,
                self.serial_number,
            ]
        )
