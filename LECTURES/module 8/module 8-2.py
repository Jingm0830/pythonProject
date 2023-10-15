"""
Write a program that asks the user to enter the area code (for example FI)
and prints out the airports located in that country ordered by airport type.
For example, Finland has 65 small airports, 15 helicopter airports and so on.
"""
import mysql. connector
#main program

connection= mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='7890',
    autocommit=True
)
country = input("Enter the area code:  ")
sql_type=f"SELECT type, count(*) FROM airport WHERE iso_country = '"+country+"' group by type;"
sql_name=f"SELECT name FROM country WHERE iso_country = '"+country+"';"
cursor_t=connection.cursor()
cursor_t.execute(sql_type)
result_t = cursor_t.fetchall()
cursor_n=connection.cursor()
cursor_n.execute(sql_name)
result_n = cursor_n.fetchall()
if result_t is not None:
    print(f"{result_n} has {result_t} airports.")
else:
    print("No data!")



