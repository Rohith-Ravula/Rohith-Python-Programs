#Using Lambda function we can write both the argument and code expression in the same line
# SYNTAX- Function= lambda argument : expression
# def mul(x):
#     return x*4
# res= mul(4)
# print(res)
#
# def diff(x,y):
#     return x*y-y
# res=diff(3,7)
# print(res)
#
# # Using Lambda
# func=lambda x:x*4
# res=func(4)
# print(res)
#
# func=lambda x,y:x*y-y
# res=func(3,7)
# print(res)

# i) filter()- filter function takes function as the 1st argument and sequence as the second argument
# using filter() we can filter out the elements in a sequence for which the function is true
# We can use lambda function to write the logic of the function(1st argument) for filter()
# SYNTAX- filter(function, sequence)
# If we need to filter out the even elements from a sequence and leave the odd elements using filter()
seq=[1,2,3,4,5,6,14,17,12,15,13,22]
even=lambda a: True if a%2==0 else False
output=filter(even,seq)
print(output)
print(f"even numbers from the sequence {seq} are {list(output)}")

# ii) map()- map function takes function as the 1st argument and sequence as the second argument
# SYNTAX- map(function, sequence)
# map() function show o/p as True or False for the o/p
seq=[1,2,8,11,18,23]
map_output=map(lambda x: True if x%2!=0 else False,seq)
print(map_output)
print(list(map_output))

seq=[2,4,5,7,8,9]
map_output=map(lambda y: y**2,seq)
print(f"sqaures of the numbers from the sequence are {list(map_output)}")

