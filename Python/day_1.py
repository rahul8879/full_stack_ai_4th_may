# objective ??
# 10?
# 10 --> 3-4 # Prem
# Chris --> 2-3
# Sasi  --> 4-5/10 ( Python )
# pavan - ??

# 1 Variable 
age = True
 # int

#print(type(age))

# x= 15
# y='Rahul'
# print(x+y)

# type casting ??
# case 1 : 
# x = 15
# y = int("30")
# print(type(y))
# print(x+y)

# case 2 :
# x = 15
# y = int("30A")

# rule about variable declartion ??
# 1. name ?? why -->   there are lots of reserved keywords in python --> you cant use for your variable name
# how I will know what are the keywords ??

# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#   'break', 'class', 'continue', 'def', 'del', 'elif', 
#   'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 2. your variable name cant start with digit
age_1 = 23
# 1_age = 23

# 3. you cant use special char when you are declaring the variable names
# age*_test = 23


# input from user ??
# age = int(input("Enter your age : ")) # type casting 
# print(age)
# print('type of age is',type(age))
# condition ??
# if True --> what do --- false --> 
# if age>18:
#     message = "Hello"
#     print(message+", you are eligible for the vote")
# else:
#     message ="Sorry! "
#     print(message + "You are not eligible")




ssn_number = "313123123ABC"
age = int(input('Enter your age'))

# check the len --><12 --> reject--accept

if len(ssn_number)!=12:
    print(' Check your ssn number')
elif age<18:
    print('You are not elibile')

else:
    print('Everything is ok')

# variable/data structure  --> List, tuples, sets, dict
# 