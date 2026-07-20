# def func():
#     '''
#     This is a docstring
#     We can write anything what function does here
#     :return: None
#     '''
#     return None
# print(func())
# print(help(func))

def divide(n1,n2):
    '''
    We will divide two numbers n1, n2
    :param n1: n1 is the numerator
    :param n2: n2 is the denominator
    :return: float
    '''
    if n2==0:
        print("Cannot divide as n2 is 0")
    else:
        return n1/n2
divide(10,7)
print(divide(10,7))
print(f"Division of n1 and n2 is {round(divide(10,7),2)}")
help(divide)
