# .py files in python are called as Modules
# 2 types- Built in and User defined
# Built in modules are the modules that are already there in Python and are used by importing them
# eg: random, math, keyword, copy, datetime....
# finding sqaureroot of a number using function in math module
import math
n=90
res=math.sqrt(n)
print(f"The square root of {n} is {round(res,2)}")

# Importing a function within a module can be done in 2 ways
# i) Importing module, then importing a function from that module
# import module
# res= module.function_name(arg1, arg2...)
# ii) Importing a function directly from a certian module, without importing the whole module
# res= from module import function_name(arg1, arg2.....)

# Finding the area and circumference of the circle (importing function directly)
r= 6
from math import pi
Area= pi*(r**2)
Circ= 2*pi*r
print(f"Area of the circle with radius {r} is {round(Area,2)} \nCircumference of the circle is {round(Circ,2)}")
print(round(pi,2))

# Throwing a dice
from random import randint
value=randint(1,6)
print(value)

# We can create alias name for the module that is imported, so that we can start giving easy alias names rather than the big module names
# SYNTAX- import module_name as alias_name
# Lets try alias with datetime module
import datetime as dt
t=dt.time(6,30,50)
print(f"Morning wakeup time is {t}")
