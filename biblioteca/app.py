import smtplib
from email.message import EmailMessage

def send_email(message_text, recipient_email):

    EMAIL = 'leospinosa2607@gmail.cpom'
    PASSWORD = 'aqtsvyllalenayvf'
    
    msg = EmailMessage()

    msg['Subject'] = "Empréstimo de Livro"
    msg['From'] = EMAIL
    msg['To'] = recipient_email

    msg.set_content(message_text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)        