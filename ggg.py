
class abcde:
    pass
def divide(a, b):
    if b== 0:
        raise abcde ("abcdee")
    print(a/b)


try:
    divide(5, 0)
except abcde as e:
    print(e)