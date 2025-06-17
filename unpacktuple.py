#we can unpack the items in list too same as tuples
mytuple=  ("apple", "banana", "pineapple")  
(fruit1, fruit2, fruit3)= mytuple
print(fruit1)
print(fruit2)
print(fruit3)

#if the no. of variable is not equal to no. of items in tuple we use *
(fruits1, *fruits2)= mytuple
print(fruits1)
print(fruits2)  #it will assign the remaining items in list


'''
If the asterisk is added to another variable name than the last,
Python will assign values to the variable until the number of values left matches the number of variables left.
'''

mytuple1= ("apple", "banana", "mango", "orange", "litchi")
(*var1, var2 ,var3)=  mytuple1
print(var1)
print(var2)
print(var3)

(var1, *var2 ,var3)=  mytuple1
print(var1)
print(var2)
print(var3)