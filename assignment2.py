# Creating Sets
set1 = {10, 20, 30, 40, 50, 60, 70, 80}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)

# Adding
set1.add(90)
print("Adding:", set1)

# Accessing through loop
for num in set1:
    print("Accessing:", num)

# Union of Sets
union_set = set1.union(set2)
print("Union set:", union_set)

# Intersection of Sets
intersection_set = set1.intersection(set2)
print("Intersection Set:", intersection_set)