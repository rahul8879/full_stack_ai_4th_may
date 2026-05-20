
# # name_1 = 'rahul'
# # age_1 = 29
# # income_1 = 1000

# # name_2 = 'Chris'
# # age_2 = 29
# # income_2 = 1200

# # name_3 = 'ABC'
# # age_3 = 29
# # income_3 = 1000



# # def hike(hike_pct,income):
# #     final_income = income*hike_pct+income
# #     return final_income
# # # task is give hike to ABC by 10%
# # updated_income_chris = hike(0.10,income_2)
# # print('updated income of Chris',updated_income_chris)



# # define my template/class
# # public variable : any one can use it --> just create the objects
# # use that objects to get any attribute acces or method
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age  = age
#         self.__salary = salary # private attributes
#         self.__updated_salary = None
    
#     def hike_salary(self,hike_pct):
#         self.__updated_salary = self.__salary*hike_pct + self.__salary
#         return self.__updated_salary
#     def display_info(self):
#         print("salary is :")


# obj_1 = Employee('rahul',29,1500)
# obj_1.hike_salary(0.10)
# print(obj_1.hike_salary(0.10))

# obj_2 = Employee('chris',30,27854)
# print(obj_2.hike_salary(0.10))

# # if I want to see the salary of obj_1 ??
# print(obj_1.updated_salary)



#
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
client = OpenAI()


class LLMModel:
    def __init__(self,provider,model_name,max_tokens):
        self.provider = provider
        self.model_name = model_name
        self.max_token = max_tokens
        self.__system_prompt = None

    def generate(self,prompt):
        response = client.chat.completions.create(
            model=self.model_name,
            max_tokens=self.max_token,
            messages=[{'role':'user','content':prompt}]
        )
        return response.choices[0].message.content


email = "Can you help me to build download functinlaities"
prompt  = f"""
Classify the below email into one of the category : 
Billing, Feature request ,Technical, Other.
make sure output should not have any kind of explanation, only category
Here is the email body details
{email}
"""



gpt_4 = LLMModel('OpenAI','gpt-4o',1200)
gpt_4_mini = LLMModel('OpenAI','gpt-4o-mini',1200)
output_gpt_4 = gpt_4.generate(prompt)
output_gpt_4_mini = gpt_4_mini.generate(prompt)

print(output_gpt_4)
print(output_gpt_4_mini)
# agentic AI solutions 

#you want to compare different model output


# inheritance 

class Parents:
    def test(self):
        return 'I am from parents'
    
class Child(Parents):
    def __init__(self,name):
        self.name = name
    def get_discount(self):
        return 0.2

obj_1 = Child('rahul')
print(obj_1.get_discount())