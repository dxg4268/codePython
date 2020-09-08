x = 18
i = 0
z = 9

while(True):

    z = z - 1
    i = i + 1

    y = int(input("Enter a number to guess the true one : "))

    if y > 0 and y <= 14:
        print("Number is greater than what you entered ")
        print("Lives : " , z)
    elif 14 < y <= 17:
        print("You are very near! But the number is greater than value entered")
        print("Lives : " , z)
    elif x < y:
        print("Number is less than what you entered")
        print("Lives : " , z)
    else:
        print("You have guessed the number!")

        if i == 1:
            print("You took ", i, " guess")
        else:
            print("You took ", i, " guesses")
        
        break
    
    
    
    if i == 9:
        print("Game Over")
        break




    