# # To print a Star pattern of 7 rows.
#
# # print(f"Welcome to Star pattern, please select the number of rows for your Star")
# # n=int(input("Enter a number: "))
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# # Mirror of Normal star.
# for i in range(1,6):
#     print(" "*2*(5-i),end="")
#     for j in range(i):
#         print('*',end=' ')
#     print()
#
#
# # Inverted triangle
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*', end=" ")
#     print()
#
# # Mirror of Inverted triangle
# for i in range(5,0,-1):
#     # Spaces
#     print(" "*2*(5-i),end="")
#     for j in range(i):
#         print('*', end=" ")
#     print()

# To print a Pyramid pattern of 5 rows
# for i in range(1,6):
#     # spaces
#     print(' '*(5-i),end='')
#     for j in range(i):
#     # stars
#         print('*',end=' ')
#     print()
#
# # To print a Inverted Pyramid of 5 rows
# for i in range(5,0,-1):
#     # spaces
#     print(" "*(5-i),end='')
#     for j in range(i):
#     # stars
#         print('*',end=' ')
#     print()
#
# # To print a Grid Pyramid of 5 rows
# for i in range(0,5):
#     # spaces
#     print(' '*(4-i),end='')
#     for j in range(2*i+1):
#     # stars
#         print('*',end='')
#     print()
#
# # To print a Inverted Grid Pyramid of 5 rows
# for i in range(5,0,-1):
#     # spaces
#     print(' '*(5-i),end='')
#     for j in range(2*i-1):
#         print('*',end='')
#     print()

# To print a diamond- 5 rows
# for i in range(1,6):
#     print(' '*(5-i),end='')
#     for j in range(i):
#         print('*',end=' ')
#     print()
# for i in range(4,0,-1):
#     print(' '*(4-i),end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()

# To  print a Grid diamond Pattern- 5 rows
# for i in range(0,5):
#     print(' '*(4-i),end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()
# for i in range(4,0,-1):
#     print(' '*(5-i),end='')
#     for j in range(2*i-1):
#         print('*',end='')
#     print()

# To print a n*n square.
n=int(input('Enter a number: '))
for i in range(1,n+1):
    for j in range(n):
        print('*',end=' ')
    print()



