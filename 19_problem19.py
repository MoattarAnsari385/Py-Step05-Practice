# Create an empty set. Add five elements to the set, then remove one item and print the updated set.

my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)

print("Original set:", my_set)

my_set.remove(1)

print("Updated set:", my_set)