username = "python"
password = "rules"
times_max = 5
times = 0
print("Enter the correct username and password, please!")
USERNAME = input("Username: ")
PASSPORT = input("password: ")

while times <= 5:

    if username == USERNAME and password == PASSPORT:
        print("Welcome!")
        break
    else:
        print("Enter again!")
        print("Enter the correct username and password, please!")
        USERNAME = input("Username: ")
        PASSPORT = input("password: ")


    times += 1

else:
        print("Access denied")

