import intbitset

arr1 = intbitset.intbitset([1, 3, 4, 5, 2])
arr2 = intbitset.intbitset([1, 3, 4])
arr3 = intbitset.intbitset([1, 3, 232, 44])


arr1.intersection(arr2)
arr3.union(arr1)

print(arr1)
print(arr3)
