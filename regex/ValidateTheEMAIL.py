import re


email = "ak@gmail.com ask#gmail.com  asdf@gmail.asdf  aa@g.com bb@gm.in"
print('Emails : ', len(re.findall("[\w._+%-]{1,20}@[\w.-]{2,4}.[A-Za-z]{2,3}", email)))

