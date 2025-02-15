#                           "Varibale & data Types"

#1. Declare three variables: an integer, a float, and a string. Print their types.
"""
integer=10
float=10.0
string="ali"
print(type(integer),type(float),type(string))
"""
#2. Convert a float num = 12.7 to an integer and a string. Print the results.
"""
num=12.7
integer=int(num)
string=str(num)
print("float number is " ,num,"and integer number ", integer ,"and a string is ", string )
"""
# 3-Convert x = '25' (a string) to an integer and a float. Print the results.
"""
x='25'
integer=int(x)
f_num=float(x)
print("the value of string is ", x, "and the converted the string in to integer is ", integer, "and the string converted to float is ", f_num)
"""
# 4. Check the datatype and mutability of given variables: a=10, b='Hello', c=3.14, etc








#5- Create a dictionary with variable names as keys and values as different datatypes.
"""
student={
    "String":"Hey guys!"
    ,"integer":15
    ,"float":3.85
    ,"list_student":["ali",21,"lahore"]
    ,"tuple_variable":(1,3,56,64)
    ,"boolean":True
    ,"None_value":None
    ,"dictinory":{"name":"ali","age":20}
}
print(student)
"""
#=========================================================================================================
#                                "List"

#1-Create a list of five fruits and print the second and last element.
"""
fruits=["Apple", "banana","grape","Watermellon","Orange"]
print("Second fruit is ",fruits[1])
print("last fruit is ",fruits[-1])# last index having -1 
"""
#  2. Add a fruit at the start and end of the list, then print it.
"""
fruit=["apple","banana","grape","orange"]
fruit.insert(0,"Stawberry")
fruit.append("cherry")
print(fruit)
"""
# 3. Remove the third element from the list and print it
"""
fruit=["apple","banana","grape","orange"]
fruit.pop(2)
print(fruit)
"""
# 4. Replace the second element in [10, 20, 30, 40, 50] with 25.
"""
num=[10,20,30,40,50]
num[1]=25
print(num)
"""
# 5. Concatenate two lists and print the result.
"""
num=[10,20,30,40,50]
num2=[60,70,80,90,100]
print(num+num2)
"""
# 6. Extract elements from index 1 to 4 using slicing.
"""
num=[10,20,30,40,50,60,70]
print(num[1:4:])
"""
# 7. Create a list with an integer, string, and float. Print each element's type.
"""
num=[10,"hey",10.0]
print(type(num[0]))
print(type(num[1]))
print(type(num[2]))
"""
#=============================================================================================================
#                                        "Tuples"

# 1. Create a tuple with five city names and print first and last element.
"""
city=("lahore","karachi","peshawar","Quetta","islamabad")
print(city[0])
print(city[-1])
"""
# 2. Try modifying a tuple element. Explain the error.
"""
city=("lahore","karachi")
city[1]="Islamabad"
print(city)
" it gave error message because tuple is immutable means unchangeable . It cannot be removed, add the variables ."
"""
#3-  Convert (10, 20, 30, 40, 50) into a list, modify an element, and convert back.
"""
num=(10,20,30,40,50)
num_list=list(num)
num_list[2]=34
num_tuple=tuple(num_list)
print(num_tuple)
"""
#4. Check if 'purple' exists in a tuple.
"""print("purple"in("yellow","blue","red","white","purple"))"""

#  5. Unpack ('Alice', 25, 'Doctor') into separate variables and print them.
"""
name,age,field=("Alice",25,"Doctor")
print(name)
print(age)
print(field)
"""
#  6. Create a mixed data type tuple and print types of each element
"""
num=("ali",25,3.86,{"age":20},[1,2,3,4],True)
print(type(num[0]))
print(type(num[1]))
print(type(num[2]))
print(type(num[3]))
print(type(num[4]))
print(type(num[5]))
print(type(num))
"""
#7. Count occurrences of 5 in (1, 5, 2, 5, 3, 5, 4, 5).
"""
number=(1,5,2,5,3,5,4,5)
count_num=number.count(5)
print(count_num)
"""
#========================================================================================================
#                                              "Dictionary"
#  1. Create a dictionary with country names as keys and capitals as values.
"""
country={
        "Pakistan":"Islamabad",
        "UK":"London",
        "India":"Delhi"
        ,"japan":"Tokyo"
}
print(country)
"""
#  2. Add a new key-value pair and print the updated dictionary.
"""
country={
    "Pakistan":"Islamabad",
    "UK":"London",
    "Japan":"Tokyo"
}
country["India"]="delhi"
print(country)
"""
# 3. Store student info (name, age, grade) in a dictionary and print the grade.
"""
Student={
    "name":"Ali"
    ,"age":21
    ,"grade":"A"

}
print(Student["grade"])
"""
# 4. Update the age in a student dictionary and print the result.
"""
Student={
    "name":"Ali"
    ,"age":21
    ,"grade":"A"
}
Student["age"]=22
print(Student)
"""
#  5. Create a phonebook dictionary and check if 'John' exists in it
"""
Phone_book={
    "Michel":342243454335
    ,"Jordge":45434535343
    ,"John":3435453534353
    ,"Osman":34353455646
}
print(Phone_book["John"])
"""
#  6. Remove a key from a dictionary and print the updated dictionary.
"""
phone_book={
    "Michel":342243432224,
    "Ali":34325346544354,
    "Osman":243544346345,
    "Talha":3543523425256345,
}
phone_book.pop("Michel")
print(phone_book)
"""
#  7. Store book info (title, author, year, price) and print the price
"""
store_book={
    "title":"C++"
    ,"author":"Horstmann"
    ,"year":2000
    ,"price":1290
}
print(store_book["price"])
"""
#  8. Convert a dictionary's keys into a list and print them
"""
student={
        "name":"ali"
        ,"age":20
        ,"Section":"4C1"
        ,"CGPA":3.85
}
convert_ls=list(student)
print(convert_ls)
"""
# 9. Merge two dictionaries into one and print it.
"""
student1={
    "name":"ali"
    ,"age":20
    ,"GPA":4
}
store_book={
     "title":"C++"
    ,"author":"Horstmann"
    ,"year":2000
    ,"price":1290
}
student= student1 | store_book # | is used for merging dictionary + operator cannot used for dic. or it also
#use merge keyword
print(student)
"""
#========================================================================================================================

