from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template


import os

from configuration import MY_ADDRESS


class SendEmail():
    def __init__(self, user, job):
        self.user = user
        self.job = job

    def read_template(self):
        """
        Returns a Template object comprising the contents of the
        file specified by path.
        """
        with open(os.path.join(os.getcwd(), "templates", "email.html"), "r", encoding="utf-8") as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def create_message(self):
        """
        Create the body of the message.
        """
        message_template = self.read_template()
        message = message_template.substitute(
            PERSON_NAME=self.name,
            COMPANY=self.job.company,
            PROFESSION=self.job.job_name,
            EXPERIENCE=self.job.experience,
            SALARY_MIN=self.job.salary_min,
            SALARY_MAX=self.job.salary_max,
            CURRENCY=self.job.currency,
            SKILLS="\n".join([skill.name for skill in self.job.skills.all()]),
            DESCRIPTION=self.job.description,
        )
        return message
    
    def email_sender(self, s):


        # Create message container - the correct MIME type is multipart/alternative.
        message = self.create_message()
        msg = MIMEMultipart()
        msg["From"] = MY_ADDRESS
        msg["To"] = self.user.email
        msg["Subject"] = "This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, "plain"))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg


# For each contact, send the email:


