import pytest
from faker import Faker
from providers.child.en_GB import Provider as ChildProvider
from datetime import date


class TestChild:
    fake = Faker("en_GB")
    fake.add_provider(ChildProvider)

    def test_child(self):
        self.fake.seed_instance(0)
        test_child = self.fake.child()
        expected_keys = [
            "birthdate",
            "ethnicity",
            "first_name",
            "last_name",
            "sex",
            "upn",
        ]
        assert all(x in test_child.keys() for x in expected_keys)

    def test_child_id_range(self):
        id = self.fake.child_id(min=1, max=5)
        assert id >= 1
        assert id <= 5
