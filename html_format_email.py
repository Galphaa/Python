from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import smtplib


host = "smtp.gmail.com"
port = 587
username = "keratishvili95@gmail.com" 
password = "eax1300pro"
from_email = username
to_list= ["gkeratishvili@gmail.com"]

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello"
    the_msg['From'] = from_email
    #the_msg['To'] = to_list
    plain_txt = 'testig message'
    html_txt = """\
    <html>
       <head></head>
       <body>
         <p>Hey!<br>
           Testing this eamil <b>Message</b>. Made by <a href='https://www.joincfe.com'>Galpha team</a>
         </p>
       </body>
    </html>
    """
    part_1 = MIMEText(plain_txt, "plain")
    part_2 = MIMEText(html_txt, "html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("erro senfing massage")

