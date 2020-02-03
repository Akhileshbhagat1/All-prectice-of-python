def pos(search, target):
    first = (search.find(target))
    #second = (search.find(target, first+1))
    #third = (search.find(target, second+2))
    return first+1

hob = "i like to play cricket and i am good  in cricket while cricket is the match is for all thats why cricket is popular"
a = pos(hob, "cricket")
print(a)
