# message = 'hello my name is Akhilesh Kumar bhagat'
# count = {}
# for i in message:
#     count.setdefault(i, 0)
#     print(count[i], i)
#     count[i] = count[i]+1
# print(count)

import pprint
message = 'hello my name is Akhilesh Kumar bhagat'
count = {}
for i in message:
    count.setdefault(i, 0)
    # print( i)
    count[i] = count[i]+1
    print(count[i])
# print(pprint.pformat(count), len(message))
pprint.pprint(count)


