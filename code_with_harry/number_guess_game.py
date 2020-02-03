# n= 18
# attempt number of guess 5
# count how many  left chances you have
# if chances 0 then game over
original = 18
count = 5
game_over = False
while not game_over:
    print("Enter a number of your choice between 1 to 100  :")
    num = int(input())
    if original > num:
        print(" your no is lower then actual no")
        count = count - 1
        print('you have left ', count, 'chance')
        if count == 0:
            break
    elif original < num:
        print(" your no is greater then actual no")
        count -= 1
        print('you have left ', count, 'chance')
        if count == 0:
            break
    elif original == num:
        print('you have entered right number', num)
        game_over = True
        # break
    else:
        print('Please enter a valid number')




