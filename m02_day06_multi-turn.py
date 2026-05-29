from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

while True:
    user_input = input('사용자 : ')

    if user_input == 'exit':
        break
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        temperature=0.1, # 무작위성 - 0에 가까울수록 일관된 답변, 1에 가까울수록 창의적
        messages=[
            {'role':'system', 'content':'너는 사용자를 도와주는 상담사야.'},
            {'role':'user', 'content':user_input}
        ]
    )
    print(f'AI : {response.choices[0].message.content}')