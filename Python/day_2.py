# variable continuation ??
# int
# float
# string
# bool
# list
# tuple ?? solving the same problem ?

# s1 = 45
# s2= 67
# s3=65
# s4=78
# s5= 79
# s6= 78
# s7=99

# # avg marks
# avg_marks = (s1+s2+s3+s4+s5+s6+s7)/7
# print('the avg value is: ',avg_marks)

# after 10 days --> 2 more students join ??

# list
marks = [45,46,74,54,78,89]
# print('before appending the value: ', marks)
# add more number/ marks
# here marks is list type --> method/operation
# you can add valu in the list
# marks.append(67)
# print('before appending the value: ', marks)
# print(marks[-3])

# iterable objects -->list ( variable which can holdvalue more then 1 )

# print(sum(marks)) # here len, sum : inbuilt method/functions

# # to find out the avg marks
# avg_marks = round(sum(marks)/len(marks),1)
# print('avg marks is: ',avg_marks)

# round===> round(64.33333333333333,2). # 64.33
# print(round(64.33333333333333,2))

# print(marks[0])

# data = ['rahul',23,'65',[12,32]]
# print(type(data[3]))


# 

# passed_exam = ['123ABC',"KBC673","675BCA"]

# print('candidate who qualified the exam',passed_exam)

# rahul_roll= '91333ABC'
# passed_exam[0] = rahul_roll

# print('candidate who qualified the exam',passed_exam)


# but if you store your data into tuple data structure ??


# passed_exam_tu = ('123ABC',"KBC673","675BCA")
# # access any value ??
# print(passed_exam_tu[0])

# # but if you try to change any value ??
# passed_exam_tu[0] =rahul_roll
# print('candidate who qualified the exam',passed_exam)


# # daily sales data
# sales_data = (100,150,167,189,186,287)
# print('correct total sales ',sum(sales_data))

# print('max sales ??')
# print('max sales ',max(sales_data))
# # sales_data[0] = 0 # modified in between --> bcz of this its not correct output
# print('total sales ',sum(sales_data))

# print('min sales ??')
# print('min sales ',min(sales_data))



# assume that we dont know about sum()
marks = [45,46,74,54,78,89,101]

# find the avg marks ??
# total_marks = (marks[0] + marks[1] + marks[2]+ marks[3]+ marks[4] + marks[5]+marks[6])
# print('total marks: ',total_marks)


# what is the for loop
# example 1 : 
# marks = [45,46,74,54,78,89,101,1000]
# total_marks = 0 
# for i in marks:
#     total_marks = total_marks + i

# print('total marks is : ',total_marks)

# Example 2 :
# task : find how many 2 occurred ???

count = 0
data = [2,3,2,4,2,1]
for i in data:
    if i ==2:
        count = count +1
print('count of 2 is : ',count)

# 90
# 1.15mint 5-10mint
