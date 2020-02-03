# def is_phone_number(text):
#     if len(text) != 12:
#         return text + ' is not a phone no'
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return text + ' is not a phone no'
#     if text[3] != '-':
#         return text + ' is not a phone no'
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return text + ' is not a phone no'
#     if text[7] != '-':
#         return text + ' is not a phone no'
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return text + 'is not a phone no'
#     return text + ' is a phone no'
#
#
# # print('415-355-4848 is a phone number :')
# print(is_phone_number('415-385-4848'))
# # print('Moshi Moshi is a phone number :')
# print(is_phone_number('Moshi Moshi'))


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
        return True


print('415-355-4848 is a phone number :')
print(is_phone_number('415-385-4848'))
print('Moshi Moshi is a phone number :')
print(is_phone_number('Moshi Moshi'))
