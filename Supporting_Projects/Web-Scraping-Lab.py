from bs4 import BeautifulSoup
import requests, csv

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

table = soup.find('table')
dict = []  # List to hold dicts

for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) >= 4:
        language = cols[1].get_text(strip=True)
        salary = cols[3].get_text(strip=True)
        dict.append({"Language": language, "Average Annual Salary": salary})

with open("popular-languages.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["Language", "Average Annual Salary"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(dict)
