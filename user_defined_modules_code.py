# We have already created a user defined module using operations.py file
# lets test it
# import operations
# a=8
# b=3
# res1=operations.power(a,b)
# print(f"{a} to the power of {b} is {round(res1,2)}")
# res2=operations.square_root(a)
# print(f"square root of {a} is {round(res2,2)}")
# res5=operations.square_root(b)
# print(f"square root of {b} is {round(res5,2)}")
# res3=operations.divide(b,a)
# print(f"result of {b}/{a} is {round(res3,2)}")
# res4=operations.mul(a,b)
# print(f"multiplication of {a} and {b} is {res4}")

a=16
b=5
from operations import divide
print(divide(a,b))
out1=divide(b,a)
print(f"{b}/{a} is {round(out1,2)}")
from operations import square_root
print(f"square root {a}/{b} is {round(square_root(a/b),2)}")

print(f"__name__ value in operations.py is {__name__}")