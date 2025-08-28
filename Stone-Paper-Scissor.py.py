import random

#Greetings!
print("Welcome to Stone-Paper-Scissors Game! ")

#Game informations.
print("You have to choose anyone 'stone','paper','sissor'")
print("'s' indicates stone\n'p' indicates paper\n'si' indicates sissor")

options = ["s","p","si"]

#Using while loop to execute the game again and again.
while True:
     
#User choice
     user = input("what would you wanna choose: ").lower()

#Computer choice
     comp = random.choice(options)

#Using if-else statement to checking the winner.
     if user==comp:
        print("Draw")
     elif user=='s' and comp=='p':
            print("Computer Wins!")
     elif user=='p' and comp=='s':
             print("You Wins!")
     elif user=='p' and comp=='si':
                print("Computer Wins!")
     elif user=='si' and comp=='p':
                 print("You Wins!")
     elif user=='s' and comp=='si':
                  print("You Wins!")
     elif user=='si' and comp=='s':
                   print("Computer wins!")
     else:
            print("Invalid choice, please try agian.")
#Asking from user to play more or not.
     ans = input("You wanna play more (y/n): ")
     if ans != "y":
         break