#                                                   "Set , Theoratical Question"

# 1- what is set in python. And how it is different from list?
"Definition:"
"""In Python, a set is defined as an unordered collection of  objects. 
It can be expressed in the form of curly braces it also called delimeters {} or set() constructor."""
"Different from the list:"
"""1-Set is unorder collection .And list is order collection.
2-In set duplication is not allowed .but in list it is allowed.
3-In set indexing is not possible but in list it is possible.
4-Both set orr list are mutable."""

# 2- Explain the properties of sets in Python.
"""1- set is unorder collection of objects
2- set is mutable. it could be change the values , add the values.
3- In set indexing is not possible.
4- Set having Unique values. """

# 3-  What are the advantages of using a set over a list?
"""1- There is no duplication. It having unique elements 
2-It's more efficient to solve methimetical operation like union ,intersection.
3-set store unique elements so it's memeory efficient."""

#4- How do you remove duplicate elements from a list using a set?
"We can remove a duplication of elements in the list by converting a list in to a set."
"Example:"
"""numbers = [1, 2, 2, 3, 4, 4, 5]
without_Duplication_numbers = set(numbers)
print(without_Duplication_numbers)"""

#5- Explain the difference between union and intersection in sets with examples.
"Union:"
"In union it combines a set without dupication of elements."
"""Example:
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Using | operator
print(A.union(B))  # Using union() method"""

"Intersection:"
"In intersection takes a common value in the set"
"Example:"
"""
A={2,3,4,5,6,7}
B={3,7,8,9,6}
print(A & B)  # Using & operator
print(A.intersection(B))  # Using intersection() method
"""

#  6. What is a frozen set? How is it different from a normal set?
"""
Frozen set is immutable.
Set is mutable but frozenset is immutable .
Set used operation like add,remove.But Frozen set doesnot support any operation.
"""

#  7. Can a set contain duplicate elements? Why or why not?
"No, set having uniquee elements. When a duplicate values are inserted in the set it automatically remove."
"EXample:"
"""
num = {1, 2, 2, 3, 4, 4}
print(num)  # Output: {1, 2, 3, 4}
"""
#  8. Explain how sets handle unordered data. Provide an example.
"In set it store a data in unorder. The order may be change each time you print the value."
"Example:"
"""
num={10,20,30,40,50,60}
print(num)
"""
#================================================================================================================

#                                                 "Sets - Practical Questions"

#  1. Create a set with five unique numbers and print it.
"""
num={1,2,3,4,5,6}
print(num)
"""
# 2. Add an element to a set and remove an element from it. Print the result.
"""
num={4,5,6,7,8,9}
num.add(10)
num.remove(6)
print(num)
"""
#  3. Create two sets and perform union, intersection, and difference operations.
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union (combines both sets without duplicates)
union_set = set1 | set2  # OR set1.union(set2)
# Intersection (common elements in both sets)
intersection_set = set1 & set2  # 
# Difference (elements in set1 but not in set2)
difference_set = set1 - set2  
# Printing results
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
"""

#  4. Convert a list with duplicate values into a set and print the unique elements.
"""
list=[1,2,3,3,3,4,4,5,6,7,8,8,9,9,9,2]
convert_set=set(list)
print(convert_set)
"""

# 5. Check if a given element exists in a set and print an appropriate message.
"""
numbers = {1, 2, 3, 4, 5}
element = 3
print(element in numbers)
"""

#  6. Create a set of vowels and check if 'z' is present in the set or not.
vowels = {'a', 'e', 'i', 'o', 'u'}
print('z' in vowels)

# 7. Try adding a list as an element inside a set. What happens? Explain.
"""
set = {1, 2, 3}
set.add([4, 5, 6])  
print(set)
"""

# 8. Convert a set into a sorted list and print the result
"""
num = {5, 2, 8, 1, 4}
list = sorted(num)
print(list)
"""