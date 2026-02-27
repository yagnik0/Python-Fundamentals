# Q.1 :-  Write a python program to display a user entered name followed by GoodAfternoon using input () function

# username = input("Enter your name:- ")

# print("Good afternoon,", username)


# Q.2 :- Write a program to fill in a letter template given below with name and date.

# name = "Bhootnath"
# date= "27/2/2026"

# letter = '''
# Dear name,
# You are selected!
# date
# '''

# letter = letter.replace("name", name)
# letter = letter.replace("date", date)

# print(letter)

# Another method with f- string 🐍-

# name = "Bhootnath"
# date = "27/2/2026"

# letter = f'''
# Dear {name},
# You are selected!
# {date}
# '''

# print(letter)

# Q.3:- Write a program to detect double space in a string.

string = "Hello my  name is Bramharshi yagnik"

d_space = string.find("  ")
# print(d_space)

# Q.4:-  Replace the double space from problem 3 with single spaces

new_string = string.replace("  "," ")
# print(new_string)

# Q.5:- Write a program to format the following letter using escape sequence characters.

letter = "Dear Harry,\n this python course is nice.\n Thanks!"
print(letter)





