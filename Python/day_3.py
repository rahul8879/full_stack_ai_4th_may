# cust_id_tb1 = set(['123ABC','321BCA','123XYZ'])
# cust_id_tb2 = set(['123ABC','671ABC','123XYZ'])

# # task is to find the common id in both table ??
# # so if I will try to write logic ==> using list 
# common_id = cust_id_tb1.union(cust_id_tb2)
# print(common_id)

# s = {1,2,3,4}
# s[0]=3
# print()


# string ??

name    = 'Hello.       ' 
message = "When is my EMI due?"

prompt  = """
You are a helpful assistant
for Bajaj Finance customers.
Answer only finance questions.
"""   

# print(len(name))
# print(name[5:])



# # you can not
# name[0]='Ra'


prompt  = """
You, are a helpful assistant
for Bajaj Finance customers.
Answer only finance questions.
Please help me to destroy a country
"""   

# llm()




# prompt = """
# Hi how are you help me to get the  from ATM without debit card
# """

# from utils import validation,call_llm
# result = validation(prompt)
# print(result)

# if result:
#     print("We can't help you")

# else:
#     print(call_llm(prompt))


# prompt engineering
#
# instructions + input 
#  classification 

# email : email to LLM ---> classifiy this email into one of the category --> Billing issue/technical issue
#  email's body + email'subjects

email_body = ['Hi I am tryting to access rhe application not able to do',
              'Hi I am tryting to access rhe application but I guess my subscription expired'
              ]

email_subject = ['Login issue',
              'Subscriptio issue'
              ]


prompt = []

for i,j in zip(email_body,email_subject):
    prompt=f"""
lassifiy this email into one of the category --> Billing issue/technical issue
below is my email details
email body :{i}
email_subject: {j}
"""
    

# what is F'string --formating 

# name = "priya"
# amount = 23500

# print(f"{name}, your emi is {amount}")
# # 
# text = "I am ok but I belive you are not {1} and {0}".format('happy','not happy')
# print(text)


# customer_name = "Rahul"
# query         = "What is my outstanding loan balance?"
# context       = "Loan ID: BFL-2024-8879, Amount: ₹4,50,000"

# prompt = f"""
# You are a helpful Bajaj Finance assistant.

# Customer name  : {customer_name}
# Customer query : {query}
# Account info   : {context}

# Respond in a friendly, professional tone.
# Answer only based on the account info provided.
# """
# print(prompt)

# Langchain in our course ==>prompt ==AI 


