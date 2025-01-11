from email.message import EmailMessage
import smtplib


def send_to_email(attachment):

    # Set SMTP configuration
    smtp_sender = "smtp.abv.bg"
    smtp_port = 465
    sender_email_address = "fanrihanna@abv.bg"
    sender_email_password = "faWrup-0tifbo-revvaz"

    # Create email message
    msg = EmailMessage()
    msg["From"] = sender_email_address
    msg["To"] = "dilqn.dev@gmail.com"
    msg["Subject"] = "Test email"
    msg.set_content("This email is sent via Python")

    # Attach file to email
    with open(attachment, "rb") as file:
        file_data = file.read()
        file_name = attachment.split("/")[-1]  # Extract file name from the path
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    # Send the email
    try:
        # Connect to the SMTP server and send message
        with smtplib.SMTP_SSL(smtp_sender, smtp_port) as smtp:
            smtp.login(sender_email_address, sender_email_password)
            smtp.send_message(msg)
            print("Email send successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
