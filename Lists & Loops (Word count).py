Country=['India','US','China','Italy','Japan','Ireland','UK','Iran','SA','Iceland','Russia','Iraq']
# Countries starting with 'I' should be counted (O/P should be 6 Countries)
# We have to count the country, so we need a count variable and it's value should be Zero before counting starts
# count=0
# for C in Country:
#     #if C[0]=='I':
#     if C.startswith('I'):
#         count+=1    #(count=count+1)
# print(f"{count} countries starting with letter 'I'")

# Along with counting the 'I' letter countries, we also need to print those countries in a separate List?
# To print the countries in a separate List we need a new list which is empty at the beginning.
count=0
Output=[]
for C in Country:
    if C.startswith('I'):
        Output.append(C)
        count+=1
print(f"{count} countries starting with letter 'I' listed a below")
print(Output)

