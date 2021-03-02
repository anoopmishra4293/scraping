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
    #         # value = requests.get(prifex+key)
    #         # print("value",value.text)
            parts[key]=1

    if i==1:
        c = html_docs.find_all("div",class_="read-more")
        for i in c:
            key = i.a["href"]
            print("key",key)
            prifex = "https://www.constitutionofindia.net/"
            # value = requests.get(prifex+key)
            # print("value",value.text)
            schedules[key]=1
            
import csv           
with open('task_1.csv','a',newline='') as csvfile:
   writer = csv.DictWriter(csvfile, fieldnames=['part name','article name'])           
   for key in parts:
       n=key.split("/")
       # print(n[2])
       d = {'part name': n[2], 'article name': "",}
       writer.writerow(d)


# with open('task_2.csv','a',newline='') as csvfile:
#    writer = csv.DictWriter(csvfile, fieldnames=['schedules name','article name'])           
#    for key in schedules:
#         n=key.split("/")
#         #    print(n[2])
#         d = {'schedules name': n[2], 'article name': "",}
#         writer.writerow(d)
#         z =n[2]
#         z=z.replace("articles_","")
#         z=z.replace("and","")
#         z=z.replace(",","")
#         z=z.replace("___",")___")
#         y = z.split('___')
#         print("y= ",y)

#         for i in y:
#             x=i.split('__')
#             # print("x= ",x)
#             for j in x:
#                 # print("j= ",j)
#                 w=j.replace("_","(")
                
#                 print("w=",w)
#                 d = {'schedules name': w, 'article name': "",}
#                 writer.writerow(d)
                






