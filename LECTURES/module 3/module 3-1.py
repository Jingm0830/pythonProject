length = input("Tell me the length of the zander in centimeters: ")
size_limit = 42
length = float(length)
if length < size_limit:
    print("not fulfill the size limit!!!")
    print("size limit:>=42cm")
    print("release the fish back into the lake, please!")
elif length >= 42:
    print("Hyvää!!!")
