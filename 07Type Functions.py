a = 30
t = type (a) # class <int>
print(t) # This will print <class 'int'> because a is an integer

a = 30.5
t = type (a) # class <float>
print(t) # This will print <class 'float'> because a is a float

a = "Sarvesh"
t = type (a) # class <str>
print(t) # This will print <class 'str'> because a is a string

a = True
t = type (a) # class <bool>
print(t) # This will print <class 'bool'> because a is a boolean

a = [1, 2, 3]
t = type (a) # class <list>
print(t) # This will print <class 'list'> because a is a list

a = (1, 2, 3)
t = type (a) # class <tuple>
print(t) # This will print <class 'tuple'> because a is a tuple

a = {1, 2, 3}
t = type (a) # class <set>
print(t) # This will print <class 'set'> because a is a set

a = {'name': 'Sarvesh', 'age': 20}
t = type (a) # class <dict>
print(t) # This will print <class 'dict'> because a is a dictionary

a = None
t = type (a) # class <NoneType> 
print(t) # This will print <class 'NoneType'> because a is None
# This is a simple script to demonstrate the use of variables and arithmetic operations in Python

# Using type() to check the type of variables

a = "31.2"
b = float(a) # Convert string to float
print(b) # This will print 31.2 as a float

