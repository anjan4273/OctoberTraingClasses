name = "Bang"
try:
    # file = open("anjan.txt", "r")
    # print(file.read())
    #print(2/0)
    print(name[20])
except ErrorName1:
    print("Can't devide num with zero")
except ErrorName2:
    print("Please check your folder")
except ErrorName3:
    print("index error handled")
except:
    print("new error") # Default except must be used in last position

print("completed")