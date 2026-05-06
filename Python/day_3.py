# # Data structure --> for loop ---> while loop

# # 1 List

# fruits = ['apples','banana','mango']

# # access any elements of your list via index number
# # print(fruits[1])

# # slicing concept : in future -- memory concept for LLM --> its very very imp
# message = ['m1','m2','m3','m4','m5','m6']
# print(message)
# print(message[3:]) # bottom 3
# print(message[:3])
# print(message[::3])


# # if len(message)>3:


# # method : documentation ---> list

# # append
# # message.append('m7')
# # print(message)
# # message.insert(1,'m9')
# # print(message)

# # application 2 : 
# # message_2 = ['m10','m11','m12']
# # message.extend(message_2)
# # print(message)


# # remove ??

# message.remove('m1') # takes elements as a input
# print(message)

# message.pop(1) # index as input
# print(message)

# # sometime -- they will ask us to sort the data
# marks = [23,24,26,-1]
# # marks.sort(reverse=False)
# # print(marks)
# print('before reverse: ',marks)
# marks.reverse()
# print(marks)


# shoping Cart. # interview questions ?? new concept ??
cart = [] # add as json --> {'product':ABC,'price':12}

cart.append({'product':'Banana','price':12})
cart.append({'product':'Apple','price':24})
cart.append({'product':'TV','price':100})
print(cart)


# remove certain product ??
remove_product = 'banana'

new_cart = []
# print(cart[0]['product'])

# total price ??

for i in cart:
    if i['product'].lower()!=remove_product.lower():
        new_cart.append(i)
print('after removing the banana from list:',new_cart)

total_price = 0
for price in new_cart:
    total_price = total_price+price['price']
print('total price is : ',total_price)



# Leet code : list : -- for loop
# interview ?? 
# 
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# as a output I need a pair of number whose sum will be 9
# output ---> (6,3),(5,4)





# 
# name_1 ='raHul'.lower()
# name_2 ='Rahul'.lower()

# print(name_1==name_2)



# ask --> total price ??12+ 24+36==> code <==

# function --> reuse --> without repeating something 
# cart = []
# def add_item(cart,product,price):
#     cart.append({'product':product,'price':price})
#     return cart

# result = add_item(cart,'banana',54)
# print('result :',result)







       # user defined method

# print(cart)

type(24)