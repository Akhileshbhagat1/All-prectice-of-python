# Write a Python program to count the number of strings,
# where the string length is 2 or more,
# and the first and last character are same from a given list of strings

# #ex: Sample List : ['abc', 'xyz', 'aba', '1221']
# #Expected Result : 2


def count_no_of_string(listt):
    current_word = 0
    for word in listt:
        if len(word) > 1 and word[0] == word[-1]:
            current_word += 1
    return current_word


print(count_no_of_string(['aka', 'abc', 'ana', '1221', 'a11', 'p2aa']))
