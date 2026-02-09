#Operations in two sets
'''setA={1,2,3,6,7}
setB={0,2,9,5,6}
print(setA|setB)
print(setA&setB)
print(setA-setB)
print(setB-setA)
print(setA^setB)


Set_Inter=setA.intersection(setB)
print(f"Intersection of A and B is: {Set_Inter}")
Set_Union=setA.union(setB)
print(f"Union of A and B is: {Set_Union}")
set_Diff1=setA.difference(setB)
print(f"Diff of A-B is: {set_Diff1}")
set_Diff2=setB.difference(setA)
print(f"Diff of B-A is: {set_Diff2}")
set_Symdiff=setA.symmetric_difference(setB)
print(f"Symmetric difference of A and B is: {set_Symdiff}")'''

# Operations in 3 sets
setA={4,5,2,8,10}
setB={3,6,8,5,9}
setC={1,0,8,10,9}
print(setA | setB | setC)
print(setA & setB & setC)
print(setA ^ setB ^ setC)
print(setA^(setB^setC))
print(setA^setC^setB)
print(setA-setB-setC)
print(setA-(setB-setC))
print(setC-setA-setB)

Set_Union=setA.union(setB,setC)
print(f"Union of A,B,C is: {Set_Union}")
Set_Inter=setA.intersection(setB,setC)
print(f"Intersection of A,B,C is: {Set_Inter}")
set_Diff1=setA.difference(setB,setC)
print(f"Diff of A-B-C is: {set_Diff1}")
set_Diff2A=setB.difference(setC)
set_Diff2=setA.difference(set_Diff2A)
print(f"Diff of A-(B-C) is: {set_Diff2}")
set_Diff3=setC.difference(setA,setB)
print(f"Diff of C-B-A is: {set_Diff3}")
set_symdiff1=setC^setA^setB
print(f"Symmetric difference of A,B,C is: {set_symdiff1}")