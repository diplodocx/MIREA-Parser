from bs4 import BeautifulSoup
import os
import re


def get_generator():
    for entry in os.scandir("./src"):
        if re.search(r'.html$', entry.name):
            with open(entry.path, 'r', encoding="utf-8") as file:
                src = file.read()
                soup = BeautifulSoup(src, "html.parser")
                raw_students = soup.findAll('tr', id=re.compile(r'^user-index-participants'))
                for data in raw_students:
                    yield separate(data)


def separate(data):
    student = data.find('a').text
    id = data.find('td', class_="cell c1").text
    post = data.find('td', class_="cell c2").text
    group = data.find('td', class_="cell c3").text
    return {'Name': student, 'Student_ID': id, 'Student_Group': group, 'Post': post}
