from random import randint

class Student:
	def __init__(self, name, surname, ID, passed_courses):
		self.name = name.title()
		self.surname = surname.title()
		self.ID = ID
		self.passed_courses = passed_courses


	def try_exam(self, course):
		exam_grade = randint(1, 30)
		if exam_grade >= 18:
			self.passed_courses.append(course)


	def show_details(self):
		print(f'Student ID: {self.ID}, name: {self.name} {self.surname}')


	def __repr__(self):
		return f'{self.name} {self.surname}'


class Course:
	def __init__(self, name, code, year, professor):
		self.name = name
		self.code = code
		self.year = year
		self.professor = professor

	def __repr__(self):
		return f'{self.name}'


def get_students_passed(list_of_students, course):
	students = []
	for student in list_of_students:
		if course in student.passed_courses:
			students.append(student)

	return students


physics = Course('Physics', '92', '2025', 'prof_physics')
bilogy = Course('Bilogy', '17', '2024', 'prof_biology')
math = Course('Math', '23', '2025', 'prof_math')
programming = Course('Programming', '73', '2025', 'prof_programming')


students = [
	Student('jack', 'jackson', '123', [physics, math]),
	Student('john', 'johnson', '893', [bilogy, programming]),
	Student('mark', 'markson', '156', [physics, math, programming]),
	Student('jacob', 'jacobson', '235', [physics, math, bilogy, programming]),
	Student('peter', 'peterson', '190', [programming]),
]

students[0].show_details()
print(students[0].passed_courses)

students[0].try_exam(programming)

print(students[0].passed_courses)


print(get_students_passed(students, math))