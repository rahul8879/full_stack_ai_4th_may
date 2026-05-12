# String : impoortant
# 1 way to create string
# name = "XYZ Finance"
# print(type(name))
# # sliding windows or I can access specific char
# # print(name[0])
# # print(name[0:5])
# # 
# print('total char in name is: ',len(name))


# # eg.

# prompt  = """
# You are a helpful assistant
# for XYZ Finance customers.  
# Answer only finance questions.
# """
# # prompt[0:3] = 'They'
# # if you writing multiline of text==> triple
# print(type(prompt))
# print('total char in prompt is: ',len(prompt))

# # Note : # char != token ( dont think like this)
# # name[0] = 'A'



# # Strings are immutable - You cant change a char



# # slicing - extracting substrings : interview
# # text = "LOAN_APPROVED_2024"
# # print(text[14:])

# # method -- for string

# prompt  = """
# You are a helpful assistant
# for XYZ Finance customers.  
# Answer only finance questions.
# What is the capital of France
# """

# # flow
# # prompt--> validation ?? valid --> guardrail ??  --> llm -->output
# blocked_word = ['destroy','bad_word'] # In real scaanri --p[ython library (1000 words 

# print(prompt.split()) # it will seperate the given string based on blank space--> list of word


# should_call_llm = False
# for i in prompt.split():
#     if i.lower() in blocked_word:
#         print('this is blocked word',i)
#         should_call_llm= False
#         break
#     should_call_llm=True
# print('should I call llm or not ??',should_call_llm)
# if should_call_llm:
#     # call llm --in future ??

# test = "  hello ".strip()
# print(len(test))

# test = "hello"
# # count how many times l occured
# result = test.find("3")
# print(result)

# token= ['Hi','how','are','you']
# prompt = ','.join(token)
# print(prompt)

# python fucntions??

loan_word=['loan','money','amount']
emi = ['emi','tenure','emi_amount']



def intent_classification(user_message):
    intent = 'general message'
    word = user_message.lower().split()
    for i in word:
        if i in loan_word:
            intent = 'loan_enquiry'
            return intent
        elif i in emi:
             intent = 'emi_enquiry'
             return intent
    return intent

result =intent_classification("When is my EMI due?")
print(result)





def should_call_llm(prompt,blocked_word):
    flag = False
    word = prompt.lower().split()
    for i in word:
        if i in blocked_word:
            flag = False
            break
        flag = True

    # logic

    return flag



prompt  = """
You are a helpful assistant
for XYZ Finance customers.  
Answer only finance questions.
What is the capital of France
"""
blocked_word = ['destroy','bad_word']


llm_result = should_call_llm(prompt,blocked_word)
print('llm deision',llm_result)






# message1 = "How much loan can I get?"
# words1 = message1.lower().split()
# if "loan" in words1:
#     intent = "loan_enquiry"


# message2 = "When is my EMI due?"
# words2 = message2.lower().split()
# if "emi" in words2:
#     intent2 = "emi_inquiry"

# 100 user == 100 copy paste ( 1000 question)
# should_call_llm()