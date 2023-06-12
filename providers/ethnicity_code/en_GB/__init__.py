from .. import Provider as Provider
from faker import Faker


class Provider(Provider):
    fake = Faker("en_GB")
    pass
