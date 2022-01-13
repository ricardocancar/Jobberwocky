from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template


import os

from configuration import MY_ADDRESS


def read_template(path):
    """
    Returns a Template object comprising the contents of the
    file specified by path.
    """
    with open(path, "r", encoding="utf-8") as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


# For each contact, send the email:
def send_email(s , user, job) -> None:
    """
    this function will send an email to the user
    args:
        s: smtplib object
        user: user object from database
        job: job object from database
    """
    user_name = user.name
    user_mail = user.email

    msg = MIMEMultipart()  # create a message
    message_template = read_template(os.path.join(os.getcwd(), "email_template.txt"))
    # add in the actual person name to the message template
    message = message_template.substitute(
        PERSON_NAME=user_name,
        COMPANY=job.company,
        PROFESSION=job.job_name,
        EXPERIENCE=job.experience,
        SALARY_MIN=job.salary_min,
        SALARY_MAX=job.salary_max,
        CURRENCY=job.currency,
        SKILLS="\n".join([skill.name for skill in job.skills.all()]),
        DESCRIPTION=job.description,
    )

    # setup the parameters of the message
    msg["From"] = MY_ADDRESS
    msg["To"] = user_mail
    msg["Subject"] = "This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, "plain"))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg

