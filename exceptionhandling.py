x= int(input("Enter the number: "))
try:
    res= 100/x
except ZeroDivisionError:
    print("DONOT INPUt 0")
except ValueError:

    print("Value error")

else:
    print(res)
finally:
    print("Proggram TErminated")