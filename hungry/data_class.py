import csv
import shutil
import datetime
import os
from tempfile import NamedTemporaryFile
from utils.templates import get_template, render_context
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError

host = 'smtp.gmail.com'
port = 587
username = 'imshubhamsingh007@gmail.com'
password = ''
from_list = 'imshubhamsingh007@gmail.com'

file_path = os.path.join(os.path.dirname(__file__), "data.csv")


class UserManager:
    def render_message(self, user_data):
        file_ = 'templates/email_message.txt'
        if isinstance(user_data, dict):
            context = user_data
            template = get_template(file_)
            plain_ = render_context(template, context)
            return plain_
        return None

    def get_user_data(self, user_id=None, email=None):
        filename = file_path
        print(file_path)
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            unknown_user_id = unknown_user_email = None
            for row in reader:
                if user_id is not None:
                    if int(user_id) == int(row.get('id')):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get('email'):
                        return row
                    else:
                        unknown_user_email = email
            if unknown_user_id is not None:
                print("User id {user_id} not found".format(user_id=user_id))
            if unknown_user_email is not None:
                print("User id {email} not found".format(email=email))
        return None

    def message_user(self, user_id=None, email=None, subject="Hi there"):
        user = self.get_user_data(user_id=user_id, email=email)
        file_ = 'templates/email_message.txt'
        if user:
            context = user
            template = get_template(file_)
            print(render_context(template, context))
            plain_ = self.render_message(user)
            user_email = user.get('email', 'imshubhamsingh007@gmail.com')
            try:
                email_conn = SMTP(host, port)
                email_conn.ehlo()
                email_conn.starttls()
                the_msg = MIMEMultipart()
                the_msg['Subject'] = subject
                the_msg['From'] = from_list
                part_1 = MIMEText(plain_, 'plain')
                the_msg.attach(part_1)
                email_conn.login(username, password)
                email_conn.sendmail(from_list, user_email, the_msg.as_string())
                email_conn.quit()
            except SMTPAuthenticationError:
                print("error sending message")
        return None
