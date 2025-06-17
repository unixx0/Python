mylist= [100, 200, 500, 600, 788]

#method 1
thislist= mylist.copy()
print(thislist)

#method 2
thislist= list(mylist)
print(thislist)

#method 3
thislist= mylist[:]
print(thislist)



ylist=[]
for x in mylist:
    ylist.append(x)
print(ylist)


for i in range(len(mylist)):
    ylist[i]= mylist[i]
print(ylist)


for i in range(len(mylist)):
    ylist.insert(i, mylist)
print(ylist)

