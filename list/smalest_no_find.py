def smallest_no_in_list(list_of):
    min_of = list[0]
    for i in list_of:
        if i < min_of:
            min_of = i
    return min_of


print(smallest_no_in_list([5, 8, 36, 5, 1]))
