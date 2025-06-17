import random
tied= 0
win= 0
lost= 0
played= 0
mydict={
    "1": "ROCK",
    "2": "PAPER",
    "3": "SCISSOR",
    "4": "EXIT"

}

print("-----WELCOME TO ROCK, PAPER, SCISSORS GAME-----")
print("------------------------------------------------\n")
while True:
    print("Choose from following options: ")
    for key, value in mydict.items():
        print(f"{key}: {value}")
    user= input("Choose from (1-4): ")
    if user not in mydict.keys():
        print("\nPlease choose from (1-4)\n")
        continue
    if user== "4":
        print("Thanks for playing the game\n")
        print(f"You played for {played} times")
        print(f"You won {win} times")
        print(f"You lost {lost} times")
        print(f"You are tied {tied} times")
        break
    #user_choice= mydict[user]
    computer= random.choice(list(mydict.keys())[:-1])
    print(f"\nYOU CHOOSED {mydict[user]}")
    print(f"COMPUTER GENERATED {mydict[computer]}")
    if user==computer:
        print("YOU ARE TIED\n")
        played+=1
        tied+=1
        
    elif (user=="1" and computer=="3") or (user=="2" and computer=="1" ) or (user== "3" and computer== "2"):
        print("YOU WON\n")
        played+=1
        win+=1

    else:
        print("YOU LOST\n")
        played+=1
        lost+=1



    
