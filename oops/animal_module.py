class animal:

    # Constructor
    def __init__(self):
        print("Animal object created")

    def walk(self):
        print("Animal Is Walking")
    

    def eat(self):
        print("Animal Is Eating")
    

if __name__ == "__main__":
    print("Current Name = ",__name__)
    obj = animal()
    obj.eat()
    obj.walk()

