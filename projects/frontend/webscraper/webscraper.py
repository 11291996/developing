#extracting data from a web site
#extract indeed and stackoverflow job search pages as csv file

import requests #python package that provides web information

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50") 

#print(indeed_result.text) #.text gives html of request.get

#beautifulsoup4 >> python package that extracts data from html and navigate data structure of html

from bs4 import BeautifulSoup #function in beautifulsoup4

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser') #parsing the html and making html data a soup object 

#print(indeed_soup) #similar to requests but in soup

#.find finds something in soup html
pagination = indeed_soup.find('div', {'class': 'pagination'}) 

#print(pagination) #upper class of page number data. anchor 'a' contains the data 

links = pagination.find_all('a') #another upper class 

#print(pages) #this is a list data!

pages = []

for link in links[:-1]: #use for loop to print all the spans in objects in the list 'pages'
    #print(page.find("span")) #span is the page number data. again use find number
    pages.append(int(link.string)) #makes a list of span data #.string extracts the text only #links.find('span').string is available
    #change to integer

#print(pages) #-1 eliminates the next button #integer string of pages

max_page = pages[-1]

range(max_page)

for n in range(max_page):
    print(f"start = {n * 50}") #how many total pages are there