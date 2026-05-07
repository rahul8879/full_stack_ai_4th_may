# # List --> method --> solve interviews 
# # Tuple --> 

# message = ['m1','m2','m3','m4','m5']
# # access ?? list via index -->
# # print(message[0])
# print(message[0:3]) # ending index will be excluded
# print(message[3:])

# # skip certain message 
# print(message[0:4:2])

# # list compression ??
# number = [2,3,4,5,6]
# # approach
# # result = []
# # for i in number:
# #     result.append(i**2)
# # print(result)

# result = [i**2 for i in number]
# print(result)

# # even number between 0-20
# evens = [x for x in range(20) if x%2==0]
# print(evens)


# # method : documentations ??
# message.append('m6')
# print(message)

# # we want to add m7 at location 1
# message.insert(1,'m7')
# print(message)

# message_2 = ['m8','m9','m10']
# message.extend(message_2)
# print(message)


# # remove ?? m2, m3
# # message.remove('m100')
# # print(message)

# # pop() --> index 
# message.pop(0)
# print(message)


# # sort
# number = [78,89,21,-1]
# number.sort(reverse=False)
# print(number)



cart = []

def add_items(product,price):
    data = {'product':product,'price':price}
    cart.append(data)

# lets call the fucntions
add_items('apple',49)
add_items('banana',78)
add_items('TV',200)


# remove ??
# for i in cart:
#     print(i['product'])


# def remove_item(product):
#     new_cart = []
#     for i in cart:
#         if i['product'].lower() != product.lower():
#             new_cart.append(i)
#     return new_cart

# new_cart = remove_item('Banana')
# print(new_cart)


# def cart_total(new_cart):
#     total_amount = 0
#     for i in new_cart:
#         total_amount = total_amount + i['price']
#     return total_amount

# print(cart_total(new_cart))


# LEET CODE ??

# we need to write a function 
# input : arr/list,target two_sum([2,7,11,15],9)
# output : [0,1]



# tuples ??
# same to your list -
# data sci/ai 
# text --> vector --> points
# creation
point = (10,20)
rgb = (255,128,0)
single = (42,)
point = 10,20

# packaging and unpackaging
person = ('rahul',28,'Mumbai') # packing
name,age,city =person # unpacking
a,b = 5,10
a,b = b,a

# data = (12,12,13,14,-2)
# print(data.count(12))


cities = {
    'Mumbai'  : (19.0760, 72.8777),
    'Delhi'   : (28.6139, 77.2090),
    'Bangalore': (12.9716, 77.5946),
    'Hyderabad': (17.3850, 78.4867),
}

# function ( mumbai )
import math


def haversine_distance(loc1, loc2):
    """Distance between two (lat, lon) tuples in km"""
    lat1, lon1 = loc1
    lat2, lon2 = loc2
    R = 6371  # Earth radius km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

dist = haversine_distance(cities['Mumbai'],cities['Mumbai'])

print(dist)


# dict

# search --> store dict ( hash table)
student = {
    'name'   : 'Arjun',
    'age'    : 22,
    'marks'  : [85, 90, 78],
    'active' : True,
}

# student['parents_name'] = "TEST"
# print(student.items())
# print(student.get('name'))




employees = {
    'E001': {'name': 'Rahul', 'dept': 'ML', 'salary': 120000},
    'E002': {'name': 'Priya', 'dept': 'Backend', 'salary': 110000},
}

# read via key
# create/update
# employees['E001']['name'] = 'Testing'
# print(employees)

# del employees['E001']
# print(employees)


# iterare 
# user = {'name': 'Rahul', 'lang': 'Python', 'exp': 7}

# for key,value in user.items():
#     print(key,value)



students = {
    'Amit'   : {'scores': [85, 92, 78, 90], 'grade': None},
    'Priya'  : {'scores': [95, 88, 97, 93], 'grade': None},
    'Rahul'  : {'scores': [60, 72, 55, 68], 'grade': None},
    'Sneha'  : {'scores': [45, 50, 48, 52], 'grade': None},
}


# assign_grade(avg) --> return grade --avg>-90 grade A, more 80 B


# data = set([34,34,56,78])
# print(data)

data_1 = {34,56,78,1,79}
data_2 = {80,85,78,1,79}

# 10th
# intersection ??
result = data_1.intersection(data_2)
print(result)