import animal_module as am

class cat(am.animal):

    def __init__(self):
        print("Cat Created")

    def make_sound(self):
        print("meow")

    # override
    def walk(self):
        print("Cat is walking")
    # override
    def eat(self):
        print("Cat is eating")


if __name__ == "__main__":
    cat_obj = cat()

    cat_obj.walk()
    cat_obj.eat()
    cat_obj.make_sound()

    print("Current Name in Cat Module = ",__name__)