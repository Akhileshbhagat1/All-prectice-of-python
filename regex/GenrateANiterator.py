import re


data = "we need to inform the latest information"
for i in re.finditer("inform", data):    # finditer() returns the starting as well as the ending index of the matching
                                         # object
    actual_data = i.span()
    print(actual_data)
