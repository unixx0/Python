def myfun(a,b):
    c= a+b
    print(f"the sum of {a} and {b} is {c}")

l= 6
j= 6
myfun(l,j)


def thisfun (**a):
    print(a["lname"])

thisfun(fnmae= "yunish", lname= "shrestha")


#default argument
def thisfun(name= "yunish"):
    print(f"My name is {name}")

thisfun()
thisfun("rram")
thisfun("shyam")



#keyword only argument
def function1(x,y,/):    #/ aagadi ko sabei argument postion garument hunu  parcha
    print(x+y)


function1(2,3)



#postion only argument
def function2(*, x,y):    #* pachadi ko sabei argument keyword argument hunu  parcha
    print(x+y)


function2(y=4, x=6)


#postion only and keyword argument
def function3(x,y,/,*,a,b):    
    print(x+y+a+b)


function3(2,3,a=5, b=7)
