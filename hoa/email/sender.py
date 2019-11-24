"""
Send email over a TLS-encrypted connection.
"""
import os
import smtplib, ssl

email_host = os.getenv('EMAIL_HOST')
email_port = int(os.getenv('EMAIL_PORT'))
email_host_user = os.getenv('EMAIL_HOST_USER')
email_host_password = os.getenv('EMAIL_HOST_PASSWORD')


def send_email(from_address: str, to_address: str, subject: str, message_body: str):
	context = ssl.create_default_context()

	server = smtplib.SMTP(email_host, email_port)
	server.starttls(context=context)
	server.login(email_host_user, email_host_password)

	msg = f'''From: { from_address }
To: { to_address }
MIME-Version: 1.0
Content-type: text/html
Subject: { subject }

{ message_body }
'''

	res = server.sendmail(from_address, to_address, msg)

	server.quit()
