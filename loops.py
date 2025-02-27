#for loop only used in string or dictionary print each chaarcter .

#print the sqaure of each number in the list 
"""
num=[1,2,3,4,5]
for mul in num:
    print(f"the list is ",{mul},"and square of list is ",{mul**2})
"""
# for making 100 time loop 
"""
for num in range(0,101): # use range keyword
    print(num**2)
"""
# while loop is used for more loop and also more iteration
"""
i=0
while i<5:
    i=i+1
    #i+=1 both are same 
    print(i)
"""
# print even number from 0 to 10
"""
i=0
while i<=10:
    i+=2
    print(i)
"""
# break used for immdiate break the loop 
"""
for num in range(1, 6):
    if num == 3:
        print("Breaking the loop at", num)
        break
    print(num)
"""
# continue used skips the current iteration of the loop
"""
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue
    print(num)
"""
# game to guess the value 
"""
import random 
secret_number=random.randint(1,10)
guess=0
while not(guess== secret_number):
    guess = int(input("Guess the number:"))
    if guess<secret_number:
        print("The numnber is to low ")
    elif guess>secret_number:
        print("The number is to high")
    else:
        print("Correct")
"""
#OOP
#four pilers of OOP 
# Encapsulatoin: related attributes and functions place in one class 
"""
class cat:
    legs=4
    name= "tiger"
    tail = True
    def meow(self):
        print("Meow ")
    def play(slef):
        print("playing")
    def sleep(self):
        print("sleeping")
# object 
cat1=cat()
cat2=cat()
cat1.play() # function call
print(cat1.legs) # class attribute call 
print(cat2.name)
cat2.sleep()
cat1.meow()
cat1.sleep()
"""
# make a class student having attribute name, student_id , marks
# and method enroll , pay_fees and studing 
"""
class Student:
    name=input("Enter your name")
    student_id=int(input("Enter your roll number "))
    marks=input("enter your marks ")
    def enroll(self):
        print("Enrolled")
    def pay_fees(self):
        print("pay fee ")
    def studying(self):
        print("studying")
student1=Student()
student2=Student()
student1.enroll()
student2.studying()
print(student2.name)
print(student1.student_id)
"""
# use of self keyword 

#class is called blue  print it's instruction
"""
class dog:
    name="mani" 
    def bark():
        print("Bark")
    def sleep(self):# self is used to access the objects attribute in the class 
        print("sleep")
    def eating(self):
        name="bully"
    print("Eating")    
dog1=dog()
dog1.bark()
dog1.eating()
"""
"""
class Student:
    name=input("Enter your name")
    student_id=int(input("Enter your roll number "))
    marks=input("enter your marks ")
    def enroll(self):
        print("Enrolled")
    def pay_fees(self):
        print("pay fee ")
    def studying(self):
        print("studying")
    def display(self):
        print(self.name,self.student_id,self.marks)
student1=Student()
student2=Student()
#student1.enroll()
#student2.studying()
print(student2.name)
print(student1.student_id)
student1.display()
"""

"""
class Cat:
    def __init__(self,l,t,n): # constructor
        self.legs=l
        self.tail=t
        self.name=n
    def meow(self):
        print("meow")
    def sleep(self):
        print("sleeping")
    def display(self):
        print(f"name:{self.name},legs: {self.legs}, tail{self.tail}")
cat1=Cat(4,True,"tiger")
cat2=Cat(3,False,"Cat")

cat1.display()
cat2.display()
"""
        

