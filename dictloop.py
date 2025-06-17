mydict= dict(name= "yunish", grade= 13, rollno= 36)

#accessing the keys of dict
for x in mydict:
    print(x)

#for accessing the values in dict
for x in mydict:
    print(mydict[x])


#another way of doing it
for x in mydict.keys():
    print(x)


#another way
for x in mydict.values():
    print(x)


#to print them simultaneously
for x,y in mydict.items():
    print(f"{x}: {y}")