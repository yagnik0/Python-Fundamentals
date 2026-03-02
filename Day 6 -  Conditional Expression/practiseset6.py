# Q.1:-  Write a program to find the greatest of four numbers entered by the user.

# num1 = int(input("Enter your 1 number:- "))
# num2 = int(input("Enter your 2 number:- "))
# num3 = int(input("Enter your 3 number:- "))
# num4 = int(input("Enter your 4 number:- "))


# if(num1 > num2 and num1 > num3 and num1 > num4 ):
#   print("Number 1 is the greatest", num1)

# elif(num2 > num1 and num2 > num3 and num2 > num4):
#   print("Number 2 is the greatest", num2)

# elif(num3 > num4 and num3 > num2 and num3 > num1):
#   print("Number 3 is the greatest", num3)

# else:
#   print("Number 4 is the greatest", num4)

# Q.2:- Write a program to find out whether a student has passed or failed if it requires atotal of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# marks1 = int(input("Enter Marks 1:- "))
# marks2 = int(input("Enter Marks 2:- "))
# marks3 = int(input("Enter Marks 3:- "))

# # checking for total percentage

# totalPercentage = ((100) * (marks1 + marks2 + marks3))/300

# if(totalPercentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
#   print("You are passed", totalPercentage)
# else: 
#   print("You Failed, Try again", totalPercentage)


# Q.3 :- A spam comment is defined as a text containing following keywords:“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# p1= "Make a lot of money"
# p2 = "buy now"
# p3= "subscribe this"
# p4= "click this"

# message= input("Enter your comment:- ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#   print("This comment is a spam")
# else:
#   print("This comment is not a spam")

# Q.4 :- Write a program to find whether a given username contains less than 10 characters or not

# userName  = input("Enter username :- ")

# if(len(userName) < 10):
#   print("It contains less than 10 characters")
# else:
#   print("It contains more than 10 characters")

# Q.5 :- Write a program which finds out whether a given name is present in a list or not.

# namelist = ["yash", "krishna", "mahadev"]

# name = input("Enter the name:- ")

# if(name in namelist):
#   print("It is present in the list")
# else:
#   print("It is not present in the list")

# Q.6 :-  Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# marks  =  int(input("Enter your marks:- "))

# if(marks>=90 and marks<100):
#   print("Grade Ex")
# elif(marks>=80 and marks<90):
#   print("Grade A")
# elif(marks>=70 and marks<80):
#   print("Grade B")
# elif(marks>=60 and marks<70):
#   print("Grade C")
# elif(marks>=50 and marks<60):
#   print("Grade D")
# elif(marks>=40 and marks<50):
#   print("Grade E")
# else:
#   print("Grade F")

# Q.7:-  Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter your post:- ")

if("harry".lower() in post.lower()):
  print("Harry is there in post")
else:
  print("It is not there in the post")