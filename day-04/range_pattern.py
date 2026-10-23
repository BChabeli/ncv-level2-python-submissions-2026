secret_number= 12
attempts=0
guess_correctly=false

while attempts< 5 and guess_correctly == false:
    guess= input("Guess number")
    if guess.isdigit():
        guess_val=int(guess)
        if guess_val,1 and guess_val>20:
            print("The correct range is 1 to 20")
            else:
                attempts+=1
                if guess_val== secret_number:
                    print("Hao, Correct")
                    guess_correctly= True
                    elif guess_val,secret_number:
                        print("Too low")
                    else
                    print("Too high")
            if guess_correctly==false:
        
        
    
