# inpu = input("enter a string for count : ")
# def len_count(str):
    #count = 0
   # for i in str:
  #      count += 1
 #   print(count)
#len_count(inpu)

#inpu = input("enter a string for count : ")
#print(len(inpu))
text = input("Please input a list of words to evaluate: ")
longest = 0
for words in text.split():
    if len(words) > longest:
        #longest = len(words)
        longest_word = words
print("The longest word is", longest_word, "with length", len(longest_word))
 
