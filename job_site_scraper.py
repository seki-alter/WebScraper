import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

""" job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print() """

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for python_job_element in python_job_elements:
    title_element = python_job_element.find("h2", class_="title")
    company_element = python_job_element.find("h3", class_="company")
    location_element = python_job_element.find("p", class_="location")
    link_url = python_job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()
