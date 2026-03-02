age  = int(input("Enter your age:- "))

# if elif else ladder

if(age>=18):
  print("You are eligible for vote")
elif(age<0):
  print("Age cannot be in negative")
elif(age==0):
  print("Age canot be zero")
else:
  print("You are not eligible for vote")
