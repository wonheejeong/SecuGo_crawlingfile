import requests
from bs4 import BeautifulSoup


def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

def get_crawl(number):
    BASE_URL = 'http://cwe.mitre.org/data/definitions/{}.html'.format(number)
    html = get_html(BASE_URL)
    soup = BeautifulSoup(html, 'html.parser')

    #Description
    div = soup.find("div",{"id": "Description"})
    description = div.find("div",{"class": "indent"})

    print("Description:" + str(description.text))

    #example code
    for el in soup.find_all('div', attrs={"id":"ExampleCode"}):
        print (el.get_text())

get_crawl(601)

# print("PHP:"+ str(examplecode.text))