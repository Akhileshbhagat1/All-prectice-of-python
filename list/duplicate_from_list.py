# Write a Python program to remove duplicates from a list.[1,2,8,9,6,7,3,1,5,9]


def take_a_list(list_one):
    final_1 = []
    for i in list_one:
        if i not in final_1:
            final_1.append(i)
    return final_1


print(take_a_list([1, 2, 8, 9, 6, 7, 3, 1, 5, 9]))

a = [1, 2, 8, 9, 6, 7, 3, 1, 5, 9]
print(list(set(a)))
