#Project - 2
# Simple calculator
# Greeting
print("Welcome to the python calculator!")

# taking the input form user for the calculation
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Operations start 
multiply = "1"
addition = "2"
subtracte = "3"
divide = "4"

# Using while loop to run the loop again 
while True:
 print("You to choose 1,2,3,4, where \n 1 indicates multiplicatioin \n 2 indicates additioin \n 3 indicates substracte \n 4 indicates division.")
 choose = input("Please choose your operation: ")

# Using the if else statement to execute the caluclation 
 if choose == "1":
    print(a*b)
 elif choose == "2":
    print(a+b)
 elif choose == "3":
    print(a-b)
 elif choose == "4":
    print(a/b)
 else:
    print("You choose the wrong operation.")

# Here's user will tell that the calculation has done or not 
 ans = input("Have you done calculation? (yes/no): ")
 if ans == "yes":
    break

print("Hope it did work efficiently!")
