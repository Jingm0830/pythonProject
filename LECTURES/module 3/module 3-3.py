gander = input("Enter your biological gander--F/M: ")

if gander == "F":
    hemoglobin_F = float(input("Enter your hemoglobin value(g/l):  "))
    if hemoglobin_F>=117 and hemoglobin_F<=155 :
     print("A normal hemoglobin value!")
    elif hemoglobin_F <117:
     print("The hemoglobin value is low!")
    else:
     print("The hemoglobin value is high!")

elif gander == "M":
    hemoglobin_M = float(input("Enter your hemoglobin value(g/l):  "))
    if hemoglobin_M>=134 and hemoglobin_M<=167 :
     print("A normal hemoglobin value!")
    elif hemoglobin_M <134 :
     print("The hemoglobin value is low!")
    else:
     print("The hemoglobin value is high!")

else:
    print("Invalid!")
