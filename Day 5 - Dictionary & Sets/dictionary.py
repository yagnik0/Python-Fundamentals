# Dictionary :-  List of key-value pairs

marks = {
  "Yash": 78,
  "Krishna":100,
  "Bramharshi": 89
}

# print(marks, type(marks))

# print(marks["Krishna"])

# Methods of dictionaries :- 🐍

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Yash": 80})
# print(marks)

# Interview Question 🐍

print(marks.get("Bramharshi"))  # prints none if its not in the list 
print(marks["Bramharshi"])  # prints a error if its not in the list 

  

