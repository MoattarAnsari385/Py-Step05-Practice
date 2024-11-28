# If the language of 2 friends are same; what will happen to the program in problem 6?

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

# If two friends have the same language, the program will assign the same value to different keys (friends' names) without any issue.
#    Example: {'Ali': 'Python', 'Ahmed': 'Python'} is valid.
