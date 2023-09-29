AIRPORTRT_ICAO = {
    "John F. Kennedy International Airport": "JFK",

    "Los Angeles International Airport": "LAX",

    "Heathrow Airport": "EGLL",

    "Tokyo Narita International Airport": "RJAA",

    "Sydney Kingsford Smith International Airport": "YSSY"
}

Y = "yes"
N = "no"


while True:
    Q1 = input("Do you want to enter a new airport? Y/N:  ")
    Q2 = input("Do you want to  fetch airport information? Y/N:  ")
    Q3 = input("Do you want to quit? Y/N:  ")
    if answer == Y:
        new_airport = input("Enter the name and ICAO of the airport:" ":"  ". ")
        AIRPORTRT_ICAO.add(new_airport)
    elif Q1 == N:

        if Q2 == Y:
            ICAO_code = input("Enter the ICAO code:   ")
            for ICAO_code in AIRPORTRT_ICAO:
                print(f"{ICAO_code} is {AIRPORTRT_ICAO[ICAO_code]}")
        elif Q2 == N:

            if Q3 == Y:
                break



