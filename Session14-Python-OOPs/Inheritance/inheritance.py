class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def show_details(self):
        print("-------------------------------------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
# Student is Child of Person Class
# Parent name always comes after child name
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age) #passing name and age to parent class constructor
        self.student_id=student_id
    # method oevrriding    
    def show_details(self):
        super().show_details() #Reuse the method of parent class
        print(f"Student ID: {self.student_id}")
    def study():
        print("Study Going on")
        
s1= Student("Sonam",26,"S101") # object of Student class
s1.show_details() # calling parent class method
s1.study # calling own menthod

class Employee(Person):
    def __init__(self, name, age, emp_id,salary):
        super().__init__(name,age) #passing name and age to parent class constructor
        self.emp_id=emp_id
        self.salary=salary
    # method oevrriding    
    def show_details(self):
        super().show_details() #Reuse the method of parent class
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        

e1= Employee("Alex",46,"E101",46000) # object of Student class
e1.show_details() # calling parent class method

    
