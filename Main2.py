# Game Development: Snake Water Gun:
import random
i = 1
score = 0
print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

while(i<=10):
    computer_guess = ["Snake", "Water","Gun"]
    choice = random.choice(computer_guess)
    print("Enter one of them: S,W,G")
    j = input()
    n= j.upper()
    if n=="S" or n=="W" or n=="G":
        if choice=="Snake" and n=="S":
            print("****Match Drawn****")
        elif choice=="Snake" and n=="W":
            print("****You loose!****")
            print("****computer win!****")
        elif choice=="Snake" and n=="G":
            print("****you win!****")
            print("****computer loss!****")
            score +=1
        elif choice=="Water" and n=="W":
            print("****Match Draw****")
        elif choice=="Water" and n=="S":
            print("****you win!****")
            print("****computer loss!****")
            score += 1
        elif choice=="Water" and n=="G":
            print("****computer win!****")
            print("****you loss!****")

        elif choice=="Gun" and n=="G":
            print("****Match Draw****")
        elif choice == "Gun" and n=="S":
            print("****computer win!****")
            print("****you loos!****")

        elif choice=="Gun" and n=="W":
            print("****computer win!****")
            print("****you loos!****")

        i+=1
    else:
        print("Please Enter correct input ")
print("Your Total Score is :  ",score)
