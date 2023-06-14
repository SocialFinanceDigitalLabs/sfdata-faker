from .. import Provider as Provider
from providers.UPN import Provider as UPNProvider
from providers.ethnicity_code import Provider as EthnicityCodeProvider
from faker import Faker


class Provider(Provider):
    fake = Faker("en_GB")
    fake.add_provider(UPNProvider)
    fake.add_provider(EthnicityCodeProvider)
    pass
