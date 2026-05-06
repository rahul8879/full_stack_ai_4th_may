# 1. fundamental ?? rules how to declare ?? data --> variables (int, float, string boolean)
# rules -- java - c--> int a = 12 --> python ??
# if else --> for loop --> while loop, functions --class and objects ??\
# DS --> LIST, TUPLES, DICT, SETS etc : operations ??  slow ??
# sales_producta= compare them ?? 1-2 mint ( lot of times)
# 2. to understand
# 2.1 PANDAS : data manipulation -- LLM applications 
# csv/excel/json/text/db PANDAS --> load data ---clean data -->pass to your AI  
# 2.2 NUMPY ( modern AI framwork - TENSORFLOW , PYTORCH)
# MATH -- implemations --> fundamental -- libries ( usecase )

# age =  23.2
# print(type(age))


# int
# float
# bool
# string
# list 


# 3 students  : I want to store the marks
# s1 = 45
# s2=46
# s3 =47
# s4 = 67
# students = [45,46,47,67]
# print(type(students))

# total_marks = sum(students)
# print(total_marks)

# age = int(input("Enter your age"))

# if age>18:
#     print(' you are eligible')
# else:
#     print('Not eligble')

# nested if else 
# if age>18:
#     print('something')
#     if age>24:
#         print('something')
#     elif age >78
# elif age<18:
#     print('soemthing')
# else:
#     print('not working')
# for loop --. while loop

marks = [56,76,78,89,34,56,78]
# find the avg marks ?? assume I dont know about len, sum
# for loop
# total_marks = 0
# for i in marks:
#     total_marks = total_marks + i

# avg_marks = round(total_marks/len(marks),2)
# print('avg marks',avg_marks)

data = [2,3,2,4,5,6,7,2]
# task ?? count how many times 2 occured ( without using any inbuilt method )
key = 2
count = 0
for i in data:
    if i==key:
        count = count+1
print('count:',count)


# search certain key from the iterable object ( list )

# data = [2,3,4,-1,3,1]
# output --> where is -1 available --> index number
# key = -1
# for i in range(len(data)):
#     if key == data[i]:
#         print('it found')
#         break
#     print('I am at : ',data[i])


# 
sales_data = [[34,45,56,76,67],[48,45,49,76,67],[90,91,67,76,89]]

# output --> A: avg_sales , B: avg sales, C = avg_sales
final_output = []
for i in sales_data:
    total_sales = 0
    for j in i:
        total_sales=total_sales+j
    avg_sales = total_sales/len(i)
    final_output.append(avg_sales)
print('final sales :', final_output)

# tuple ??
# access from list
# via index 
# you do the sames
# result = (2,3,2,4,5,6,7,2)
# result[0] = 34
# print(result[0])


# while loop --
# first condition --> logic 

# rules associated with your variables 

# and = 23

from math_module import avg_sales
# 2 stages -- define -- call 
avg_sales(sales_data)

# function arguments ??
# default par
# keyword arguments
# Arbitary arguments 


# print(2,23,24)
# def greet(*names):
#     print(names)

# # greet(name="rahul",msg="Go n Study")
# greet("rahul","testing",2)


# Lambda Function / Anonymous functions
# when to use -->dont have any name --> 1 liner function 

lst = [1, 2, 3, 4, 5]

# filter even number ??
# filter(fucntion(which will have logic to find out even number), lst)

# def even(x):
#     return x%2==0

# output = []
# for i in lst:
#     result = even(i)
#     if result:
#         output.append(result)

# print('even value is ',output)


# print(list(filter(lambda x: (x%2==0),lst)))



# files -->


f = open('/Users/rahultiwari/Documents/02_Freelancing/Hachion_batch/full_stack_ai_4th_may/Python/example.txt')
print(f.read())

