talents_str = input("Enter talents: ")
pounds_str = input("Enter pounds: ")
lots_str = input("Enter lots: ")
talents = float(talents_str)
pounds = float(pounds_str)
lots = float(lots_str)
grams = talents*20*32*13.3 + pounds*32*13.3 + lots*13.3
kilograms = grams/1000
print(f"The weight in modern units: "+ str(grams), "grams", "and" + str(kilograms), "kilograms")