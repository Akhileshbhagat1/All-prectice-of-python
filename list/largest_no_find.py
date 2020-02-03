# [1,9,8,3,7]

# a = [1,9,8,3,7]
# print(max(a)

# another method


def max_in_list(listt):
    max_of = listt[0]
    for i in listt:
        if i > max_of:
            max_of = i
    return max_of


print(max_in_list([5, 8, 9, 7, 23]))
