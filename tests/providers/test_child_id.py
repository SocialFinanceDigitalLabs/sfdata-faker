import pytest
from faker import Faker
from providers.child_id.en_GB import Provider as ChildIDProvider


class TestChildID:
    fake = Faker("en_GB")
    fake.add_provider(ChildIDProvider)

    def test_child_id_range(self):
        id = self.fake.child_id(min=1, max=5)
        assert id >= 1
        assert id <= 5
