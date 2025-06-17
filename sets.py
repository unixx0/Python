thisset= {"apple", "mango", "banana" }  #dublicate values not allowded
print(thisset)       #sets are unordered

#add an item form set
thisset.add("orange")
print(thisset)

#delete an item from set
thisset.remove("orange")    #sends error if item i not in set
print(thisset)

#or

thisset.discard("orange")     #doesnot sends error if item is not present in set
print(thisset)



#pop method
'''
here an random value is removed from the set
'''
x= thisset.pop()
print(x)   #returns which item is removed
print(thisset)




thisset1={"a", "b", "c", "d"}


#to join two sets or set with link
thisset.update(thisset1)
print(thisset)

thislist= ['my', 'name', 'is']
thisset.update(thislist)
print(thisset)

thistuple= ('h', 'e', 'm')
thisset.update(thistuple)
print(thisset)


#accessing the items in set
for i in thisset:
    print(i)