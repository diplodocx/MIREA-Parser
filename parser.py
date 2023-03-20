from bs4 import BeautifulSoup
import os
import re


def find_tags():
    for entry in os.scandir("./src"):
        if re.search(r'.html$', entry.name):
            with open(entry.path, 'r', encoding="utf-8") as file:
                src = file.read()
                soup = BeautifulSoup(src, "html.parser")
                allNews = soup.findAll('tr', id=re.compile(r'^user-index-participants'))
                for data in allNews:
                    yield separate(data)


def separate(data):
    student = data.find('a').text
    id = data.find('td', class_="cell c1").text
    post = data.find('td', class_="cell c2").text
    group = data.find('td', class_="cell c3").text
    return (student, id, group, post)


gen = find_tags()
while True:
    try:
        print(next(gen))
    except:
        break