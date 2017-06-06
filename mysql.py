import MySQLdb
import os
from prettytable import PrettyTable


db = MySQLdb.connect(os.environ["MYSQL_HOST"], os.environ["MYSQL_USER"], os.environ["MYSQL_PASSWORD"], "test1")

cur = db.cursor()

cur.execute("SELECT * FROM mydb.cars")

id = []
model = []
mileage = []

x = PrettyTable (["id", "Model", "Mileage"])

for row in cur.fetchall():
    x.add_row([int(row[0]), int(row[1]), int(row[2])])

print x.get_string(start=0, end=10)

db.close()