import re


data = '123451'
print("Matches: ", len(re.findall("\d{3}", data)))