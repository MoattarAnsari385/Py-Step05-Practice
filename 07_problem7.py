# If the name of 2 friends are same; what will happen to the program in problem 6?
dictionary = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

dictionary.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

dictionary.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

dictionary.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

dictionary.update({name: lang})

print(dictionary)

# If two friends have the same name, the previous value for that name will be updated with the new language value.
# Example: If 'Ali' is entered twice, the dictionary will store only the latest language for 'Ali'.