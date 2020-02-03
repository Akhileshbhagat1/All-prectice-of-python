def multi_all(items):
    mul = 1
    for i in items:
        mul *= i
    return mul


print(multi_all([2, 5, 8]))
