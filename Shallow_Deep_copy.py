# Shallow and Deep copy are only allowed for Mutable datatypes (Lists, Sets, Dictionaries)
import copy

# Shallow and deep copy with Lists
'''L1=[1,2.5,'Rohith',3,[0,2,4,6],'Ravula']
print(L1)
#L2=copy.copy(L1)
L2=copy.deepcopy(L1)
print(L2)
L1[1]=10.0
L1[-2][2]=20
print(f"L1 is: {L1}", id(L1))
print(f"L2 is: {L2}", id(L2))

#Shallow and Deep copy with Dictionaries
d1={'id':1259960, 'Name':'Rohith', 'Marks':{'sem1':460,'sem2':450}}
print(d1)
#d2=copy.copy(d1)
d2=copy.deepcopy(d1)
print(d2)
d1['Name']='Ravula'
d1['Marks']['Sem2']=480
print(f"d1 is: {d1}", id(d1))
print(f"d2 is: {d2}", id(d2))'''

#Shallow and deep copy with sets
S1={20,4.5,'Ravula',20,'Wow',10,30,'Wow'}
print(S1, id(S1))
#S2=copy.copy(S1)
S2=copy.deepcopy(S1)
print(S2, id(S2))
S1=list(S1)
print(f"List of S1 is: {S1}", id(S1))
S2=list(S2)
print(f"List of S2 is: {S2}", id(S2))
S1[-2]=100
S1[2]='Rohith'
print(f"S1 is: {S1}", id(S1))
print(f"S2 is: {S2}", id(S2))
S1=set(S1)
S2=set(S2)
print(f"Set S1 is: {S1}", id(S1))
print(f"Set S2 is: {S2}", id(S2))

