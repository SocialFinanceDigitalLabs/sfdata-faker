import pytest
from faker import Faker
from providers.UPN.en_GB import Provider as UPNProvider
from providers.UPN import UPN
import unittest


class TestUPN:
    fake = Faker("en_GB")
    fake.add_provider(UPNProvider)

    def test_check_letter_is_correct(self):
        upn = self.fake.upn(
            la_code="801",
            establishment_number="2000",
            year_allocation="01",
            serial_number="001",
        )
        assert upn[0] == "H"

    def test_temporary_check_letter_is_correct(self):
        upn = self.fake.upn(
            la_code="801",
            establishment_number="2000",
            year_allocation="01",
            serial_number="00A",
            temporary=True,
        )
        assert upn[0] == "X"

    def test_la_code_length_error(self):
        with pytest.raises(Exception):
            upn = self.fake.upn(
                la_code="8010", establishment_number="2000", year_allocation="01"
            )

    def test_la_code_format_error(self):
        with pytest.raises(Exception):
            upn = self.fake.upn(la_code="80G")
