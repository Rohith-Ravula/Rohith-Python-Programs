user={'Name':'Rohith','Age':29,'Address':'H.No: 2-18, Nagaram','Aadhar':759872670393,'Job':'Corporate'}
sensitive_info=['Address','Aadhar','Phone No:','Married?']
# i) Running for loop on a dict and delete the same dict keys (fetches error)
# for i in user:
#     if i in sensitive_info:
#         user.pop(i)
# print(user)

# ii) Running for loop on List and deleting keys from dict based on the items present in List? (works)
# for i in sensitive_info:
#     if i in user:
#         print(f"Deleted=> key:{i}, value:{user[i]}")
#         user.pop(i)
# print(f"New Dict is {user}")

# iii) What if an item in a List to be deleted which is not present in dict?
for i in sensitive_info:
    if i in user:
        print(f"Deleted=> key:{i}, value:{user[i]}")
        user.pop(i)
    else:
        print(f"Key '{i}' not in user, cannot be deleted")
print(f"New Dictionary is {user}")