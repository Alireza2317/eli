A = 's:213 m:28;s:78 m:16;s:765 m:19;'

students_info = A.removesuffix(';').split(';')

ids = []
marks = []

for info in students_info:
	student_id = info.split()[0].split(':')[1]
	student_mark = info.split()[1].split(':')[1]

	ids.append(student_id)
	marks.append(student_mark)

best_id = 0
worst_id = 0

best_mark = 0
worst_mark = 101

for ID, mark in zip(ids, marks):
	if int(mark) < worst_mark:
		worst_mark = int(mark)
		worst_id = ID

	if int(mark) > best_mark:
		best_mark = int(mark)
		best_id = ID


print(f'Best student -> ID: {best_id} Mark: {best_mark}')
print(f'Worst student -> ID: {worst_id} Mark: {worst_mark}')