from PyPDF2 import PdfFileReader
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfFileReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

def translate_text(text, target_language='hi'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def create_pdf(translated_text, output_path):
   
    pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Arial", 12)
    width, height = letter
    y_position = height - 50  

    line_spacing = 14  

    for line in translated_text.splitlines():
        if y_position <= 50:  
            c.showPage()
            c.setFont("Arial", 12)
            y_position = height - 50

        c.drawString(50, y_position, line)
        y_position -= line_spacing

    c.save()

def translate_pdf(input_pdf, output_pdf):
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(input_pdf)

    print("Translating text to Hindi...")
    translated_text = translate_text(text)

    print("Creating translated PDF...")
    create_pdf(translated_text, output_pdf)
    print(f"Translated PDF saved as {output_pdf}")

if __name__ == "__main__":
    input_pdf_path = r"C:\Users\Arnav\OneDrive\Desktop\pdf_translator\vacancies job matching.pdf"

    output_pdf_path = "translated3_sample.pdf"

    translate_pdf(input_pdf_path, output_pdf_path)
