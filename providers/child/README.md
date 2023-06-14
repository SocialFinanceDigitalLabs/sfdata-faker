# Child
This provider generates random data about a Child. 

## Usage
### child
Generates data about a single child. Takes a few optional arguments: `sex` which is either 'M' or 'F', 
and `age` which is the child's age. What is returned is a dictionary containing details about the generated 
child.

example usage
```python
fake.child()
# Returns something like:
# {
#   'first_name': 'Hayley', 
#   'last_name': 'Sutton', 
#   'ethnicity': 'MWBA', 
#   'sex': 'F', 
#   'upn': 'A454961504220', 
#   'birthdate': datetime.date(2013, 3, 15)
# }

fake.child(sex='M', age=10)
# Returns something like:
# {
#   'first_name': 'Terence', 
#   'last_name': 'Hunt', 
#   'ethnicity': 'REFU', 
#   'sex': 'M', 
#   'upn': 'A521397915956', 
#   'birthdate': datetime.date(2012, 7, 16)
# }
```

### child_id
While essentially just a random number which could be generated using the faker library, this will 
likely need to be modified to allow for different types of child ids in the future. Child id takes 
two optional arguments: `min`, and `max` which specify the smallest value that can be used, and the 
largest value that can be used.

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