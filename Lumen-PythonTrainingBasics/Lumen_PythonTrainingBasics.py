# Using Python From Visual Studio Comunnity 2026

# Python is an interpreted language known for its simplicity and large base of libraries.
#It suere is a slow language at execution time, still is the most popular programming language mainly due to its extensive use in data science and AI-related areas

# Here are a few examples of basic variables in python

from email.errors import InvalidBase64PaddingDefect


num = 1  #Here python use its duck typing to detect the data type we are using, in this case it detected it is an integer
number = int(1) #Here we use the optional static typing to tell python the data type is a number

name = "Lumen"
name = str("Lumen")

mar = False
married = bool(False)

hf = 0.5
half = float(0.5)

# These are tuples
yearandname= (2006, "Ant")
names = ("Lumen", "X", "Hero")


#Now, here are a few contants

PI = 3.1416
ISHUMAN = bool(True)

#Let's show'em

print(f"my name is {name}")
print(f"PI equals {PI}")

#Let's create an input and show it as an outpsut
newHuman = input("New Human is: ")
print(newHuman)

#Let's do some math

num1= int(input("Write the 1st number to calculate: "))
num2= int(input("Write the 2st number to calculate: "))
print(f"The result as a sum is {num1+num2}")