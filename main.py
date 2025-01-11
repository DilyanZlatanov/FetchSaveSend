from convert_to_pdf import convert_to_pdf
from fetch_data import fetch_data
from send_to_email import send_to_email

# Execute the main logic
pdf_to_send = None

# Prepare PDF file for sending
try:
    pdf_to_send = convert_to_pdf(fetch_data(), "result_data.pdf")
except Exception as e:
    print(f"Error occurs while creating PDF {e}")

# Send the email with attached PDF file
if pdf_to_send:
    send_to_email(pdf_to_send)
