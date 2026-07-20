"""Principle (P) is the Amount given
Time  (T) is amount of Time period
Rate of Interest is R
Simple Interest(SI)= (P*T*R)/100"""
P= float(input('Enter the Principle amount: '))
T= float(input('Enter the Time period: '))
R= float(input('Enter the Rate of Interest: '))
SI= (P*T*R)/100
TA= SI+P
print(f"Interest amount for the time period is {round(SI,2)}")
print('Total Amount to be given back is',round(TA,2))