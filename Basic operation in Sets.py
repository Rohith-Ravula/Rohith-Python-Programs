'''set1={6,67.8,'Rohith',True,'God',67.8,6,'God'}
set2={9.5,'Ravula',10,False,None}
print(set1, len(set1))
print(set2, len(set2))
#Membership operator (in & not in)
print('God' in set1)
print(False not in set1)
print(True in set2)

#Concatenation in sets is not allowed
#print(set1+set2)

#Typecasting in sets
print(type(set1))
set1=tuple(set1)
print(set1, type(set1))
print(set1[0:8:1])
print(len(set1))
print(set1[1:5:2])'''

# Are sets Mutable or immutable
set1={0,1,2,3}
print(set1)
print(id(set1))
set1.remove(3)
print(set1)
print(id(set1))
# Here the
# This means the modified values are stored in the original set. Set has been changed permanently.
memory address remains the same even after the modification.
set1.add(4)
print(set1)
print(id(set1))

set1.discard(0)
print(set1)
print(id(set1))
set1.discard(10)
print(set1)
print(id(set1))
set1.clear()
print(set1)
print(id(set1))
print(len(set1))
#Memory address remains the same even after the modification. Hence, sets are Mutable