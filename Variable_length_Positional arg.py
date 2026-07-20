# Variable length Positional arguments (*args)
def add(*args):
    return sum(args)
res=add(1,2,3,4,5)
print(res)

def add (*args):
    print(args, type(args))
add(1,2,3,4,5)

def student(sname, sid, *marks):
    if len(marks)==0:
        print(f"{sname} with id {sid} was absent in all the exams")
    else:
        percent=sum(marks)/len(marks)
        print(f"{sname} with id {sid} has secured {round(percent,2)}%")
student("Rudhvika",105,92.5,87.8,96.4,89.9,97.5)
student("Rudhransh",109,87.8,92.3,95.6,90.0,86.4,93.5)
student("Rohith",112)
student("sathwika",116,66.8,70.3,83.5,68.9)
student("Uma",118,78.7,85.6,74.4,82.5)
