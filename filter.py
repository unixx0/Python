# example of filter function
list1= [1,2,3,4,5,6]
list2=[x*2 for x in list1 if x%2==0]   #list comprehension
print(list2)

#filter function
fun= lambda x: x%2==0
#filter(function, iterator)
list3= list(filter(fun, list1))
print(list3)



s = ['  hello  ', '  world ', ' python  ']
llist= list(map(lambda x: x.strip(), s))
print(llist)