import sqlalchemy as db

metadata = db.MetaData()

student = db.Table('student', metadata,
                   db.Column('ID', db.INTEGER, nullable=False, unique=True, autoincrement=True, primary_key=True),
                   db.Column('Student_ID', db.TEXT),
                   db.Column('Name', db.TEXT),
                   db.Column('Student_Group', db.TEXT),
                   db.Column('Post', db.TEXT),
                   )