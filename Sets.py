# Sets are non-sequential collection of data types enclosed within curly {} brackets
# Sets are non-sequential bcz the indexing is not allowed in them
# Sets don't allow the duplicate elements i.e even if the same element given more than once, it will only be considered once
set1={30,45.3,'Rohith',True,None,30,'Ravula',45.3,None,True}
print(set1)
print(len(set1))
#print(set1[2])
#print(set1[0:4:1])
#set1.append('Ravula')
##print(set1)
#set1.extend({'Home','Rent'})
#print(set1)
set1.remove(None)
print(len(set1), set1)
set1.clear()
print(len(set1), set1)

