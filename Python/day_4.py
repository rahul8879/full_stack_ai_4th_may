# tuple
# message = ('m1','m2','m3','m4','m5','m6')
# message[0]='m7'

# point = 10,20
# single = 42,
# print(type(point))


# person = ('Rahul', 28, 'Mumbai')
# name, age, city = person

# print(name, age, city)



student = {
    'name'   : 'John',
    'age'    : 22,
    'marks'  : [85, 90, 78],
    'active' : True,
}


# keys(), values(), items()
# print(student.items()) # both -- key as well as value 


d = {'name': 'Arjun', 'city': 'Mumbai'}
# print(d.get('address'))

# # how you can create new key 
# d['address'] = 'Somewhere'
# print(d)

# # how you can delete some keys
# # we have one keyword in python which helps you to delete the key
# del d['name']
# print(d)

# # if you want to clear your dict
# d.clear()
# print(d)


# iterate ( for loop)

user = {'name': 'Rahul', 'lang': 'Python', 'exp': 7,'address':'something'}
# for key in user:
#     print(key) # by default you are just printing the key, not values 

# for val in user.values():
#     print(val)

# for key, value in user.items():
#     print(key,value)



# Lets try to solve one interview questions ??

students = {
    'Amit'   : {'scores': [85, 92, 78, 90], 'grade': None},
    'Priya'  : {'scores': [95, 88, 97, 93], 'grade': None},
    'Rahul'  : {'scores': [60, 72, 55, 68], 'grade': None},
    'Sneha'  : {'scores': [45, 50, 48, 52], 'grade': None},
}

# print(sum(students['Priya']['scores'])/len(students['Priya']['scores']))


# python functions
def assign_grade(avg):
    if avg >= 90: return 'A+'
    elif avg >= 80: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 60: return 'C'
    else: return 'F'

# task is :
# Find the avg marks for each students ??
for name, data in students.items():
    avg = sum(data['scores'])/len(data['scores'])
    data['avg'] = avg
    data['grade'] = assign_grade(avg)

print(students)


# Day 1 - till today - try to execute ==> then you wil be in
#  better to position to understand future topics
# stopping the session ---> utilize this time to revise this one


# avg marks ==> You need to assign the grade ??

# print(sum(students['Sneha']['scores'])/len(students['Sneha']['scores']))
