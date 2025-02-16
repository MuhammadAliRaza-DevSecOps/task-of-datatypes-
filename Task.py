#Task 1
#area of circle.
"""r=5
PI=3.14159
Area=PI*r**2
print("Area of the Circle: ",Area)"""

#Task 2
# make a list of student object 

"""Student=[
    {"name":"Ali Raza" , "age":20 ,"Subject":"Python"},
    {"name":"Usman" , "age":21,"Subject":"Python"},
    {"name":"Uzair","age":21,"Subject":"C++"},
    {"name":"Talha", "age":26,"Subject":"JavaScript"}
]
print(Student)
#using dictionary OR Array 
print(Student[0])
print(Student[1])
print(Student[2])
print(Student[3])"""

#Task 3
# 1- Write a program to swap the values of two variables 
"""
x=70 #value initiazing number 
y=34
print("The Variables Before swapping ",x , y )
temporary_variable=y   #it's a temporary variable that store the value of y 
y=x                    # now we are assigning the value of x to y 
x=temporary_variable   # And here  we are assigning the value that hav been store in temporary variable to x 
print("Variables after Swapping ",x , y) """


# 2-Write a program to convert temprature from Celsius to Fahrenheit and vice versa.
"""
F=32
C=45
F=(C*9/5)+32
print("The value is in Fahrenheit", F)
C=(F*5/9)-32
print("The value is in Celsius ", C)
"""
# 3- Assign the values 10,20 and 30 to variable p,q,r in a single line.
"""
p,q,r=10,20,30
print(p)
print(q)
print(r)
"""

# 4- Swap the values of three variables x,y,z such that x takes the value of y and y takes the value of z and z takes the value of x.
"""
x=802
y=803
z=804
x,y,z=y,z,x
print("the values after swaping is :", x ,y ,z )
"""

#Task 4

# 1-Write a program to calculate the distance traveled by the car moving at the speed 60km/h for 2.5 hours 
"""
speed=60
time =2.5
distance=speed*time 
print("The distance of car is:", distance,"km")
"""

# 2- Write program to calculate the  simple interest for a principal amount of $1000 ,a rate of 5% annually ,and a time period of 3years
"""
Principal_Amount=1000
Rate=5
Time=3
Interest=Principal_Amount*Rate*Time/100
print("The amount of interest is :",Interest ,"$")
"""

# 3- Write a program to Calculate a person's age in years ,month and  days given their birthdate.
"""
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
current_year = 2025
current_month = 2
current_day = 11
years = current_year - year
months = current_month - month
days = current_day - day
print("Your age is", years, "years,", months, "months, and", days, "days.")
"""
#take a input from user and check whether it is positive or negative and print it
"""
mark=int(input("Enter Your number"))
if mark>=0:
    print("It is positive ")
else:
    print("Negative nnumber ")
print(mark)
"""

#input from  user and check wehter it is even or odd.
"""
num=int(input("Enter the number:"))
if num%2==0:
    print("number is even ")
else:
    print("Number is odd")
print(num)
"""
# make a function 4
"""
def main():
    
    a =int(input("Enter yourn number "))
    b = int(input("Enter Second Number"))

    return [a, b]

x, y = main()

def add(m,n):
    addition_value =m+n
    print(addition_value)
add(x, y)

def Multiplication(m,n):
       multiply_value=m*n
       print(multiply_value)
Multiplication(x,y)
def division(m,n):
       divide_value=m/n
       print(divide_value)

division(x,y)
def Subtraction(m,n):
       subtract_value=m-n
       print(subtract_value)

Subtraction(x,y)
def remainder(m,n):
       remainder_value=m%n
       print(remainder_value)

remainder(x,y)
"""
