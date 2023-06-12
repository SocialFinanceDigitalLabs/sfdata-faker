# Child ID
This provider generates random Child IDs. While essentially just a random number
which could be generated using the faker library, this will likely need to be modified
to allow for different types of child ids in the future.

## Usage
### child_id

Child id takes two optional arguments: `min`, and `max` which specify the smallest value
that can be used, and the largest value that can be used.

example usage
```python
# Generate a random child ID
fake.child_id()

# Generate a random child ID using custom limits
id = fake.child_id(
    min=0
    max=100
)
```