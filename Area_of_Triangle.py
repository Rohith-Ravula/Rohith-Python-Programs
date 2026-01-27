"""When all the 3 sides of a Triangle is known
Perimeter(P)= a+b+C
Semi-Perimeter(S)=(a+b+c)/2
Area(A)=Square root of (s*(s-a)*(s-b)*(s-c)) """

a=float(input("Enter the length of first side of Triangle: "))
b=float(input("Enter the length of second side of Triangle: "))
c=float(input("Enter the length of third side of Triangle: "))
S= (a+b+c)/2
A= S*(S-a)*(S-b)*(S-c)*0.5
print('Perimeter of the Triangle is',2*S,'Area of the Triangle is', round(A,2))