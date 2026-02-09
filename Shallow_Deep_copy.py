# Shallow and Deep copy are only allowed for Mutable datatypes (Lists, Sets, Dictionaries)
import copy

'''L1=[1,2.5,'Rohith',3,[0,2,4,6],'Ravula']
print(L1)
#L2=copy.copy(L1)
L2=copy.deepcopy(L1)
print(L2)
L1[1]=10.0
L1[-2][2]=20
print(f"L1 is: {L1}", id(L1))
print(f"L2 is: {L2}", id(L2))'''

d1={'id':1259960, 'Name':'Rohith', 'Marks':{'sem1':460,'sem2':450}}
print(d1)
#d2=copy.copy(d1)
d2=copy.deepcopy(d1)
print(d2)
d1['Name']='Ravula'
d1['Marks']['Sem2']=480
print(f"d1 is: {d1}", id(d1))
print(f"d2 is: {d2}", id(d2))