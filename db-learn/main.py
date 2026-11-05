import sqlite3

db = sqlite3.connect("Artistc.db")

cursor = db.cursor()

QUERY = '''select min("Birth Year") from artists'''
year = cursor.execute(QUERY).fetchone()
print(year)

QUERY = '''select Name from artists where "Birth Year" = ?'''
result = cursor.execute(QUERY, (year[0],)).fetchall()

print(result)