mylist=["apple", "mango", "orange", "pineapple"]
ylist=[]
for x in mylist:
    print(x)
mylist.insert(0, "litchi")
print(mylist)
mylist.append("kiwi")
for i in range(len(mylist)):
    print(mylist[i])
for x in mylist:
    if len(x)!=5:
        ylist.append(x)
print(ylist)
mulist1= [x.upper() for x in mylist]
print(mulist1)
mylist.extend(ylist)
print(mylist)



y= "my name is yunish name"
print(y.count("name"))


print(y.index("name"))


print(mylist.index("apple"))