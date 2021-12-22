try:
    file = open("anjan.txt", "r")
    print(file.read())
except:
    print("Please check your folder")
print("completed")