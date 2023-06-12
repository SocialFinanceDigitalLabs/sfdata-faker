from .. import Provider as Provider
from faker.providers.address import BaseProvider as AddressProvider
from faker import Faker


class Provider(Provider):
    fake = Faker("en_GB")
    fake.add_provider(AddressProvider)
    pass
