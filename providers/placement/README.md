# Placement
Generates a random placement, or data about that placement

## Usage
### placement
Generates a list with the following values:

* placement_type 
* placement_code 
* home_postcode 
* place_postcode 
* urn

Example usage
```python
# Generate a random child ID
fake.placement()
```

### place_change_reason_code

Can take an optional argument: `length` which determines
how many codes are returned

Example usage
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

### placement_type

Can take an optional argument: `age` which will use different probabilities if:

* The age is below 5
* The age is below 16

Example usage
```python
# Generate a placement type using the default weighting
fake.placement_type()
# returns something like 
# "A4"

# Generate a placement type using the age weighting for < 16
id = fake.placement_type(
    age=10
)
# Returns something like: 
# "K1"
```

### placement_provider_urn

Creates a 7-digit URN (Unique Reference Number) used to identify a provider

Example usage:
```python
fake.placement_provider_urn()
# returns something like
# 1234567
```