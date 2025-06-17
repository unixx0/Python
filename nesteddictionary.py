mydict= dict(dict1= dict(name= "yunish", grade= 11, rollno= 23 ),
             dict2= dict(name= "ram", grade= 9, rollno= 30),
             dict3= dict(name="shyam", grade= 11, rollno= 1))
print(mydict)
print(mydict["dict1"])
print(mydict["dict2"]["name"])


#accessing using loops
for x in mydict:
    print(mydict[x])




for key, value in mydict.items():
    print(key, value)
    for x,y in value.items():
        print(x,y)
        