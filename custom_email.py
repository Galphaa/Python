import smtplib

host = "smtp.gmail.com"
port = 587
username = "keratishvili95@gmail.com"
password = "eax1300pro"
from_email = username
to_list= ["gkeratishvili@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "hello from georgy")
email_conn.quit()


from smtplib import SMTP


ABC = SMTP(host, port)
ABC_conn.ehlo()
ABC_conn.starttls()
ABC_conn.login(username, password)
ABC_conn.sendmail(from_email, to_list, "hello from georgy")
ABC_conn.quit()


from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
        pass_wrong.login(username, "wrong password")
        pass_wrong.sendmail(from_email, to_list, "hello from georgy")
except SMTPAuthenticationError:
        print("could not login") 
except:
        print("an error occured")
pass_wrong.quit()

