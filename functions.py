# Syntax
# def Function_name(arg1, arg2,....argN):
#     print(arg1)
#     print(arg2)
#     .....
#     print(argN)
# Calling a function
#Function_name("arg1")
#Function_name("arg2")


# def greet_someone(name):
#     print(f"Hi {name}, Good morning!")
#     print(f"Have a Great Day!")
#
# # Calling a function.
# greet_someone("Rudhvika")
# greet_someone("Rudhransh")
# greet_someone("Rohith")
# greet_someone("Laharika")

# def odd_even(num):
#     if num%2 == 0:
#         # print(f"{num} is even")
#         return f'{num} is Even'
#     else:
#         # print(f"{num} is odd")
#         return f'{num} is Odd'
# result=odd_even(5)
# print(result)
# odd_even(34)
# odd_even(79)
# odd_even(60)

#Addition of 3 numbers
# def add(num1,num2,num3):
#     result=num1+num2+num3
#     return result
# a=int(input("enter num1:"))
# b=int(input("enter num2:"))
# c=int(input("enter num3:"))
# Val=add(a,b,c)
# print(Val)

# Multiple operations using Functions:
def operations(n1,n2,n3):
    add=n1+n2+n3
    sub=n1-n2-n3
    mul=n1*n2*n3
    div=n1/n2/n3
    mod=n1%n2%n3
    return add,sub,mul,div,mod
#calling a function
a=int(input("enter n1: "))
b=int(input("enter n2: "))
c=int(input("enter n3: "))
res1, res2, res3, res4, res5=operations(a,b,c)
print(f"Addition of {a},{b} & {c} is: {res1}")
print(f"Substration of {a},{b} & {c} is: {res2}")
print(f"Multiplication of {a},{b} & {c} is: {res3}")
print(f"Division of {a},{b} & {c} is: {res4}")
print(f"Modulo of {a},{b} & {c} is: {res5}")



