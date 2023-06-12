# Ethnicity Codes
This provider generates random ethnicity codes of the type used in many 
government data

## Usage
### ethnicity_code

Can take an optional argument: `length` which determines
how many codes are returned

example usage
```python
# Generate a random child ID
fake.ethnicity_code()
# returns something like 
# "BAFR"

# Generate a random child ID using custom limits
id = fake.ethnicity_code(
    length=10
)
# Returns something like: 
# ['AIND', 'BCRB', 'MWBC', 'WOTH', 'MWAS', 'NOBT', 'BAFR', 'APKN', 'WIRI', 'WIRI']
```