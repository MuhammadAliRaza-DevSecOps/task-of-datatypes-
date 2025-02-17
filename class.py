#variables(value store) 
x=45
y=10
# Arithmatic operators 
sum_result=x+y
subtract_result=x-y
division_result=x/y
# ** used for power 

"""print(sum_result)
print(subtract_result)
print(division_result)"""

print(sum_result,subtract_result,division_result)#reults 
# ctrl+j (to open the terminal)
# ctrl+? (to comment out)

# for comment multiple line dobble cout 2 times is documentation .("""")

#special charactere are not used in the operations 

#types of error (bug)
# 1- synatx error   2- Logicsl error (mistake in logic)
# to solve the eroor is called (debugging)


# Difference between modulous (%) and Division (/)
 
 #division (is the qoutient in division.)
division_result=x/y
print(division_result) #result is 4.5  for checking  dividing the 45 by 10 qoutient is 4.5.
#Modulous (is the remainder of the division it's the part of the division method.)
modulous_result=x%y
print(modulous_result) #result is 5 for checking 45 divided by 10 is remainder is 5 
           # End in Nexskills 
#=======================================================================================================================================
           #Start in Harvard University course python 
#acctual print having values 
"""print(*operator,sep='',end='/n')
*operator #means it having various number of strings 
sep=''     #it means separating the values 
end=''     #it means it will not goes to new line . 
end='/n'   #it means it will goes to new line.
"""
#it's an example of print 
"""
print("Hello", end='')
print("World")
"""
#formate of string is 
"""
name=input("What's your name bro?")
print(f"Hello , {name}")# f is the formate of the string which we enter.
"""
# removing space from right and left on the run time on powershell 
"""
name=input("What's your name?")
name=name.strip() # remove the space on the run time on powershell 
print(f"Hello , {name}")
"""
# for capitalizing the entered name we use 
"""
name=input("What's your name buddy?")
name=name.capitalize() #this is used for Capitalize the first value 
print(f"Hey,{name}")
"""
# for capitalizing the first letter  for each word which entered
"""
name=input("Assalam-o-alaikum! Bhai name Kia hy ap ka ?")
name=name.title() #it's use for capatilizing
print(f"Kya hal hy bhai,{name}")
"""
# for making round in float
"""
x=float(input("What's the value of x "))
y=float(input("What's the value of y "))
z=round(x/y , 2) # it means it will round of at least 2 decimal e.g 0.67
print(f"{z}")
print(f"{z:.2f}") # it also means it will round at least 2 decimal e.g 0.67
"""
# make a Function 
"""
def hello(to):  # it's a keyword def for making the function and the argument in the function is "to" is used for specifying.
    print("hello",to)

name=input("What's your name? ")
hello(name)
"""
# Nested Function
"""
def main():
    name=input("Enter your name:")
    hello(name)
def hello(to="World"):
    print("hello",to)

main()
"""
# Use of return 
"""
def main():
    x=int(input("What's the value of x "))
    print("x Square is ",suqare(x))
def suqare(n):
    #return n*n
    return pow(n,2)# power of the value
main()
"""
# Recursion or Factorial
""" 
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
result=factorial(3)
print(result)
"""
# return value  
"""
def greeting(input):
    if "hello" in input:
     return "Hey , How are you !"
    else:
       return "Bro It doesn't contain hello in the sentence"
    
Greet=greeting("hello, computer !")
print(Greet)
       """

# Side effect 
"""
emoticon="v.v" # it means sad 
def main():
    global emoticon # it means the out side emoticon is global and now it will access and also modify
    #using global keyword 
    say("Hey, there is someone ?")
    emoticon=":D"
    say("Oh hello") # here the say function is used for input or also to return the value .
def say(phrase):
    print(phrase +""+emoticon)

main()
"""
# using string method 

# for capitalizing the fist alphabet in the string 

Shows=[
    "Ali",
           " Uzair ",
        "    Osman",
                  "  Saad",
                "            Sajid"
                
]
"""
def main():
    for show in Shows:
        print(show.capitalize()) 
main()
"""
#for captalizing 
"""
def main():
    for show in Shows:
        print(show.title())
main()
"""

# for removing space
"""
def main():
    for show in Shows:
        print(show.strip())
main()
"""
#for applying multiple method on list 
"""
def main():
    for show in Shows:
        print(show.strip().title())
main()
"""
# For adding in to the new list 
"""
def main():
    cleaned_show=[]
    for show in Shows:
         cleaned_show.append(show.strip().title())
         print(cleaned_show)
main()
"""
# for making a join 
"""
def main():
    clean_show=[]
    for show in Shows:
        clean_show.append(show.strip().title())
        print(" ".join(clean_show))
main()
"""
# Recommendation:
 
def main():
    difficulty=input("Enter a Game do you like Casual or Difficulty ")
    player=input("Enter which you want to play like Single player or Multiplayer ")
    if difficulty=="Difficult":
        if player=="Single player":
            print("Clock")
        else:
          print("PUBG")
    elif difficulty=="Medium":
        if player=="One player":
            print("GTA")
        else:
            print("Chess")
    else:
        if player=="Single":
            print("Heart")
        else:
            print("Free-Fire")

def recommendation(game):
    print("recomended game for you :D ", game)

main()