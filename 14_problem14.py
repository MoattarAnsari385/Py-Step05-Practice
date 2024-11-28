# Write a function that removes a specific key from a dictionary using the pop() method and then prints the modified dictionary

person = {
    'name': 'Ayesha',
    'age': 25,
    'city': 'Lahore'
}

print(f"Before removing key: {person}")

removed_value = person.pop('age')

print(f"After removing keys: {person}")

print(f"Removing Value: {removed_value}")

