#   What relationship is appropriate for Student and Person?

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Major: {self.major}")

# Creating instances
person1 = Person("Alice", 25, "Female")
person1.display_info()

student1 = Student("Bob", 20, "Male", "S12345", "Computer Science")
student1.display_info()
