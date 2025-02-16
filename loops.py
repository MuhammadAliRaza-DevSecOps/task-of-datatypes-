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

#OOP
#four pilers of OOP 