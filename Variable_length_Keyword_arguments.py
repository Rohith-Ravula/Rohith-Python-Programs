# **kwarg is used in function definition while using Keyword arguments
# The output for kwarg is stored in a dictionary
def func(**kwarg):
    print(kwarg, type(kwarg))
func(x=5, y=10, z=12)

def func(**kwarg):
    print(kwarg, type(kwarg))
func()

def stu_details(sname, sid, *interest, **marks):
    if len(marks)== 0:
        print(f"{sname} with id {sid} was absent to all the exams")
    else:
        percent=sum(marks.values())/len(marks)
        print(f"{sname} with id {sid} has secured {round(percent,2)}% ")
        print(f"{sname} subject wise marks are {marks}")
    print(f"{sname} has also interest in {interest} and does well in that field")
stu_details('Rudhvika', 101,'Bharatanatyam', 'Singing','Art', Eng=93.6,Maths=94.4,Phy=90.1,Che=95.7,Bio=86.9)
stu_details("Rudhransh", 104, 'Cricket','Dancing', Hindi=88.7,Maths=97.5,Eng=93.8,GK=84.6)
stu_details("Rohith", 108,'Cricket','Drinking')