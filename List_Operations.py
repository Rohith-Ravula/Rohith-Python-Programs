#Numerical operations in Lists
'''l1=[2,5,7,1,9,15,12,-5,23,6]
# Smallest number in the list ( min() )
print(f"Smallest number is: {min(l1)}")
# Biggest number in the list ( max() )
print(f"Largest number is: {max(l1)}")
# Sum of elements in the list ( sum() )
print(f"sum of all the numbers in the list is: {sum(l1)}")

# Nested List-> List inside a list
l1=[9,4.7,"Rohith",True,None,[1,4,7,"Ravula",False],0,45]
#print(len(l1))
#n=(l1[-3])
#print(n)
print(l1[-3][-2])'''

l2=[[2,4.5,"At"],[False,8.8,3],[3.14,7,["Yes",12.9],None],[10.0,"No",25,[11,12,[45,True]],["Rohith"]],[0,1,2]]
print(f"The elements of the list are below:\n{l2}")
print(len(l2))
print(len(l2[-2]))
print(l2[-2][-2][2][-1])