from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-4o-mini', # 사용할 LLM 모델명
    temperature=0.1, # 무작위성 - 0에 가까울수록 일관된 답변, 1에 가까울수록 창의적
    messages=[
        {'role':'system', 'content':'너는 유치원생이야. 유치원생처럼 답변해 줘.'},
        {'role':'user', 'content':'참새'},
        {'role':'assistant', 'content':'짹짹'},
        {'role':'user', 'content':'오리'},
        {'role':'assistant', 'content':'꽥괙'},
        {'role':'user', 'content':'닭'},
        {'role':'assistant', 'content':'꼬끼오'},
        {'role':'user', 'content':'개구리'}
    ]
)

# print(response)
print(response.choices[0].message.content)