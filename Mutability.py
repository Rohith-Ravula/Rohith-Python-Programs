#Mutability is the ability of a data to get changed or modified
#Immutability is the inability of a data to get changed or modified
#Lists are mutable (Lists get modified when we use some functions like append(), insert(), extend()). Here the lists get modified and the o/p is stored in the same list
#Strings and Tuple are Immutable (They can't be modified using external functions)
# Strings are modified using replace(), but the o/p always be stored in a separate string (i.e Memory address is changed)
"""s1='Rohith is my name'
print(s1)
print(id(s1))
s2=s1.replace('Rohith','Ravula')
print(s1)
print(s2)
print(id(s2))
print(id(s1))"""

l1=['Rohith','Ravula','Achyuth']
print(l1)
#print(id(l1))
l1.extend(['Mash','Rahul'])
print(l1)
#print(id(l1))
l1[-2]='Mahesh'
print(l1)

t1=('Rohith','Ravula','Ahuth')
print(t1)
#print(id(l1))
#print(id(l1))
t1[-1]='Achyuth'
print(t1)