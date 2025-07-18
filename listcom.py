fun= lambda x: print("positive") if x>0 else print("Negative") if x<0 else print("zero")
fun(5)


l= lambda x, y: [x+y, x-y]
print(l(1,2))