# OOPS
# Object oriented programming


# class == blueprint
# 2 component ==> atributes ==> method
# if any one want to use / access the attribute ==> we need to create object of that class/ reference of that class
# I can protec my variables??
# public your obejct can access it ( inside the class and outside)?? 
# protected(only object can access that variable) or private ( you cant access outside the class)

# Langchain and Langgraph : use to build our GenAI applicsation 
# import many classes 
# obiect
# access those method

# GenAI application 
# convesationl bot
# memory
# q --> llm --answer : this need to be capture message[m1]
# q+ hostory ==> llm 
# Langchain
# InMemoryChatHistory()

class Customer:
    bank = 'BFL Bank'
    def __init__(self,name,score,age,amount): # constructor ?? it 
        self.name = name
        self.__score = score
        self.age   = age
        self.amount = amount

    
    def deposit(self,deposit_amount):
        self.amount = self.amount + deposit_amount

    def display(self):
        print(f'{self.name} | Score: {self.__score} | Balance: {self.amount}')

    
        

    
    
# cust_1 = Customer('rahul',500,34,1000)
# cust_1.display()
# cust_1.deposit(500)
# cust_1.display()

# cust_2 = Customer('chris',500,34,1000)
# cust_2.deposit(800)
# cust_2.display()


class Loan:
    def __init__(self, loan_id, principal, tenure_months):
        self.loan_id        = loan_id
        self.principal      = principal
        self.tenure_months  = tenure_months
        self.is_active      = True

    def basic_info(self):
        print(f'Loan ID  : {self.loan_id}')
        print(f'Principal: Rs {self.principal:,}')
        print(f'Tenure   : {self.tenure_months} months')

    def close_loan(self):
        self.is_active = False
        print(f'Loan {self.loan_id} closed.')


# cust= Loan('BFL123',1000,12)
# cust.basic_info()


class PersonalLoan(Loan):
    INTEREST_RATE = 0.14
    def __init__(self, loan_id, principal, tenure_months):
        super().__init__(loan_id, principal, tenure_months)

    def monthly_emi(self):
        r = self.INTEREST_RATE / 12
        n = self.tenure_months
        emi = self.principal * r * (1+r)**n / ((1+r)**n - 1)
        return round(emi, 2)

cust = PersonalLoan('BFL123',1000,12)
print(cust.close_loan())