# Reason Place Change Code
 Generates a random reason for placement change from the codeset.

## Usage
### place_change_reason_code

Can take an optional argument: `length` which determines
how many codes are returned

example usage
```python
# Generate a random child ID
fake.place_change_reason_code()
# returns something like 
# "CARPL"

# Generate a random child ID using custom limits
id = fake.place_change_reason_code(
    length=10
)
# Returns something like: 
# ['CARPL', 'CREQO', 'CUSTOD', 'CREQB', 'CARPL', 'CREQO', 'CUSTOD', 'CREQB', 'CUSTOD', 'CREQO']
```