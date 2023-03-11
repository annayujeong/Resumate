from PyPDF2 import PdfReader

def convert_pdf_to_txt(file_path):
    resume = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        pages = pdf_reader.pages
        for page in pages:
            resume += page.extract_text()
    return resume

RESUME = convert_pdf_to_txt("Resume.pdf")

RESUME_PROMPT = f'''This is my resume: {RESUME}. Can you rewrite it to make it more professional and better
highlight my skills and experience, and in bullet points, can you list the differences between the original 
resume and the revised resume?'''

