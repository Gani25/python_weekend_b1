class AgeInvalidError(Exception):

    def __init__(self, *args):
        super().__init__(*args)

class Person:

    def __init__(self, age):
        
        if age < 0 or age > 120:
            # raise error
            # raise AgeInvalidError("Age cannot be 0 or greater than 120")
            raise ValueError("Age cannot be 0 or greater than 120")
        
        self.age = age 

    
    def __str__(self):
        return f"Person Info\nAge = {self.age}"

RED = "\033[91m"  # ANSI code for red text
BLUE = "\033[94m"
RESET = "\033[0m" # ANSI code to reset text attributes
if __name__ == "__main__":

    try:
        person_obj = Person(5)
        print(BLUE+person_obj.__str__()+RESET)
    except Exception as e:
        print(RED + e.__str__()+RESET)
