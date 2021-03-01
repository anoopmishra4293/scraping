from bs4 import BeautifulSoup

import requests

r = requests.get("https://www.constitutionofindia.net/constitution_of_india")

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.title.parent.string)
# print(soup.title.parent.parent.name)
# print(soup.title.parent.parent.string)
# print(soup.p)
# print(soup.a)
#print(soup.div)
# print(soup.find_all('p'))
# print(soup.find_all('div'))


divs = soup.find_all("div", class_ = "row article-box")

print(len(divs))

parts = {}
schedules = {}

for i,html_docs in enumerate(divs):
    if i==0:
        b = html_docs.find_all("div",class_="read-more")
        print("b", len(b))
        for i in b:
            key = i.a["href"]
            print("key",key)
            prifex = "https://www.constitutionofindia.net/"
            value = requests.get(prifex+key)
            print("value",value.text)
            parts[key]=value

    if i==1:
        c = html_docs.find_all("div",class_="read-more")
        for i in c:
            key = i.a["href"]
            print("key",key)
            prifex = "https://www.constitutionofindia.net/"
            value = requests.get(prifex+key)
            print("value",value.text)
            parts[key]=value
    
 
# divs = soup.find_all("div", class_ = "read-more")



# a_tags =soup.find_all("href", class_ = "read-more")

# l1 = soup.find_all('div')
# print(len(l1))

# l2 = soup.find_all('a')
# print(len(l2))
