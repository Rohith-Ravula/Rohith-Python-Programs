#Positional Arguments
def add(a,b,c):
    print(f"a:{a},b:{b},c:{c}")
    return a+b+c
result=add(1,2,3)
print(result)

# Default arguments
def add(a,b=10):
    print(f"a:{a},b:{b}")
    return a+b
result=add(20)
print(result)

# def add(a,b=5,c):
#     print(f"a:{a},b:{b},c:{c}")
#     return a+b+c
# result=add(20,15,10)
# print(result)

def add(a,c,b=5):
    print(f"a:{a},b:{b},c:{c}")
    return a+b+c
result=add(20,15)
print(result)
#
def add(a,c,b=10):
    print(f"a:{a},b:{b},c:{c}")
    return a+b+c
result=add(10,5,15)
print(result)

def add(a,b=15,c=10):
    print(f"a:{a},b:{b},c:{c}")
    return a+b+c
#Keyword Argument- Using this we can only pass the values to the argument which we intended to give, that means we can ignore the order and can pass the value to the intended argument
result=add(10,c=20)
print(result)

def add(a=4,b=15,c=10):
    print(f"a:{a},b:{b},c:{c}")
    return a+b+c
result=add()
print(result)

