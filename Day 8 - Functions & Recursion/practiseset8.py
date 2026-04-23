# Q.1:- Write a program using functions to find greatest of three numbers 🚀

# num1 =  int(input("Enter your first number :- "))
# num2 =  int(input("Enter your second number :- "))
# num3 =  int(input("Enter your third number :- "))

# def greatest(num1, num2, num3):
#   if( num1>num2 and num1>num3):
#     return num1
#   elif( num2>num1 and num2>num3):
#     return num2
#   else:
#     return num3
  
# greatestNum =  greatest(num1,num2,num3)
# print(f"The greatest of all three numbers is {greatestNum}")

# 2nd method with return:- 

# num1 =  int(input("Enter your first number :- "))
# num2 =  int(input("Enter your second number :- "))
# num3 =  int(input("Enter your third number :- "))

# def greatest(num1, num2, num3):
#   if( num1>num2 and num1>num3):
#     print(f"{num1} is the greatest ")
#   elif( num2>num1 and num2>num3):
#     print(f"{num2} is the greatest")
#   else:
#     print(f"{num3} is the greatest")
  
# greatest(num1,num2,num3)

# Q.2:- Write a python program using function to convert Celsius to Fahrenheit.🚀


# def convertToFahrenheit(celcius):
#   return (celcius * 9/5) + 32

# celcius = int(input("Enter the celcius:- "))
# fahrenheit = convertToFahrenheit(celcius)
# print(f"The conversion of {celcius} C is {fahrenheit} F")

# Q.3 :- Write a python function which converts inches to cms.🚀

# inches = int(input("Enter the inches :- "))

# def inchesTocms(inches):
#   cms = inches * 2.54
#   print(cms)

# inchesTocms(inches)

# Q.4:- Write a python function to print multiplication table of a given number 🚀

# number = int(input("Enter the number:- "))

# def multiplication(number):
#   for i in range(1,10):
#     print(number * i)
  
# multiplication(number)

# Q.5:- How do you prevent a python print() function to print a new line at the end.🚀

# print("a")
# print("b")
# print("c", end="")
# print("d", end="")

# end="" :- allow us to prevent print to not too print from new line in python. 🐍

# Q.6:- Write a recursive function to calculate the sum of first n natural numbers.🚀

# 1 = 1
# 2 = 2 + 1
# 3 = 3 + 2 + 1
# 4 = 4 + 3 + 2 + 1
# 5 = 5 + 4 + 3 + 2 + 1
# n = n + (n-1) + (n-2) .... 3 + 2 + 1
# n = n + sumOfnatural(n-1)

#  My Approach :-

# def sumOfN(num):
#   if(num==0):
#     return 0
#   elif (num == 1):
#     return 1
#   return num + sumOfN(num-1)

# num = int(input("Enter your number:- "))
# sumOfnatural = sumOfN(num)
# print(f"The sum of {num} natural number is {sumOfnatural}")

# Optimize approach :- 

# def sumOfN(num):
#   if(num<=1):
#     return num
#   return num + sumOfN(num-1)

# num = int(input("Enter your number:- "))
# sumOfnatural = sumOfN(num)
# print(f"The sum of {num} natural number is {sumOfnatural}")


# Q:- Write a python function to remove a given word from a list ad strip it at the same time. 🚀

def remove(l,word):
  n = []
  for item in l:
    if not(item == word):
      n.append(item.strip(word))
  return n


l = ["Harry", "Rohan", "Subham", "Arjun", "an"]

print(remove(l, "an"))