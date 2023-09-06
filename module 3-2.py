cabin_class = input("Welcome to cruise ship and choose your cabin class in LUX、A、B、C,please：")
if cabin_class == "LUX":
    print("your cabin is an upper-deck cabin with a balcony!")
elif cabin_class == "A":
    print("your cabin is above the car deck, equipped with a window")
elif cabin_class== "B":
    print("your cabin is windowless cabin above the car deck")
elif cabin_class == "C":
    print("your cabin is windowless cabin below the car deck")
else:
    print("Invalid cabin class")