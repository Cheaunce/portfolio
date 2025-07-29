import requests
from collections import defaultdict
from openpyxl import Workbook

api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
response = requests.get(api_url)
data = response.json()

#Language skills to search for
languages = [
    "C",
    "C#",
    "C++",
    "Java",
    "JavaScript",
    "Python",
    "Scala",
    "Oracle",
    "SQL Server",
    "MySQL Server",
    "PostgreSQL",
    "MONGODB"]

language_counts = defaultdict(int) #empty dynamic dict that initializes missing keys to 0

for job in data:
    key_skills = [skill.lower().strip() for skill in job.get("Key Skills", "").lower().strip().split('|')]
    for lang in languages:
        if lang.lower() in key_skills:
            language_counts[lang] += 1
            
#sort dict as alphabetical list            
sorted_language_counts = sorted(language_counts.items(), key=lambda x: x[0].lower())            



#Write to workbook
wb = Workbook()
ws = wb.active
ws.Title = "Technologies"
ws.append(["Technology", "Job Postings"])
wb.save("tech_job_counts.xlsx")