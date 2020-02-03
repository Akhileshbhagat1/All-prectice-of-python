# Write a Python script to sort (ascending and descending) a dictionary by value
import operator
d = {1: 2, 2: 3, 3: 4, 5: 9, 9: 9, 6: 5, 4: 7}
print('original dictionary is', d)
sorted_a_d = sorted(d.items(), key=operator.itemgetter(0))
print("dictonary is assending order" + str(sorted_a_d))
