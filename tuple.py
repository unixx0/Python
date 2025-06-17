# check if item is present in tuple
mytuple= ("apple", "banana", "litchi", "mango")
if("apple" in mytuple):
    print("Present")
else:
    print("not present")

'''
y= "my name"
mylist=list(y)
print(mylist)
'''

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
mylist= list(mytuple)
mylist.append("orange")
mytuple= tuple(mylist)
print(mytuple)

#adding two tuples
mytuple1= tuple(("pineapple",))   #put a comma if there is only one item in tuple. Orelse it take string values
mytuple= mytuple+mytuple1
print(mytuple)

mylist.extend(mytuple)
print(mylist)


#to delete tuple completely we can use del keyword
del mytuple1



#counttext of tuple
print(mytuple.count("apple")) #only takes one argument in con

y= "my name"
print(y.count("m"))     # incase of string it takes 3 argument
print(y.count("m",0,4))
print(y.count("name",0,4))
print(y.count("m",0,4))



#count
print(y.count("n"))
print(y.count("name"))
print(y.count("name", 0, 5))