

while True:
    print("Enter a year for check Leap year or not (or q for quit) : ")
    year = input()
    if year == 'q':
        break
    else:
        if int(year) % 400 == 0:
            print(f'{year}' " is a leap year")
        elif int(year) % 4 == 0:
            print(f'{year}' " is a leap year")
        elif int(year) % 100 == 0:
            print(f'{year}' " is not a leap year")
        else:
            print(f'{year}' " is not a leap year")

