#In this datatype, data are stored in key: data pair

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

'''
another process of definiing dictionary
thisdict= {
"name": "john",
"age": 36,
"country":"Norway"}
print(thisdict)
'''

#Accessing the value in dictionary using keys

print(thisdict["name"])


#to know datatype
print(type(dict))

#we can aslo include list, tuple, set inside a dictionary
mydict= dict(product= "fruits", good= True, names= {'apple', 'mango', 'orange'})
print(mydict)
   
#to know the length of dictionary
print(len(mydict))


#print the keys of dictionary
x= mydict.keys()
print(x)

#print the values of dict
y= mydict.values()
print(y)


#Now if we change the dictionary, the values of x and y will automatically(dynamically) changes
mydict["ripen"]= True
mydict["names"]= "apple"
print(x)
print(y)

#we can also update/add items to dictionary dictionary using update()
thisdict.update({"name":"yunish"})
print(thisdict.keys())
print(thisdict.values())


#The items() method will return each item in a dictionary, as tuples in a list.
z= thisdict.items()
print(z)