# Q.1 :- Write a program to print multiplication table of a given number using for loop

# num = int(input("Enter a number:- "))

# for i in range(1,11):
#     print(num * i)

# Q.2 :- Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#   if(i[0]== "S"):
#     print("Greetings", i)

# 2nd method

# for name in l:
#   if(name.startswith("S")):
#     print(f"Hello {name}")

# Q.3:- Attempt problem 1 using while loop.

# num = int(input("Enter a number:-"))

# i = 1

# while(i <= 10):
#   print(i * num)
#   i+=1 
  

# Q.4:- Write a program to find whether a given number is prime or not

# n = int(input("Enter a number:-"))

# for i in range(2, n):
#   if(n%i == 0):
#     print("Number is not prime")
#     break
# else:
#   print("Number is prime")


# Q.5:- Write a program to find the sum of first n natural numbers using while loop

# n = int(input("Enter a number:- "))

# i= 1
# sum = 0

# while(i<= n):
#   sum += i
#   i += 1
  
# print(sum)


# Q.6:- Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number:- "))

product = 1

for i in range(1, n+1):
  product = product * i

print(f"factorial of {n} is {product}")






