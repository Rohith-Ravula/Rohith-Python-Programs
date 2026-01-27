"""Principle (P) is the Amount given
Time  (T) is amount of Time period
Rate of Interest is R
Total Amount(TA)= P*(1+R/100)**T
Compound Interest (CI)= TA-P"""
P= float(input('Enter the Principle amount: '))
T= float(input('Enter the Time period: '))
R= float(input('Enter the Rate of Interest: '))
# TA= P*(1+R/100)**T
TA= P* pow(1+R/100,T)
CI= TA-P
print('Compound Interest for given amount', round(CI,2), 'Total Amount to be paid', round(TA,2))