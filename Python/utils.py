
blocked_word= ['destroy','bad_word','suscide','hack','money'] 
def validation(prompt):
    flag = False
    for word in prompt.lower().split():
        if word in blocked_word:
            flag = True
            return flag
        
    return flag


from dotenv import load_dotenv
print(load_dotenv())

from openai import OpenAI

client = OpenAI()

# string ??

def call_llm(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

