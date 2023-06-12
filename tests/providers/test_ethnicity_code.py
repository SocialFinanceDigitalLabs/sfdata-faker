import pytest
from faker import Faker
from providers.ethnicity_code.en_GB import Provider as EthnicityCodeProvider
from providers.ethnicity_code.ethnicities import ETHNICITY_CODES


class TestEthnicityCode:
    fake = Faker("en_GB")
    fake.add_provider(EthnicityCodeProvider)

    def test_basic_ethnicity_code(self):
        eth = self.fake.ethnicity_code()
        assert eth in ETHNICITY_CODES

    def test_multiple_ethnicity_codes(self):
        eth = self.fake.ethnicity_code(length=10)
        assert len(eth) == 10

    def test_ethnicity_code_weighting(self):
        from collections import OrderedDict

        eth = self.fake.ethnicity_code(
            codes=OrderedDict([("TEST", 0.01), ("YES", 0.99)])
        )
        assert eth == "YES"
