# Write a program to create a dictionary of Hindi words with values as thier English tralsation. Provide user with an option to look it up!

words = {
    "madad" : "help", 
    "kursi" : "chair", 
    "Dosti" : "Friendship", 
    "Azadi" : "Freedom", 
    "Haqeeqat" : "Reality", 
    "Umeed" : "Hope", 
    "Khushi" : "Happiness", 
}

print("Welcome to the Urdu-English Dictionary!")
print("Available words:", list(words.keys()))
word = input("Enter the word you want the meaning of (from the above list): ")

print(words[word])