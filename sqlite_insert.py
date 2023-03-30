from parser import get_generator
import sqlalchemy as db
from db_model import student

def fill_db():
    gen = get_generator()
    engine = db.create_engine("sqlite:///Students.db")
    with engine.connect() as connection:
        while True:
            try:
                insertion_query = student.insert().values(next(gen))
                connection.execute(insertion_query)
            except AttributeError:
                break
        connection.commit()