from django.db.models.query_utils import PathInfo
from django.test import TestCase
from job_register import get_externals_job_offers, input_parser


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
