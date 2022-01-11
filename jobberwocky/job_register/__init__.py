import requests

EXTERNALS_URL_JOB_OFFERS = "http://localhost:8081/jobs?name="


def input_parser(externals_jobs_offers: list, jobs_data_list: list = None) -> list:
    """
    This function will parse the input data and return a list of jobs formated as a dictionary
    to match with local database model
    """
    if jobs_data_list is None:
        jobs_data_list = []
    TAGS = {0: "name", 1: "salary", 2: "country", 3: "skills"}
    if not externals_jobs_offers:
        return jobs_data_list
    if isinstance(externals_jobs_offers[0], list):
        jobs_data_list.append(
            {TAGS[index]: job for index, job in enumerate(externals_jobs_offers.pop(0))}
        )
        input_parser(externals_jobs_offers, jobs_data_list)
    else:
        jobs_data_list.append(
            {TAGS[index]: job for index, job in enumerate(externals_jobs_offers)}
        )
        return jobs_data_list
    return jobs_data_list


def get_externals_job_offers(job_name: str = "") -> list:
    """
    do a request to externals API to get more JOB offers
    """
    externals_jobs_offers = requests.get(EXTERNALS_URL_JOB_OFFERS + job_name)
    if externals_jobs_offers.status_code == 200:
        externals_jobs_offers = externals_jobs_offers.json()
    if isinstance(externals_jobs_offers, dict):
        externals_jobs_offers = externals_jobs_offers.get("jobs", [])
    return input_parser(externals_jobs_offers)
