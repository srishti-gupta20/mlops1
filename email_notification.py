import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "**********.com"		#sender's email
receiver_email = "*****@gmail.com"	#receiver's email
password = "*********"			#sender's password    

message = MIMEMultipart("alternative")
message["Subject"] = "Your CNN Model"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
Your model has been created with more than 98% accuracy"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       Your model has been created with more than 98% accuracy<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )