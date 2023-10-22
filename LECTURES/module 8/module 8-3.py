"""
Write a program that asks the user to enter the ICAO codes of two airports.
The program prints out the distance between the two airports in kilometers.
The calculation is based on the airport coordinates fetched from the database.
Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
write geopy into the search field and finish the installation.
"""
from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='7890',
    autocommit=True
)
cursor = connection.cursor();


def getSqlResult(sql):
    cursor.execute(sql)
    return cursor.fetchall()


ICAO1= input("Enter ICAO code A:  ") + "'"
ICAO2= input("Enter ICAO code B:  ") + "'"

sql = "select latitude_deg, longitude_deg, `name` from airport where ident = '"
sql1 = sql + ICAO1
sql2 = sql + ICAO2
A = ''
B = ''

airportA = (0, 0)
airportB = (0, 0)

result1 = getSqlResult(sql1)
if (len(result1) > 0):
    airportA = (result1[0][0], result1[0][1])
    A = result1[0][2]

result2 = getSqlResult(sql2)
if (len(result2) > 0):
    airportB = (result2[0][0], result2[0][1])
    B = result2[0][2]
print(f"The distance between {A} and {B} is ", distance.distance(airportA, airportB).kilometers,"km")