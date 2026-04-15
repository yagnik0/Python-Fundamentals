s = {1,3,32}

# Empty sets :- don't use s= {} as it will create an empty dictionary use = set()

empty = set()

# In set values cannot be repeated

# Methods in sets:- 🐍

s.add(566)
s.remove(1)
print(s, type(s))


# Unions in sets
s1= {1,2,34}
s2 = {56,78,23,1}

print(s1.union(s2))

# Intersection in Sets

print(s1.intersection(s2))
