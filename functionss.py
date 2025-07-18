#args

def myfun1(*arg):
    for x in arg:
        print(x)

l= [1,2,3]
myfun1(l)




def myfun2(**kwarg):
    for x, y in kwarg.items():
        print(y)


myfun2(fname= "tunish", lname= "shrestha")





mydict= {"dict1": {"name": "Yunish",
"class":9},
"dict2":{"name": "ram",
         "class": 9} }
print(mydict)
for key, value in mydict.items():
    print(key)
    print(value)
    for x, y in value.items():
        print(x, y)