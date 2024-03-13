from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

resposta = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Liste apenas os nomes dos produtos, sem considerar a descrição"
        },
        {
            "role": "user",
            "content": "Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-3.5-turbo",
)

print(resposta.choices[0].message.content)