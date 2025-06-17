set1={"a", "b", "c" }
set2= {"d", "b", "c"}
set3= {"j", "k", "l"}


#union it returns the new set while update() changes the existing set and doesnot returns new set
x= set1.union(set2)    # we can aslo use x= set1|set2
print(x)

y= set1.union(set2, set3)   #for multiple set union/ y= set1| set2| set3
print(y)

#intersection it returns new set whereas we can also use intersection_update() which changes the current set instead of returning new set
a= set1.intersection(set2)      # x= set1&set2
print(a)
b= set1.intersection(set2, set3)  # y= set1& set2& set3
print(b)


#difference it returns new set whereas we can also use difference_update() which changes the current set instead of returning new set
m= set1.difference(set2)      # x= set1-set2
print(m)

'''
symmetric_update()
- The symmetric_difference() method will keep only the elements that are NOT present in both sets
'''
r= {"apple", "banana", "cherry"}
t = {"google", "microsoft", "apple"}
l = r.symmetric_difference(t)

print(l) 