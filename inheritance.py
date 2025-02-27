class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print(f"{self.name} is walking")
    
    def talk(self):
        print(f"{self.name} is talking")
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # super keyword is used for parent class inheritance 
        self.student_id = student_id
    
    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

def main():
    person = Person("Ali",20)
    student = Student("Ahmad", 20, "S123")
    
    print("Person Details:")
    person.display()
    person.walk()
    person.talk()
    
    print("\nStudent Details:")
    student.display()
    student.walk()
    student.talk()

if __name__ == "__main__":
    main()
