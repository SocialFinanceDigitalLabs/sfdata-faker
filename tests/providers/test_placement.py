import pytest
from faker import Faker
from providers.placement.en_GB import Provider as PlacementProvider
from providers.placement.placement import (
    PLACE_CHANGE_CODES,
    PLACEMENT_TYPE_CODES,
    PLACEMENT_CODES,
)


class TestPlacement:
    fake = Faker("en_GB")
    fake.add_provider(PlacementProvider)

    def test_basic_place_change_reason_code(self):
        eth = self.fake.place_change_reason_code()
        assert eth in PLACE_CHANGE_CODES

    def test_multiple_place_change_reason_code(self):
        eth = self.fake.place_change_reason_code(length=10)
        assert len(eth) == 10

    def test_place_change_reason_code_weighting(self):
        from collections import OrderedDict

        eth = self.fake.place_change_reason_code(
            codes=OrderedDict([("TEST", 0.00), ("YES", 1.00)])
        )
        assert eth == "YES"

    def test_placement_type_codes_probabilities(self):
        total_probability = sum(
            value["probability"]
            for value in PLACEMENT_TYPE_CODES.values()
            if "probability" in value
        )
        assert round(total_probability, 3) == 1

    def test_placement_type_codes_probabilities_under_five(self):
        total_probability = sum(
            value["probability_age_5"]
            for value in PLACEMENT_TYPE_CODES.values()
            if "probability_age_5" in value
        )
        assert round(total_probability, 3) == 1

    def test_placement_type_codes_probabilities_under_sixteen(self):
        total_probability = sum(
            value["provability_age_16"]
            for value in PLACEMENT_TYPE_CODES.values()
            if "provability_age_16" in value
        )
        assert round(total_probability, 3) == 1

    def test_placement(self):
        this_placement = self.fake.placement()
        assert len(this_placement) == 5
        assert this_placement[0] in PLACEMENT_TYPE_CODES.keys()
        assert this_placement[1] in [code[0] for code in PLACEMENT_CODES["even"]]
