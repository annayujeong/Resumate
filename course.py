import openai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import constants

load_dotenv()

openai.api_key = os.getenv('API_KEY')

load_dotenv()
openai.api_key = os.getenv("CHATGPT_API_KEY")

model_engine = "text-davinci-003"

# TODO: extract to main file
# def convert_pdf_to_txt(file_path):
#     resume = ""
#     with open(file_path, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         pages = pdf_reader.pages
#         for page in pages:
#             resume += page.extract_text()
#     return resume

job_description='''About the job
Building the life you want starts with acquiring skills that are in demand.
As a certified tradesperson, career potential is unlimited.
It all starts with apprenticeship; a unique opportunity to earn and learn while building your career.

About the Opportunity

British Columbia has an increasing demand for skilled tradespeople, resulting in rewarding employment opportunities. As a first-year apprentice, you will be starting a career path towards obtaining your SkilledTradesBC trade certification. This is a great opportunity to get hands-on training while receiving a competitive wage for your work!


Gasfitters in BC are classified as either class A or class B. Class A gasfitters are permitted to work on any size of gas system. Whereas class B gasfitters have limitations on the energy input of equipment they work on. Therefore, gasfitter – class B is a pre-requisite to gasfitter – class A certification. Apprenticeship training for the gasfitters is administered through the Industry Training Authority BC (ITA BC) and Technical Safety BC regulates and certifies the trade.


A typical day as a gasfitter – class B could include installing, testing, adjusting, maintaining and repairing equipment such as boilers, burners, make-up air units, and furnaces. Class B gasfitters work with various gas fuels including natural gas, manufactured gas, liquified petroleum gas, landfill gas or biogas. Gasfitting is closely related to other piping trades including plumbing, sprinkler fitting, and pipe fitting.


Day-to-day as an apprentice you could be:

Installing, inspecting, and repairing gas lines and gas equipment
Advising clients on safety features and maintenance of gas units
Converting cars and appliances to use natural gas fuels
Using hand and power tools (wire strippers, pliers, sheet metal snips, channel locks, wrenches, power drills, side cutters, tape measures, hammers, levels, etc)
Reading and interpreting blueprints
Working from ladders and scaffolding
Sorting materials and maintaining a clean worksite

About You


BCCA Apprenticeship Services is looking for applicants interested in pursuing a career in construction as a first-year apprentice gasfitter - class B. The ideal candidate should be interested in starting a career path towards certification as gasfitter - class B and should be motivated to learn, reliable, and hardworking.


To succeed as a first-year apprentice gasfitter - class B, you:

Communicate, work well with others, and follow directions well
Have good dexterity and like to work with your hands
Enjoy working indoors or outdoors in all seasons
Like to solve problems and build solutions
Are physically fit with stamina for manual labour
Have experience using hand and power tools
Are willing to follow safety guidelines at all times
Understand basic math
Have strong attention to detail
Are in good physical condition with good endurance

Other qualifications can include (but are not required):

Hands-on experience in working with piping materials, tools and/or mechanical systems
Background in another trade such as plumbing, sprinkler fitting, or pipefitting
Occupational First Aid training or SiteReadyBC certification
High school diploma and/or completion of the Level 1 Gasfitter – Class B Training from a SkilledTradesBC recognized post-secondary institution
Valid BC driver’s license and reliable vehicle
Prior experience in construction (hobbies, summer jobs, or volunteer activities), agriculture or forestry, manufacturing, marine services or fisheries, municipal work, or other non-construction trades are a bonus

The Benefits of Apprenticeship


An apprenticeship offers a pathway to a successful career in construction. You will earn an income while gaining work-based training hours, education, and certification. Apprentices are eligible for government grants, tax credits, and employment insurance while attending training. This can help you offset the cost of training and certification and allow you to complete your apprenticeship and minimise student debt.


The starting hourly rate for first-year apprentices is usually between $17-$22/hour. It is determined by each employer and can vary depending on skills, location, and your experience. As a first-year apprentice new to a trade it is customary to begin at the bottom of the pay range but as you ‘earn and learn’ on the job, your pay will increase as you progress in your apprenticeship.


If this sounds like you, and you want to start your career in construction, we encourage you to apply today!'''

#resume = convert_pdf_to_txt("Resume.pdf")

prompt = f"This is my resume: {constants.RESUME}, and this is the description of a job I'm interested in:{job_description}. What are some courses and their URLs, in format of course name&&&course url, separated by***, that I could take to be better suited for the job?"
def request():
    completion = openai.Completion.create (
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return completion

def response():
    data = request()
    data = data.choices[0].text
    courses = data.split("***")
    course_dictionary = {}

    for course in courses:
        course = course.split("&&&")
        course_dictionary[course[0]] = course[1]

    return course_dictionary
