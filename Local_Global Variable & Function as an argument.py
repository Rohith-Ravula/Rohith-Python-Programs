#Local and Global Variable
# Local- inside a specific function
# Global- outside the function, accessed allover the code
# Always Local variable has the highest priority-> Local variable specified in output first, then comes the Global
n=3
print('out', n)
def func():
    global n
    n=5
    print('in', n)
func()
print('out', n)

# Function as an argument
# In Python we can pass i) value as an argument to other function and ii) Function as an argument to the other function
def add_1(n):
    return n+1
def Sq(n):
    return n**2
x=int(input("Enter a number: "))
res=Sq(add_1(x))
print(f"Adding 1 to {x} and squaring the result is {res}")