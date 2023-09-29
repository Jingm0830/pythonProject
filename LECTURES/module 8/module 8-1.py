"""
Write a program that asks the user to enter the ICAO code of an airport.
The program fetches and prints out the corresponding airport name and
location (town) from the airport database used on this course.
The ICAO codes are stored in the ident column of the airport table
"""

import mysql.connector

#main program
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='7890',
    autocommit=True
    )


def get_airport_name_location_byICAO(ICAO):
    sql = "SELECT name, municipality  FROM Airport WHERE ident='"+ICAO+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print(f"This is {row[0]} in {row[1]}.")
    return



ICAO = input("Enter the ICAO_code:   ")
get_airport_name_location_byICAO(ICAO)


