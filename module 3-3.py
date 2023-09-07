gander = input("Enter your biological gander--F/M: ")
hemoglobin = float(input("Enter your hemoglobin value(g/l):  "))
if gander == "F":
    if hemoglobin>=117 and hemoglobin<=155 :
     print("A normal hemoglobin value!")
    elif hemoglobin <117:
     print("The hemoglobin value is low!")
    elif hemoglobin>155:
     print("The hemoglobin value is high!")
elif gander == "M":
    if hemoglobin>=134 and hemoglobin<=167 :
     print("A normal hemoglobin value!")
    elif hemoglobin <134 :
     print("The hemoglobin value is low!")
    elif hemoglobin>167:
     print("The hemoglobin value is high!")

