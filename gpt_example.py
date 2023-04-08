import os
import openai
import csv
from dotenv import load_dotenv 

load_dotenv()



openai.api_key  = os.getenv('API_KEY')


# Must be a string
prompt = 'Who is the current president?'


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a news anchor"},
            {"role": "user", "content": prompt},
        ],
    max_tokens=400
)

gpt_output = response['choices'][0]['message']['content']

print(gpt_output)