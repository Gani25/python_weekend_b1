# READ FILE FROM SYSTEM

try:
    with open("./file_handling/demo.txt","r") as file:
        print(file)
        # print(file.readlines())
        for line in file:
            print(line, end="")
except Exception as e:
    print(e)

