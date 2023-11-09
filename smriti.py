# connect to mysql
import pymysql
import sys
import os
import time
import datetime
import json

# connect to mysql
connection = pymysql.connect(
    host="localhost", port=9906, passwd="root", user="root", db="dump"
)
cursor = connection.cursor()

# query to call
query = "SELECT users1.name as for_user, users2.name as from_user, t_data.test FROM t_data INNER JOIN users as users1 ON users1.uid = t_data.for_user INNER JOIN users as users2 ON users2.uid = t_data.by_user ORDER BY for_user"

# execute query
cursor.execute(query)

# fetch all the results
data = cursor.fetchall()

current_user = ""
for row in data:
    if current_user != row[0]:
        current_user = row[0]
        print("\n\n")
        print("# " + current_user)
    print("__" + row[1] + "__")
    print("\n")
    print(row[2].decode("utf-8"))
    print("\n")
