
# Basic Functions in Python
# Introduction to Functions
# Functions are independent blocks of instructions that perform specific tasks.
# Functions in Python are categorized into two types:
#   1. Built-in Functions (e.g., len(), print())
#   2. User-defined Functions

# Syntax of a Function:

# def function_name(parameters):
#     function_statements

# Printing the Address of a Function:
# function_name

# Calling a Function:
# function_name()

# Classification of User-defined Functions:
# User-defined functions are classified into 4 types:
#   1. Function without Arguments and without Return Value
#   2. Function with Arguments and without Return Value
#   3. Function without Arguments and with Return Value
#   4. Function with Arguments and with Return Value

# Below are examples of each type of user-defined function.

# 1. Function without Arguments and without Return Value
def greet():
    '''This function prints a greeting message.'''
    print("Hello, welcome to the Python functions tutorial!")
greet() # Calls the greeting function

# 2. Function with Arguments and without Return Value
def add_numbers(a, b):
    '''This function adds two numbers and prints the result.'''
    result = a + b
    print("The sum is:", result)
add_numbers(10,20) # Calls add_numbers with arguments

#arguments are 5 type
#a).mandatory or positional argumengt:
def add(a,b,/):
    c=a+b
    print(c)
add(10,20)

#b).keyword arguments:
def add(*,a,b):
    c=a+b
    print(c)
add(a=23,b=24)

#c).default arguments:
def add(a=25,b=24):
    c=a+b
    print(c)
add()

#d).variable length arguments:
def add(*args):
    print(args)
    print(type(args))
    summ=0
    for j in args:
        summ+=j
    print(summ)
add(100,200)

#e).variable length Keyword arguments:
def add(**kwargs):
    print(kwargs)
    print(type(kwargs))
    summ=0
    for i in kwargs:
        summ+=kwargs[i]
    print(summ)
add(a=10,b=20,c=30)

#order of defining the argument of a function
#positional --> default -->  variable length -->  variable length Keyword
def function(a,b=90,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
function(78,56,999,12,22,67,name='killy',age=10)

# 3. Function without Arguments and with Return Value
def get_five():
    '''This function returns the integer 5.'''
    return 5
print(get_five()) # Calls get_five and prints the result
#return statement(we shall call a return functions by 3 ways):
#i.inside print function
def function():
    a=10
    b=30
    return a+b
c=function()
print(c)
#ii.inside a variable:
def function():
    a=10
    b=30
    return a+b
print(function())
#iii.inside a condition:
def lifecyle(age):
    if age in range(0,13):
        return 'child'
    elif age in range(13,20):
        return 'teenage'
    elif age in range(20,50):
        return 'adult'
    else:
        return 'child'
print(lifecyle(10))

# 4. Function with Arguments and with Return Value
def multiply_numbers(a, b):
    '''This function multiplies two numbers and returns the result.'''
    return a * b
print(multiply_numbers(10,20)) # Calls multiply_numbers and prints result



