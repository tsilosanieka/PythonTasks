#Student Class
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        average = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {average:.2f}"

#Classroom Class
class Classroom:
    def __init__(self):
        self.students = []  # Initialize an empty list to hold Student objects

    def add_student(self, student):
        self.students.append(student)

    def get_top_students(self):
        sorted_students = sorted(
            self.students,
            key=lambda student: student.get_average_grade(),
            reverse=True
        )
        return sorted_students[:3]

    def get_failed_students(self):
        return [student for student in self.students
                if student.get_average_grade() < 51]

#Implement the Solution (Example Usage)

#Create a Classroom
my_classroom = Classroom()

#Create Student objects
student_alice = Student("Alice")
student_bob = Student("Bob")
student_charlie = Student("Charlie")
student_david = Student("David")
student_eve = Student("Eve")

#Add grades to each student
student_alice.add_grade(92)
student_alice.add_grade(88)
student_alice.add_grade(95)

student_bob.add_grade(78)
student_bob.add_grade(82)
student_bob.add_grade(80)

student_charlie.add_grade(95)
student_charlie.add_grade(100)
student_charlie.add_grade(98)

student_david.add_grade(40)
student_david.add_grade(50)
student_david.add_grade(35)

student_eve.add_grade(85)
student_eve.add_grade(88)
student_eve.add_grade(90)

#Add students to the classroom
my_classroom.add_student(student_alice)
my_classroom.add_student(student_bob)
my_classroom.add_student(student_charlie)
my_classroom.add_student(student_david)
my_classroom.add_student(student_eve)

#Use the Classroom methods to get results
print("Top 3 Students")
top_students = my_classroom.get_top_students()
for s in top_students:
    print(s)

print("\nFailed Students (Score < 51)")
failed_students = my_classroom.get_failed_students()
for s in failed_students:
    print(s)