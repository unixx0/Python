class Rectangle:
    def input(self, l, b):
        self.length= l
        self.breadth= b
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
    def display(self):
        print(f"The perimeter is {self.perimeter()}")
        print(f"The area is {self.area()}")


if __name__ == "__main__":
    r1= Rectangle()
    r1.input(2,3)
    r1.display()
    print(r1.length)
        
    
    
    
