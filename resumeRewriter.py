import openai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import constants

load_dotenv()

openai.api_key = os.getenv('API_KEY')

def rewriteResume(data):
  resume_prompt = f'''This is my resume: {data}. Can you rewrite it to make it more professional and better
  highlight my skills and experience?'''

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt = resume_prompt,
    temperature=0.9,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )

  return response["choices"][0]["text"]
