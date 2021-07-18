import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'your_name'
email['to'] = 'person_email@gmail.com'
email['subject'] = 'your_subject'

email.set_content(html.substitute(name = 'person_name'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@gmail.com', 'your_password')
    smtp.send_message(email)
    print('all good!')