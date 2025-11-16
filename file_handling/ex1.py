# READ FILE FROM SYSTEM
file = None
try:
    file = open("./file_handling/demo.txt","r")

    print(file)
    # print(file.readlines())

    for line in file:
        print(line, end="")
except Exception as e:
    print(e)
finally:
    if(file):
        file.close()
        print("Closing file")
    else:
        print("File Not Found")
