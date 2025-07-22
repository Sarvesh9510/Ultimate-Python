# Logical Operators

e = True or False
print(e)
# This will print True because at least one of the conditions is True
f = True and False
print(f)
# This will print False because both conditions are not True
g = not True
print(g)
# This will print False because not True is False
h = not False
print(h)
# This will print True because not False is True
# This is a simple script to demonstrate the use of variables and arithmetic operations in Python

# Truth table of 'or'

print("True or False:", True or False)
print("True and True:", True and True)
print("False and True:", False and True)
print("False or False:", False or False)

# Truth table of 'and'
print("True and True:", True and True)
print("True and False:", True and False)   
print("False and True:", False and True)
print("False and False:", False and False)

# Truth table of 'not'
print("not True:", not True)
print("not False:", not False)

print(not(False))
# This will print True because not False is True

print(not(True))
# This will print False because not True is False
# This is a simple script to demonstrate the use of logical operators in Python

# Jo True ko False aur False ko True Bana de usse 'not' operator kehte hain
# Jo True aur False ko compare kare usse 'or' operator kehte hain
# Jo True aur False ko compare kare aur dono True ho to True de usse 'and' operator kehte hain