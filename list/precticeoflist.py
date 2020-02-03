####################################
##add all items in a list
#a = [1,2,8,6,5]
# def a(num):
# 	total = 0
# 	for i in num:
# 		total += i
# 	return total
# print(a([2,5,6]))
################################################
# check largest no of the list

# def large(lsit):
# 	ma=0
# 	for i in lsit:
# 		if i>ma:
# 			ma = i
# 	return ma
# print(large([2,7,8,6, 15]))
################################################
#return if first and last character matched that value only fron that list

# def match_(listt):
# 	current = 0
# 	for i in listt:
# 		if len(i)>1  and i[0]==i[-1]:
# 			current += 1
# 	return current
# print(match_(['abc', 'aba', 'nan', 'mon']))
#######################################################################
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n):
# 	return n[-1]
# def take_a_tuple(tuple):
# 	return sorted(tuple, key=last)
# print(take_a_tuple([(2,1),(2,3),(4,3),(2,5),(3,4)]))


##################################
# # take second element for sort
# def takeSecond(elem):
#     return elem[0]

# # random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# # sort list with key
# sortedList = sorted(random, key=takeSecond, reverse=True)

# # print list
# print('Sorted list:', sortedList)

#########################################
# remove duplicates from lsit
# def rem(list):
# 	lsi = []
# 	for i in list:
# 		if i not in lsi:
# 			lsi.append(i)
# 	return lsi
# print(rem([1,5,7,5,3,1,7]))


#######################################
# check list is empty or not
# i = [1,2]
# if not i:
# 	print('list is empty')
# else:
# 	print('items in list are ', i)

#######################################
#Write a Python function that takes two lists and returns True if they have at least one common member.
# def take_two_list(list1, lsit2):
# 	results = False
# 	for i in list1:
# 		for j in lsit2:
# 			if i ==j:
# 				results = True
# 				return results
# print('non of items are available in both',take_two_list([1,2,5,4], [9,8,5,7]))
# print('here some elements are availabe in both lists',take_two_list([1,5,8,7,6],[1,8,6,5,7]))

#######################################################################
# import time
# t = time.time()
# print('current time is ', t)

##################################
# birthdays = {'Ak': 'Apr 1', 'Bk': 'Dec 12', 'Ck': 'Mar 4'}
# while True:
# 	print('Enter a name: (blank to quit)')
# 	name = input()
# 	if name == '':
# 		# print('you did not press any name')
# 		break

# 	if name in birthdays:
# 		print(birthdays[name] + ' is the birthday of ' + name)
# 	else:
# 		print('I do not have birthday information for ' + name)
# 		print('What is their birthday?')
# 		bday = input()
# 		birthdays[name] = bday
# 		print('Birthday database updated.')

############################################### Tic Toc Toe game Code
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#     	turn = 'O'
#     else:
#     	turn = 'X'
# printBoard(theBoard)

#############################################################################




























    
        
            
                
     
            
     
         
         
            
            
            


