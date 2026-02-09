#Dictionaries are a sequence of Key-value pairs seperated by comma enclosed within a curly brackets
#Each key-value pairs are seperated by a colon in between them
d1={'Milk':40,'Chicken':200,'Beers':500,'Fruits':250,'chocs':50}
'''print(d1, type(d1), len(d1))
print(d1['Beers'])
print(id(d1))

#Dictionaries are Mutable-> We can add or delete or update the values in the dictionary
d1['Beers']=900
print(d1)
print(id(d1))

print(d1['chocs'])
print(d1.get('chocs'))
#print(d1['Bikkis'])
print(d1.get('Bikkis'))

print(d1.get('Bikiis', 20))
print(d1.get('Chicken', 20))

#Membership (in or not in)
print(200 in d1)
print('Chicken' in d1)
print(200 not in d1)
print('Bikkis' in d1)
print('Bikkis' not in d1)

print(d1)
#Update
d1['Bikkis']=20
print(d1)

#delete
del(d1['Beers'])
print(d1)

sem1={'M1':95,'Eng':89,'M2':93,'Phy':92,'Chem':94}
sem2={'Sans':97,'Eng':92,'CS':91,'Java':92}
print(sem1)
print(sem2)
print(sem1['Phy'])
print(sem2.get('Java'))
print(sem2.get('Python',93))
print(sem2.get('AWS'))
print(sem1.get('M2',95))
print(sem1)
print(sem2)
#sem1.update(sem2)
#print(sem1)
#print(sem2)
sem2.update(sem1)
print(sem1)

List1={'Milk':30,'Rice':90,'Eggs':72,'Bread':40}
List2={'Chicken':240,'Milk':40,'Eggs':78}
print(List1)
print(List2)
#List1.update(List2)
#print(List1)
#print(List2)
#List2.update(List1)
#print(List2)
#print(List1)

#del(List1['Milk'])
#print(List1)
#del(List1['Meat'])
#print(List1)

#List1.pop('Milk')
#print(List1)
#List1.pop('Meat')
#print(List1)

List3={'Milk':40,'Rice':90,'Eggs':72,'Milk':30}
print(List3)

# Keys can only be Immutable datatypes
# Allowed datatypes as keys=> int,float,Bool,str,tuple
# Not Allowed datatypes as keys=> list,set,dict
#d1={1:{1,2,3},2:{4,5,6},3:{7,8,9}}
#print(d1)
# values can be any datatypes
d1={1:1,2.0:1,3:4.0,True:1,0.0:False,"Rohith":45,(1,2,3):'Ravula',100.0:[6,7,8],'Marks':(90,94,96),(11,13,15):{23,27,29},'Grade':{'Math': {'sem1':90,'sem2':94,'sem3':96},'Eng':89,'CS':91}}
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
print(type(d1))
print(d1[100.0][-1])
print(['Marks'][0])
print(d1['Grade']['CS'])
print(d1['Grade']['Math']['sem2'])'''

d1={'id':1,'Coll':'kits','Year':[1,2,3,4],'Grade':(9.0,9.7,9.4),'Marks':{'Sem1':{'Maths':95,'Python':90,'Eng':85},'sem2':264}}
print(d1['Grade'][2]) #1st function
print(d1['Year'][-2])
print(d1['Marks']['Sem1']['Python']) #2nd function
print(d1.keys(), type(d1.keys()))
print(d1.values(), type(d1.values()))
print(d1.items(), type(d1.items()))





