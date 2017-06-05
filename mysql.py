import MySQLdb
from prettytable import PrettyTable

db = MySQLdb.connect("localhost", "root", "dustyM12", "thedatabase")

cur = db.cursor()

cur.execute ("SELECT * FROM thedatabase.cars")

id = []
model = []
mileage = []

x = PrettyTable (["id", "Model", "Mileage"])

for row in cur.fetchall():
    x.add_row([int(row[0]), int(row[1]), int(row[2])])

print x.get_string(start=0, end=10)

db.close()