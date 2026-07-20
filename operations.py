'''
This is used to write some basic math arithmetic operations
'''
def divide(a,b):
    return a/b
def square_root(a):
    return a**0.5
def power(a,b):
    return a**b
def mul(a,b):
    return a*b

if __name__=="__main__":
    a=5
    b=4
    print(f"{a} to the power of {b} is {power(a,b)}")