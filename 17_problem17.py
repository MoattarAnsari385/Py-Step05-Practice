'''
    Create two sets set1 and set2. Perform the following operations:
    Union
    Intersection
    Difference
    Symmetric Difference 
'''

# Step 1: Create set1 and set2

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}

# Step 2: Perform union operation

union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")

# Step 3: Perform intersection operation

interset_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {interset_set}")

# Step 4: Perform difference operation
diff_set = set1.difference(set2)
print(f"Difference of set1 and set2: {diff_set}")

# Step 5: Perform symmetric difference operation
sym_diff_set = set1.symmetric_difference(set2)
print(f"Symmetric Difference of set1 and set2: {sym_diff_set}")