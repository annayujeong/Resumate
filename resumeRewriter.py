import openai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import constants

load_dotenv()

openai.api_key = os.getenv('API_KEY')

# def convert_pdf_to_txt(file_path):
#     resume = ""
#     with open(file_path, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         pages = pdf_reader.pages
#         for page in pages:
#             resume += page.extract_text()
#     return resume

# resume = convert_pdf_to_txt("Resume.pdf")

# resume_prompt = f'''This is my resume: {resume}. Can you rewrite it to make it more professional and better
# highlight my skills and experience?'''

# rewrittenResume = None

def rewriteResume():

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt= constants.RESUME_PROMPT,
  temperature=0.9,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
  )

  print(response)
  print(response["choices"][0]["text"])

  # rewrittenResume = response["choices"][0]["text"]

  # print("--------------------------------------------------")
  # print(rewrittenResume)
  return response["choices"][0]["text"]

def highlightDifferences():

  new_line = "\n"

  rewrittenResume = rewriteResume()

  print("?????????????????????????????????????????????????")
  print(constants.RESUME)

  print("?????????????????????????????????????????????????")
  print(rewrittenResume)

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt= f'''List the different words that were changed between these two strings: {new_line}"{constants.RESUME}" {new_line}"{rewrittenResume}"''',
  temperature=0.9,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
  )

  print("*********************************************************")
  print(response)
  return response

