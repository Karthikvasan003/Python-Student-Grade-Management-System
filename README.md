Student Grade Management System

A simple Python-based system to manage student records, subjects, scores, and grades. This project demonstrates object-oriented programming principles like encapsulation, data validation, and modular design.



## Features

- Add students with multiple subjects and scores
- Automatically assign unique student IDs
- Calculate average score and assign grade (A–F)
- View detailed student reports
- Update subject scores
- Delete student records
- List all students with or without details




## Grades are assigned based on the average score:

| Average Score | Grade |
|---------------|-------|
| 90–100        | A     |
| 80–89         | B     |
| 70–79         | C     |
| 60–69         | D     |
| Below 60      | F     |



SAMPLE INPUT

grade.add_student("John Doe", {"Math": 85, "Science": 90, "English": 78})
grade.add_student("Jane Smith", {"Math": 92, "Science": 88, "English": 95})
grade.add_student("Alice Johnson", {"Math": 75, "Science": 80, "English": 70})

grade.update_scores(1, "Math", 95)  # Updates John Doe's Math score from 85 to 95


SAMPLE OUTPUT

## Individual Report for Student ID 1 (John Doe)
Report For Student ID: 1, Name: John Doe
Math: 95
Science: 90
English: 78
Average: 87.67, Grade: B


## List OF Students
ID: 1, Name: John Doe
ID: 2, Name: Jane Smith
ID: 3, Name: Alice Johnson


## Detailed Students Report
Student ID: 1, Name: John Doe
  Math: 95
  Science: 90
  English: 78
  Average: 87.67, Grade: B

Student ID: 2, Name: Jane Smith
  Math: 92
  Science: 88
  English: 95
  Average: 91.67, Grade: A

Student ID: 3, Name: Alice Johnson
  Math: 75
  Science: 80
  English: 70
  Average: 75.0, Grade: C
