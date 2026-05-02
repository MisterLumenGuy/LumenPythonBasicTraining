
import math

active = bool(True)

while active == True:

    print("Welcome to my calculator, give me the number/n")

    num1=float(input("Write the first number:"))
    num2=float(input("Write the second number:"))

    print()

    print("/n Choose and option")
    print("1- sum, 2- substraction, 3- multiplication, 4- division, 5- module, 6- square root, 7- exit")

    option = int(input())

    match option:

        case 1:
            print(f"the sum is {num1+num2}")
        case 2:
            print(f"the substraction is {num1-num2}")
        case 3:
            print(f"the multiplication is {num1*num2}")
        case 4:
            try:
                print(f"the division is {num1/num2}")
            except ZeroDivisionError :
                print("User, it's impossible to divide by zero")
        case 5:
            print(f"the module is {num1 % num2}")
        case 6:
            print("/n Which number you'll take")
            thenum = int(input())
            match thenum:
                case 1:
                    print(f"the module is {math.sqrt(num1)}")
                case 2:
                    print(f"the module is {math.sqrt(num2)}")
                case _:
                    print("invalid option")
        case 7:
            active = False
            print("Thanks for using this calc :)")

        case _:
            print("Invalid Option")


