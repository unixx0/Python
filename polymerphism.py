class apple:
    def display(self, g):
        print(f"This is class {g}")

class orange(apple):
    def display(self,g, a):
        print(f"This is class {a}")
        super().display(g)



b= orange()
b.display("mango","orange")
        
