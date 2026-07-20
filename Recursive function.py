# Recursion is a process in which a function calls itself as long as a specific condition is met.
# Recursion stops only when the condition is fail to meet.
# Factorial (n!= n*(n-1)*(n-2)*(n-3)*....*2*1)
# Factorial program without Recursion
# def factorial(n):
#     if n==0:
#         print(f"Factorial of {n} is {n}")
#     else:
#         fact=1
#         while n>1:
#             fact*=n
#             n-=1
#         return fact
# a=int(input("Enter a number: "))
# print(f"Factorial of {a} is {factorial(a)}")

#Factorial using Recursive function
# (n!= n*(n-1)*(n-2)*(n-3)*....*2*1)
# n!= n* (n-1)!
# n! = n* (n-1)* (n-2)!
def fact_rec(n):
# Base/ Terminal condition
    if n==1:
        return 1
    else:
# Recursive condition
        factorial=n*fact_rec(n-1)
        return factorial
b=int(input("Enter a number: "))
print(f"Factorial of {b} is {fact_rec(b)}")




