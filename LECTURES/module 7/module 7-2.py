names = set()

while True:
    n = input("Enter a name or quit with a empty sting:  ")

    if n == "":
        break

    elif n in names:
        print("Existing name!")
    else:
        print("new name!")
        names.add(n)

for n in names:
    print(n)

