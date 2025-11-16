# READ FILE FROM SYSTEM

try:
    file = open("./file_handling/demo.txt","r")

    print(file)
    # print(file.readlines())

    for line in file:
        print(line)
except Exception as e:
    print(e)
finally:
    file.close()