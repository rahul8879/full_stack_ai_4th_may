
blocked_word= ['destroy','bad_word','suscide','hack','money'] 
def validation(prompt):
    flag = False
    for word in prompt.lower().split():
        if word in blocked_word:
            flag = True
            return flag
        
    return flag

def call_llm(prompt):
    return " Happy to help you "