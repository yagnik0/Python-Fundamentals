# Q.1:- Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

lang = {
  "pahad": "mountain",
  "nadi" : "river",
  "suraj" : "sun"
}

# word = input("Enter the word you want meaning of:- ")
# print(lang[word])

# Q.2:- Write a program to input eight numbers from the user and display all the unique numbers (once).

uniqueNum = set()

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# num3 = int(input("Enter the number: "))
# num4 = int(input("Enter the number: "))
# num5 = int(input("Enter the number: "))
# num6 = int(input("Enter the number: "))
# num7 = int(input("Enter the number: "))
# num8 = int(input("Enter the number: "))

# update() accepts a list/tuple of values
# uniqueNum.update({num1, num2, num3, num4, num5, num6, num7, num8})

# print(uniqueNum, type(uniqueNum))

# Q.4:- What will be the length of following set s:
    
s = set()
s.add(20)
s.add(20.0)
s.add('20')

# Interview perspective

# print(len(s))

# Q.6:- Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

favLang = {}

name = input("Enter your name:- ")
lang = input("Enter yor languaahe name:- ")
favLang.update({name:lang})

name = input("Enter your name:- ")
lang = input("Enter yor languaahe name:- ")
favLang.update({name:lang})

name = input("Enter your name:- ")
lang = input("Enter yor languaahe name:- ")
favLang.update({name:lang})

name = input("Enter your name:- ")
lang = input("Enter yor languaahe name:- ")
favLang.update({name:lang})

print(favLang)


