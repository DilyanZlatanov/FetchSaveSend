from fpdf import FPDF
from fetch_data import fetch_data


# This function converts 'content' to PDF file
def convert_to_pdf(content, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, content)
    pdf.output(output_pdf)

    return output_pdf
