import requests
from bs4 import BeautifulSoup
import time

url = "https://remoteok.com/remote-data-analyst-jobs"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("tr", {"class": "job"})

for job in jobs:
    title = job.find("h2", {"itemprop": "title"})
    location = job.find("div", {"class": "location"})
    
    if title and location:
        print(title.text.strip(), "-", location.text.strip())
    time.sleep(1)  # polite delay