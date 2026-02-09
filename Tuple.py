'''t1=(10,3.14,"Rohith",True,[1,3,5],(2,4,6),47,None)
print(len(t1))
print(t1[0:8:2])
print(t1[0:8:1])

t2=10,20,30,40
print(t2)
print(type(t2))

t3=10,5.6,"Ravula",True,[1,3,9],(2,4,12),47,None
print(t3)
print(type(t3))

#Typecasting in tuple
l1=[2,3,5,7]
print(l1, type(l1))
t1=tuple(l1)
print(t1, type(t1))
print(l1, type(l1))

t2=("Ravula","Rohith","Uma","Rudhvika","Rudhransh")
print(t2, type(t2))
l2=list(t2)
print(l2, type(l2))
print(t2, type(t2))

t3=("Ravula","Rohith","Uma","Rudhvika")
# If Rudhransh need to be added to above items, change the tuple to list and later use append()
print(t3, type(t3))
t3=list(t3)
print(t3, type(t3))
t3.append("Rudhransh")
print(t3)
t3.extend(["Rajasambaiah","Vanamala"])
print(t3)'''

t4='Rohith', 'Uma', 'Rudhvika', 'Rudhransh'
print(t4, type(t4))
l4=list(t4)
print(l4, type(l4))
l4.insert(0,'Ravula')
print(l4)

