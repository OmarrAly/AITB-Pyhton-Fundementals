import requests
from bs4 import BeautifulSoup

pageCounter = 0
#urlResult = requests.get("https://wuzzuf.net/search/jobs/?q=php&a=hpb")
urlResult = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=php&start={pageCounter}")
# save html content

while True:
    pageCounter+=1
    urlResult = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=php&start={pageCounter}").text
    soup = BeautifulSoup(urlResult, 'lxml')
    next_page = soup.select_one('[data-test=next-link]')
        
    if next_page is None:
        break
    print(pageCounter)

markup = urlResult

# take object from beautiful soup
bs = BeautifulSoup(markup , 'lxml')

# find h2 from markup
jobHeadings = bs.find_all('h2' , {"class" : "css-m604qf"})
jobAnchors = bs.find_all('a' , {"class" : "css-o171kl"})
jobLocation = bs.find_all('span' , {"class" : "css-5wys0k"})
#experienceYears = bs.find_all('span' , {"class" : '' })

#print(experienceYears)
# print(jobAnchors)
# create list to append all jobs 
jobs = []

for i in range(len(jobHeadings)):
    jobs.append(jobHeadings[i].text)
    jobs.append(jobLocation[i].text)

#print(jobs)
# Write into file 
with open('jobs.txt' , 'w') as jobsFile:
    for job in jobs:
        jobsFile.write(job)
    print('Jobs Added Successfully ')

# Read Jobs

with open('jobs.txt' , 'r') as jobsFile:
    print(jobsFile.read())