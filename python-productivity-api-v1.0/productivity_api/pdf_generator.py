from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd

def generate_pdf(csv_path, pdf_path):
    df = pd.read_csv(csv_path)
    c = canvas.Canvas(pdf_path, pagesize=A4)
    text = c.beginText(40, 800)
    for index, row in df.iterrows():
        text.textLine(", ".join(str(x) for x in row))
    c.drawText(text)
    c.save()