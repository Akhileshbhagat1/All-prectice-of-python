def even_no():
    for v in range(2,50):
        if (v%2==0):
           yield v

i=even_no()
count=0
#print(next(i))
#print(next(i))
"""by for loop"""
#for k in i:
 #   print (k)
  #  count +=1
"""by while loop"""
while True:
    try:
        print(next(i))
        count +=1
    except(StopIteration):
        break
print("even no between 10:-",count)    
        


