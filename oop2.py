class Dog:
    species= "Japnese Spitz"
    def __init__ (self, name, age):
        self.name= name
        self.age= age
    def __str__ (self):
        return(f'The name of dog is {self.name} and age is {self.age}')


if __name__ =="__main__":
    dog1= Dog("Aero", 5)
    dog2= Dog("Babu", 15)
    print(dog1)
    print(dog2)
    print(dog1.name)
    print(dog1.species)
    print(dog2.species)
    Dog.species= "German Sephard"
    print(dog1.species, dog2.species)
    dog1.name= "ram"
    print(dog1)