import sqlite3

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('recipeDB')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE recipe(id INTEGER PRIMARY KEY, name TEXT,
                       stars INTEGER, difficulty INTEGER, portions INTEGER)
''')

cursor.execute('''
    CREATE TABLE recipeIngredient(id INTEGER PRIMARY KEY, recipeId INTEGER FORIEGN KEY,
                       ingredient INTEGER FORIEGN KEY, quantity INTEGER, measurementType TEXT)
''')

cursor.execute('''
    CREATE TABLE ingredient(id INTEGER PRIMARY KEY, name TEXT,
                       type TEXT)
''')

db.commit()
