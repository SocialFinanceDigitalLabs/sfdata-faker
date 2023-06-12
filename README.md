# sf-faker
Faker Providers for Use in Generating Fake Data

## Usage:
These providers are designed to be used with the faker library. In order 
to utilise these, you must first import faker, and then import these
providers, connecting them with the `add_provider` function like the following
example:

```python
from faker import Faker
from providers import UPN

fake = Faker('en_GB')

fake.add_provider(UPN.Provider)
```

## Providers
* Unique Identifiers
  * [UPN](./providers/UPN/README.md) - Provider for creating a Unique Pupil Number
  * [Child Id](./providers/child_id/README.md) - Provider for creating unique child IDs
* Personal Metadata
  * [Ethnicity Code](./providers/ethnicity_code/README.md) - Provider for generating random ethnicity codes
* Other
  * [Placement](./providers/placement/README.md) - Generates details about a placement or placement change

### Some Common Needs This Does Not Handle:
These are generators we've used in creating data sets where there wasn't a need to reimagine here:
* [Date of Birth](https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html?highlight=date#faker.providers.date_time.Provider.date_of_birth) - Instead use the built-in faker [to pick a random birthday given an age](https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html#faker.providers.date_time.Provider.date_of_birth)

### Sources
A lot of these providers are based on work done in the following repositories:
* [CSC Data Synthesizer](https://github.com/SocialFinanceDigitalLabs/csc-data-synthesizer/blob/main/cscsynth)