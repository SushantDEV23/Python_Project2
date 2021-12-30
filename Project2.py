import random
print("****Welcome, You are in the GUESS GAME****")

randomno=random.randint(1,100)

userguess=None
guess=0
while(userguess!=randomno):
    userguess=int(input("Enter the no. ...... "))
    guess+=1
    if userguess==randomno:
        print("You Guesses it right!!Congrats")
    else:
        if(userguess>randomno):
            print("Guess a lower no.")
        else:
            print("Guess a larger no.")


print(f"The no. of guess it took you to guess it perfectly is {guess}")

with open("Hiscores.txt",'r') as f:
    Hiscore=int(f.read())
if(guess<Hiscore):
    print("Record Broken, congrats!!!!!")
    with open("Hiscores.txt",'w') as f:
        f.write(str(guess))