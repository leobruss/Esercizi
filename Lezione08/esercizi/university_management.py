#Exercise 4: University Management System
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self) -> str:
        return super().__str__()
    
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = None

    def __str__(self):
        return f"Course: {self.course_name} ({self.course_code})"
    

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if not isinstance(course, Course):
            raise TypeError("Expected a Course instance")
        if course not in self.courses:
            self.courses.append(course)
            course.students.append(self)
        else:
            print(f"Student {self.name} is already enrolled in {course.course_name}")

    def get_role(self):
        return "Student"

    def __str__(self):
        courses_str = ", ".join([course.course_name for course in self.courses])
        return f"{super().__str__()}, ID: {self.student_id}, Courses: {courses_str}"
    
class Professor(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses = []

    def assign_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("Expected a Course instance")
        if course not in self.courses:
            self.courses.append(course)
            course.professor = self
        else:
            print(f"Professor {self.name} is already assigned to {course.course_name}")

    def get_role(self):
        return "Professor"

    def __str__(self):
        courses_str = ", ".join([course.course_name for course in self.courses])
        return f"{super().__str__()}, Employee ID: {self.employee_id}, Courses: {courses_str}"
        
# Create course instances
course1 = Course("Math 101", "MATH101")
course2 = Course("History 101", "HIST101")

# Create a student instance
student = Student("John Doe", 20, "S12345")

# Create a professor instance
professor = Professor("Dr. Smith", 45, "P67890")

# Enroll the student in courses
student.enroll(course1)
student.enroll(course2)

# Assign courses to the professor
professor.assign_course(course1)
professor.assign_course(course2)

# Print student and professor information
print(student)
print(professor)

# Print course details
print(course1)
print(course2)