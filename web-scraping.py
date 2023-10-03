import requests
from bs4 import BeautifulSoup
import csv

jobs_page = requests.get("https://wuzzuf.net/a/Frontend-Developer-Jobs-in-Alexandria")

jobs_list = []


def jobs(page):
    src = page.content
    html = BeautifulSoup(src, "lxml")
    jobs_block = html.find("div", {"class": "css-9i2afk"}).contents[0]
    list_jobs = jobs_block.find_all("div", {"class": "e1v1l3u10"})
    for i in range(len(list_jobs)):
        title = (
            list_jobs[i].find("div", {"class": "css-laomuu"}).find("h2").text.strip()
        )
        address = list_jobs[i].find("span", {"class": "css-5wys0k"}).text.strip()
        date = list_jobs[i].find("div", {"class": "css-4c4ojb"})
        if not date is None:
            date = date.text.strip()
        job_dict = {"Job Title": title, "Address": address, "Date": date}
        jobs_list.append(job_dict)
    keys = job_dict.keys()
    with open("d:/sara-courses/jobs.csv", "w") as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs_list)
        print("File created")


jobs(jobs_page)
