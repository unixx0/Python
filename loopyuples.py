#to access indivisual data in tuples using loop

mytuple= (1,2,3,4,5,)
for x in mytuple:
    print (x)

#another way
for i in range(len(mytuple)):
    print(mytuple[i])


#using while loop
i= 0    #initialization
while i<len(mytuple):
    print(mytuple[i])
    i+=1

