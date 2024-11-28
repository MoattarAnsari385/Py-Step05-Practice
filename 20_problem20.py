# Given two sets set1 and set2, write a function that returns and prints the difference between the two sets (items in set1 but not in set2).

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}

diff_set = set1.difference(set2)
print(f"Difference of set1 and set2: {diff_set}")