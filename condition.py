#Indentation
"""
age=12
if age>=18:
    print("Eligibal for vote")
print("Indentatoin ")# because it is out of the if body.
"""
#taking the value from user 
"""
age=12
if age>=18:
    print("Eligibal for vote")
print("Indentatoin ")# because it is out of the if body.
marks=input()
print("Enter your age ",marks)
"""
#for converting the input value into string to int or int to float deped on the input given by the user.
#it is call typecasting 
"""
mark="45"
mark_int=int(mark)
print(mark_int)
print(type(mark_int))
"""
#if and elif condition 
"""
temprature=45
if temprature>45:
    print("Temprature is too hot ")
elif temprature<0:
    print("Temprature is too cold")
else:
    print("temprature is normal")
print("temprature is ",temprature)
"""
# function 
"the code can easily used"
#these are called dynamic function 
"""
def sum_dynamic_value(m,n):
    sum_reult=m+n
"""

# write a program that take a color as input and prints and action:
"""
color=str(input("Enter your Color name"))
if color=="Red":
    print("stop")
elif color=="Yellow":
    print("Get ready ")
elif color=="Green":
    print("Go")
else:
    print("Invalid color")
"""
#write a program that check whether a person is eligible for loan or not based on the following condition:
#1- Age should be between 25 and 60 
#2- Income should be greater than 50000
#if both condition true print "Eligible for loan"
#else print "Not Eligibal"

age=int(input("Enter Your age "))
Income=int(input("Enter income "))

if age>=20 and age<=60 and Income>=50000:
    print("Eligible for loan ")
else:
    print("Not eligible for loan ")

# Pass is used for error handling
"""
if age<20:
    pass
"""