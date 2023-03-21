import sqlalchemy as db
from db_model import metadata

def create_db():
    engine = db.create_engine("sqlite:///Students.db")
    with engine.connect():
        metadata.create_all(engine)
