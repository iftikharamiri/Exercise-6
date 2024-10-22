"""
Task nr 1
University system simulation
"""
#%%
class Person:
    def __init__(self, name, age, email) -> None:
        self._name = name
        self._age = age
        self._email = email

    def get_details(self):
        print(f"Name: {self._name}, Age: {self._age}, Email: {self._email} ")
    

class Student(Person):
    def __init__(self, name, age, email, student_id) -> None:
       
        super().__init__(name, age, email)
        self._student_id = student_id
        self._courses = []
        self._grades = {}

    def receive_grade(self, course, grade): 
        self._grades[course] = grade

    def get_grades(self):
        return self._grades
    
    def __repr__(self):
        return f"Student: {self._name}, Grades: {self._grades}"


    def enroll_in_course(self, course):
        self._courses.append(course)

    def  get_courses(self):
        return self._courses

    def get_details(self):
        return super().get_details()


class Teacher(Person):
    def __init__(self, name, age, email, subject) -> None:
        super().__init__(name, age, email)
        self._subject = subject

    def assign_grade(self, student, course, grade):
        if isinstance(student, Student):
            student.receive_grade(course, grade)



class Course:
    def __init__(self, course_name, course_code) -> None:
        self._course_name = course_name
        self._course_code = course_code
        self._enrolled_students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self._enrolled_students.append(student)
            student.enroll_in_course(self._course_name)
        else:
            pass
        
    def list_students(self):
        print(f"Course name: {self._course_name} Course code: {self._course_code}")
        print(f"Enrolled students:")
        for student in self._enrolled_students:
            student.get_details()
    def __repr__(self):
        return f"{self._course_name} Code: {self._course_code}"


        
course = Course("Mathematikk 113", "MATH113")
teacher  = Teacher("jon", 22, "gg@nmbu.no", "math113")
student1 = Student("ifti", 22, "ifti@nmbu", 3445)
student2 = Student("Henriette", 21, "olsen@nmbu", 1111)

course.add_student(student1)
course.add_student(student2)
teacher.assign_grade(student1,course, grade= "B")
teacher.assign_grade(student2, course, grade= "A")

course.list_students()
print(student1.get_grades())

#student2.get_grades()
#student1.get_courses()

# %%
