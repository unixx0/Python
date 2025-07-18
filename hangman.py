import random
turn= 11
guessed_letter=[]   #for tracking the letters guessed by the user
words= ["apple", "banana", "pineapple", "cherry","litchi", "mango", "orange" ]
guess= random.choice(words)
#print(guess)
number= random.sample(range(len(guess)),2)
number.sort()
#print(number)

#create a list with number of "_" which is equal to the length of the guess
computer=[]
for _ in guess:
    computer.append("_")
#print(computer)

for x in number:
    computer[x]= guess[x]
print("-----WELCOME TO HANGMAN GAME-----\n")
print(f"-----INITIALLY YOU HAVE {turn} ATTEMPTS LEFT-----\n")
print("YOUR WORD IS: ")
print("".join(computer))

while True:
    user= input("Enter the letter you want to insert: ").lower()
    if len(user)!=1 or not user.isalpha() or user==" " or user=="":
            print("PLEASE ENTER SINGLE LETTER\n")
            print("".join(computer))
            continue
    if user in guessed_letter:
        print("YOU HAVE ALREADY GUESSED THIS LETTER\n")
        print("".join(computer))
        continue
    else:
        guessed_letter.append(user)

    if user in guess:
        for i in range(len(guess)):
            if guess[i]==user:
                computer[i]= user 
        print("YOU HAVE GUESSED CORRECT LETTER\n")
    
        
    if user not in guess:
        print("YOU HAVE ENTERED INCORRECT LETTER")
        turn-=1
        print(f"You have {turn} attempt/s left\n")
    print("".join(computer))
    
    if ("".join(computer))==guess:
        print("CONGRATULATIONS!!! YOU HAVE GUESSED THE WORD CORRECTLY")
        break
    if turn== 0:
        print("SORRY THE GAME IS OVER :<<")
        print(f'THE CORRECT WORD WAS "{guess}"')
        break
        

