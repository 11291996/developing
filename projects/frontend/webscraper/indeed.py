import requests
from bs4 import BeautifulSoup

LIMIT = 50 
url = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{url}&start{page * LIMIT}')
        print(result.status_code)
    return jobs