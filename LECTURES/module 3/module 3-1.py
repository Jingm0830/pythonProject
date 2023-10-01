length =float(input("How long is the zander in centimeter?\n"))
if length < 42:
    i = 42 - length
    print("Release the fish back into the lake!\n"
          f"This one was {i}centimeters below the size limit")
else:
    print("Great!!!")
