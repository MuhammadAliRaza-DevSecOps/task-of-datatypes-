 # python .\datatypes.py (. is the current folder and /datatypes.py is the file )
"""test='hello world' #array of charcter /list of chars"""
# int
"""
x=45  
y=43
"""
# string
"""x="Ali Raza" """

# float 
"""z=2.5"""

# boolean
"""a=True 
b=False

result=x/y
print(result,a)"""

#Task in class
#area of Triangle
"""
base=10 
height=45
area=(1/2)*base*height
print("Area of the triangle:" ,area)"""


#area of circle.

"""
Radius=5

pi=3.14159

Area=pi*Radius*Radius
print("Area of the Circle: ",Area)
"""

#  list 
"""students=['ali','usman','uzair']#list
print(students)"""

# tuple 
 #it's also list but it is unmutable


# none 
"""test=None"""
# undefine    

# dictionary
"""student_1 = students[0]78

student_2 = students[1]

student_3 = students[2]"""

# concatenation
"""test = 'hello '+'world'

student_1["name"]
student_1["age"]
student_1["email"]

print(student_1.name, student_1["email"], student_1["age"])

student_1 = {
    "name": "ali",
    "age": 21,
    "email": "test@example.com"
}"""""

#task2
"""test = ['hello', 'world', 'this', 'is', 'me']
test[0]="hey"
test[1]="it's me Ali"
test[2]="How Are you "
test[3]="What's up"
test[4]="Nice to meet you bro"
print(test)"""
#hint = [{'name': 'talha'}, ]

# make a list of student objects
"""students={
    'name':'talha'
}
print(test,students['name'])"""

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


# for chnaging the value of the list 
#suppose
#student[1]="Talha " # it will shuffle the values 

# List of object and access the values 
"""
Student=[
    {"name":"Ali Raza" , "age":20 ,"Subject":"Python"},
    {"name":"Usman" , "age":21,"Subject":"Python"},
    {"name":"Uzair","age":21,"Subject":"C++","marks":[100,86,22]},
    {"name":"Talha", "age":26,"Subject":"JavaScript"}
]
print(Student[2]["marks"][1])
"""
#tuple in python

#student=("ali",20,"Osman","uzair")# immutable 

#using list 
"""
student=["ali","osman","uzair"]
print(student[1])"""
#to add the value in list we use append keyword
"""student.append("ahmad")"""
#to remove last value we use pop
#student.pop()
#to pass  any value in the list we use keyword remove
#student.remove(20)
#to insert the value in the list 
"""student.insert(1,20)"""
#to add list in to the list 
"""student=student+[1,2,3,4,5]
print(student)"""
#to extend or add we use keyword extend 
"""student.extend([456,234,45,804])
print(student)"""
               #Slicing values in the list.
#to print last value 
"""print(student[-1])"""
#to print the sequence from the list 
"""print(student[0:3])"""
#to print the middle value to last 
"""
print(student[2:-1])
"""
#create a new reversed list or reversed name that contain the element in reverse order using slicing and print it .
"""names=["alice","bob","charlie","david"]"""
#two method for reversing
"""names.reverse()
print(names[::-1])
print(names)"""
#multiple coln in the list 
"""print(names[0:8:2])"""# it means first value print due to 0 and after it will cheeck in the 8 values in the list 
#it will remove to number and then print the third value .
#for reversing slicing 
"""print(names[-1:5:-2])"""# -1 means it will start from the end and 5 means it will achive the value 5th and
#-2 means it will remove every 2 element

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
"""
age=int(input("Enter Your age "))
Income=int(input("Enter income "))

if age>=20 and age<=60 and Income>=50000:
    print("Eligible for loan ")
else:
    print("Not eligible for loan ")
"""
# Pass is used for error handling
"""
if age<20:
    pass
"""
