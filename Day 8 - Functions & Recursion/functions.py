# Creating a function and finding out the average of the three numbers :- 

# Function defination

# def avg():
#   a = int(input("Enter the first number:- "))
#   b = int(input("Enter the second number:- "))
#   c = int(input("Enter the third number:- "))

#   average = (a + b + c)/3
#   print(average)

# avg() # function call


# Write a program to greet a user with “Good day” using functions.

# user = input("Enter your name :- ")

# def greet(user):
#   print(f"Good day {user}")

# greet(user)

# Default parameters in functions

def goodDay(name, ending="Thank You"):
  print(f"Good day, {name}. {ending}")

# goodDay("krishna", "Thanks")

# Recursion :-  it is a process in which function call itself repeateadly

# factorial(0) = 1
# factorial(1) = 1
# factorail(2) = 2 X 1
# factorial(3) = 3 X 2 X 1
# factorial(4) = 4 X 3 X 2 X 1
# factorial(5) = 5 X 4 X 3 X 2 X 1
# factorial(n) = n X (n-1) X (n-2) .... 3 X 2 X 1

# factorial(n) = n * factorial(n-1)


# def factorial(num):
#   if (num == 1 or num == 0):
#     return 1
#   return num * factorial(num-1)

# num = int(input("Enter the number:- "))
# print(f"Factorial of {num} is {factorial(num)}")
