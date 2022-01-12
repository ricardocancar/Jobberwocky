import os
from django.db.models.query_utils import PathInfo
from django.test import TestCase
from job_register import get_externals_job_offers, input_parser
from job_register.send_email import read_template

EMAIL_TEMPLATE = """Dear ${PERSON_NAME}, 

This is a new job offer that we think it may work for You 
 Company: ${COMPANY}
 Job offer ${PROFESSION}
 Experience ${EXPERIENCE}
 Salary ${SALARY_MIN} - ${SALARY_MAX} (${CURRENCY})
 Skills ${SKILLS}

description:
${DESCRIPTION}


Have a great day! 

best Regards"""


class TestOthers(TestCase):
    def test_get_externals_job_offers_no_existing_job(self):
        """
        test the get_externals_job_offers function
        """
        job_name = "test_job_name"
        externals_jobs_offers = get_externals_job_offers(job_name)
        self.assertEqual(externals_jobs_offers, [])

    def test_get_externals_job_offers_existing_job(self):
        job_name = "java developer"
        externals_jobs_offers = get_externals_job_offers(job_name)
        self.assertEqual(len(externals_jobs_offers), 3)

    def test_input_parser(self):
        """
        transform the input data like this:
                [
            ["Developer", 30000, "Argentina", ["OOP", "PHP", "MySQL"]],
            ["DBA", 35000, "Spain", ["MySQL", "Percona", "Bash"]]
        ]
        """
        input_data = [
            ["Developer", 30000, "Argentina", ["OOP", "PHP", "MySQL"]],
            ["DBA", 35000, "Spain", ["MySQL", "Percona", "Bash"]],
        ]
        input_data_parsed = input_parser(input_data)
        expected_output = [
            {
                "name": "Developer",
                "salary": 30000,
                "country": "Argentina",
                "skills": ["OOP", "PHP", "MySQL"],
            },
            {
                "name": "DBA",
                "salary": 35000,
                "country": "Spain",
                "skills": ["MySQL", "Percona", "Bash"],
            },
        ]
        self.assertEqual(input_data_parsed, expected_output)

    def test_input_parser_empty_list(self):
        """
        transform the empty input data:
        """
        input_data = []
        input_data_parsed = input_parser(input_data)
        expected_output = []
        self.assertEqual(input_data_parsed, expected_output)

    def test_read_template(self):
        """
        test the read_template function
        """

        template = read_template(
            os.path.join(os.getcwd(), "..", "..", "email_template.txt")
        )
        self.assertEqual(template.template, EMAIL_TEMPLATE)
