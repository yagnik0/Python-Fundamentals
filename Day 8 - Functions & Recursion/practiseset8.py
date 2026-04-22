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

# 2nd method withod return:- 

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

# celcius = int(input("Enter the celcius:- "))

# def convertToFahrenheit(celcius):
#   return (celcius * 9/5) + 32

# fahrenheit = convertToFahrenheit(celcius)
# print(f"The conversion of {celcius} C is {fahrenheit} F")

# Q.3 :- Write a python function which converts inches to cms.🚀

# inches = int(input("Enter the inches :- "))

# def inchesTocms(inches):
#   cms = inches * 2.54
#   print(cms)

# inchesTocms(inches)

# Q.4:- Write a python function to print multiplication table of a given number

number = int(input("Enter the number:- "))

def multiplication(number):
  for i in range(1,10):
    print(number * i)
  
multiplication(number)


