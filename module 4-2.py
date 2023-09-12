inches = 0

while inches >= 0:
    inches = float(input("Enter the length in inches: "))
    if inches >= 0:
      length_cm = round(inches * 2.54,2)
      print(f"{inches}inches = {length_cm}cm")
    elif inches < 0:
        print("program ends.")



