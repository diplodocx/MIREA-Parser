# This script gets every MIREA student from HTML and creates local db containing them
То run script you have to write path to the html page. HTML page can be taken from edu-mirea site in subject "Как учиться в электронной среде".
To create SQLite db run sqliteCreate.create_db(), to fill SQLite db run sqliteInsert.fill_db()
To create and fill MongoDB db run mongoCreate.mongo_insert(). Previously you have to create .env file and add 2 strings in it:
MONGO_URI=<your_URI>
MONGO_DB_NAME=your_db
Choose URI to your db and it's name.

Btw the Moodle API exists but I didn't know that before.