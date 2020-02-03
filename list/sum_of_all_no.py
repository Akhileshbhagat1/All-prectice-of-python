def to_add(items):
    total = 0
    for i in items:
        total += i
    return total


print(to_add([2, 5, 7, 5]))


# #############same as above

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(sum_list([1, 2, -8]))
