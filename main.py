from typing import Optional

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    title: str
    company: str | None
    location: str | None
    application_url: str | None
    learn_url: str | None
    subtitle: Optional[str] = None
    description: Optional[str] = None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    jobs_board = soup.find(id="ResultsContainer")
    # print(jobs_board.prettify())

    job_elements = jobs_board.find_all("div", class_="card-content")
    python_jobs = jobs_board.find_all("h2", string=lambda txt: "python" in txt.lower())

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    # Fetch link/url from <a> tag "href" attribute
    for job_element in python_job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        # -- snip --
        links = job_element.find_all("a")
        job = Job(title=title_element.text.strip(),
                  company=company_element.text.strip(),
                  location=location_element.text.strip(),
                  learn_url=links[0]['href'],
                  application_url=links[1]['href'])

        print(job)

# Each job card has two links associated with it.
# You’re looking for only the second link.
# How can you edit the code snippet shown above so that you always collect only the URL of the second link?
