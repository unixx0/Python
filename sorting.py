mylist= [100, 500, 200,  600, 700, 1000]
thislist= ["apple", "mango"]
mylist.sort()
print(mylist)
mylist.sort(reverse= True)
print(mylist)

def fun(n):
    return (abs(n-500))


mylist.sort(key= fun)
print(mylist)

#to make sorting case insensitve
thislist.sort(key= str.lower)
print(thislist)


mylist.reverse()
print(mylist)