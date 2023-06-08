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

#### upn
You can call this without any arguments, but you can also specify specific 
parts of the number to use. The UPN has the following format:

CLLLEEEEYYSSS

Where:
C = Check Letter, used to make sure the UPN is valid
L = Local Authority Code
E = Establishment Number - Uniquely identifies each establishment/school in the LA
Y = Year pupil is allocated a number
S = Unique identifier for that pupil

You can specify these when creating a random UPN like so:
```python
my_upn = upn(
    check_letter = "H",
    la_code = "123",
    establishment_number "123",
    year_allocation "23",
    serial_number = "123"
)
```
In that way, you can generate UPN codes that may make more sense for a 
given data set.  There is also the `temporary` argument, that if specified, will
generate Temporary UPN values that end in a letter (J12312342357V).

```python
my_temporary_upn = upn(temporary=True)
```

#### upn_simple
This is the same as the UPN function above, but generates a string that
looks like a UPN, but may or may not pass validity. There is only one
argument that can be specified, `temporary`

```python
my_upn = upn_simple()
my_temporary_upn = upn_simple(temporary=True)
```