class Student:
    id_counter = 1
    def __init__(self, name):
        self.id = Student.id_counter
        Student.id_counter += 1
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        if subject not in self.subjects:
            if score >=0 and score <= 100:
                self.subjects[subject] = score
            else:
                raise ValueError("Score must be between 0 and 100")
        else :
            raise ValueError("Subject already exists")


    def calculate_average(self):
        if self.subjects:
            return round(sum(self.subjects.values()) / len(self.subjects), 2)
        else:
            return 0
    
        
    def get_grade(self):
        avg = self.calculate_average()
        if avg>= 90:
            return "A"
        elif avg>=80:
            return "B"
        elif avg>=70:
            return "C"
        elif avg>=60:
            return "D"
        else :
            return "F"
    

class GradeManager :
    def __init__(self):
        self.students = []

    def add_student(self, name, subjects): 
        student = Student(name)
        for subject, score in subjects.items():
            student.add_subject(subject, score)
        self.students.append(student)

        
    def list_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")

    def list_students_with_details(self):
        if not self.students:
            print("No students available.")
            return

        for student in self.students:
            print(f"\nStudent ID: {student.id}, Name: {student.name}")
            for subject, score in student.subjects.items():
                print(f"  {subject}: {score}")
            print(f"  Average: {student.calculate_average()}, Grade: {student.get_grade()}")



    def update_scores(self, id, subject, score) :
        student = self.find_student(id)
        if student:
            if subject not in student.subjects:
                raise ValueError("Subject does not exist")
            else :
                if score>=0 and score <=100:
                    student.subjects[subject] = score
                else:
                    raise ValueError("score must between 0 and 100")
        else :
            raise ValueError("Id not Found")

    
    def view_report(self, id) :
        student = self.find_student(id)
        if student :
            print(f"Report For Student ID: {student.id}, Name: {student.name}")
            for sub, score in student.subjects.items() :
                print(f"{sub}: {score}")
            print(f"Average: {student.calculate_average()}, Grade: {student.get_grade()}")
        else:
                raise ValueError("Id not Found")


    def delete_student(self, id):
        self.students = [s for s in self.students if s.id != id]

    def find_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

grade = GradeManager()
grade.add_student("John Doe", {"Math": 85, "Science": 90, "English": 78})
grade.add_student("Jane Smith", {"Math": 92, "Science": 88, "English": 95})
grade.add_student("Alice Johnson", {"Math": 75, "Science": 80, "English": 70})
grade.update_scores(1, "Math", 95)

grade.view_report(1)
grade.list_students()
grade.list_students_with_details()
