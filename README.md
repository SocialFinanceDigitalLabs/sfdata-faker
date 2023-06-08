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
### UPN
This provider generates random UPN values. There are two generators available:
`upn` that does checks for valid UPN values, and `upn_simple` that generates values
that may or may not be valid (it doesn't check)

These can be used as follows:
```
# Generate a random valid UPN
fake.upn()

# Generate a random valid UPN given a specific LA code to use
fake.upn(la_code=`123`)

# Generate 10 unique UPNs:
upns = []
for item in range(0,10):
    upns.append(fake.unique.upn_simple())
```

