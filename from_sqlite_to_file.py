from db_model import student
import os
import sqlalchemy as db
import re


def create_folders():
    groups = select_groups()
    for tuple in groups:
        group = tuple[0]
        prefix = "./lists"
        if not os.path.exists(prefix):
            os.mkdir(prefix)
        if re.search(r'^[А-Я]{4}-\d{2}-\d{2}', group):
            print(group)
            group = group.replace(' | ', ' ')
            institute_path = '/'.join([prefix, group[0]])
            year_path = '/'.join([institute_path, group[-2:]])
            if not os.path.exists(institute_path):
                os.mkdir(institute_path)
            if not os.path.exists(year_path):
                os.mkdir(year_path)


def contain_folders():
    groups = select_groups()
    for tuple in groups:
        group = tuple[0]
        group = group.replace(' | ', ' ')
        if re.search(r'^[А-Я]{4}-\d{2}-\d{2}', group):
            path = f"./lists/{group[0]}/{group[-2:]}/{group}.txt"
            students = select_lists(group)
            list = formate_lists(students)
            with open(path, 'w') as file:
                file.write(list)


def select_groups():
    engine = db.create_engine("sqlite:///Students.db")
    with engine.connect() as connection:
        selection_query = db.select(student.columns.Student_Group) \
            .group_by(student.columns.Student_Group) \
            .order_by(student.columns.Student_Group)
        result = connection.execute(selection_query)
        return result.fetchall()


def select_lists(group):
    engine = db.create_engine("sqlite:///Students.db")
    with engine.connect() as connection:
        selection_query = db.select(student) \
            .where(student.columns.Student_Group == group) \
            .order_by(student.columns.Name)
        result = connection.execute(selection_query)
        return result.fetchall()


def formate_lists(raw_list):
    strings = []
    for i, student in enumerate(raw_list):
        strings.append(f"{i + 1}. {student[2]} ({student[1]}, {student[4]})")
    return '\n'.join(strings)
