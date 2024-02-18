import math


var = input("enter something:")

try:
    if math.sqrt(int(var)):
        print('Nmber')
except ValueError:
    print(var)



# var = input("Enter number= ")
# # exception handling
# # try clause
# if math.sqrt(int(var)):
#     print('Nmber')

# else:
#     print("Please enter numerical values only! Not alphabets!")


