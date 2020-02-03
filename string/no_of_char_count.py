# ######### working
# string = input('enter your word: ')
# f = {}
# for i in string:
#     f[i] = f.get(i, 0)+1
# print(f)
# print (dict(f))

#################
# string = input('enter your word: ')
# f = {}
# for i in string:
# 	f[i] = f.get(i, 0)+1
# print(f)
# ############ length of string
# inpu = input("enter a string for count : ")
#
#
# def len_count(strf):
#     count = 0
#     for i in strf:
#         count += 1
#     # return count
#     print(count)
#
#
# len_count(inpu)

# inpu = input("enter a string for count : ")
# print(len(inpu))

# ###################### wap to find a longest word from given list


# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1]
#
#
# print(find_longest_word(["PHP", "Exercises", "Backend", "pythonwithdjango"]))

# ###########or ########
# def find_longest_word(text):
#     longest_word = max(text,  default=True)
#     return longest_word, len(longest_word)
#
#
# find_longest_word(['abc', 'akhil', 'bhagat', 'jadav'])

# ########################################################

# text = input("Please input a list of words to evaluate: ")
#
#
# def main():
#
#     longest = 0
#
#     for words in text.split():
#         if len(words) > longest:
#             longest = len(words)
#             longest_word = words
#
#
# print("The longest word is", longest_word, "with length", len(longest_word))
# main()

#########################################################
# def add_tags(tag, word):
# 	return "<%s>%s</%s>" % (tag, word, tag)
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))

# ### string reverse
# a = 'stringofstringwithsomerulesandrevolution'
# print(''.join(reversed(a)))

# ###################### WAP to find n largest word from a list

from itertools import count


def longest_word(lst, k):
    cnt = count()
    return sorted(lst, key=lambda a: (len(a), next(cnt)), reverse=True)[:k]


lst = ['i', 'am', 'akhilesh', 'and', 'have', 'completed', 'bechlor']
k = 3
print(longest_word(lst, k))
