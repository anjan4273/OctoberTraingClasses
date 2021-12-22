name = "Bang"
try:
    # file = open("anjan.txt", "r")
    # print(file.read())
    #print(2/0)
    print(name[20])
except ZeroDivisionError:
    print("Can't devide num with zero")
except FileNotFoundError:
    print("Please check your folder")
except IndexError:
    print("index error handled")
except:
    print("new error")

print("completed")