import ast
import openai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import constants
import json

def request(input):
    load_dotenv()
    openai.api_key = os.getenv("CHATGPT_API_KEY")
    model_engine = "text-davinci-003"

    # to_dict = ast.literal_eval(input.decode('utf-8'))
    resume = input['resume']
    job_description = input['job_description']
    prompt = f"This is my resume: {resume}, and this is the description of a job I'm interested in:{job_description}. What are some courses and their URLs, in format of course name&&&course url, separated by***, that I could take to be better suited for the job?"

    completion = openai.Completion.create (
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        # stop=None,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return completion

def response(input):
    data = request(input)
    data = data.choices[0].text
    courses = data.split("***")
    course_dictionary = {}

    for course in courses:
        course = course.split("&&&")
        course_dictionary[course[0]] = course[1]

    return course_dictionary
