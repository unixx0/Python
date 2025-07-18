class InvalidAgeError(Exception):
    def __init__(self, msg= "Age caannot be Negavtive"):
        self.msg= msg

    def __str__(self):
        return(f"{self.msg}")
    

def age(age):
    if age<0:
        raise InvalidAgeError()
    else:
        print("valid age")
        

try:
    age(-5)
except InvalidAgeError as e:
    print(e)

    




    