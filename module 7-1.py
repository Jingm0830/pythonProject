season = ("spring", "summer", "autumn", "winter")
month_in_season = {12:3, 1:3, 2:3, 3:0, 4:0, 5:0, 6:1, 7:1, 8:1, 9:2, 10:2, 11:2}

month_number = int(input("Enter the month number (1-12): "))

if 0< month_number < 12:
    season_number = month_in_season[month_number]
    season = season[season_number]



print(f" The {month_number} one is {season}.")
