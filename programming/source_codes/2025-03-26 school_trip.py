#students scool trip
year_cost = [12,10,7,5]

trip_cost = int(input("total trip cost? "))

proportions = input("proportions (CSV format): ") #string

num_students = int(input("total number of students: "))

#print(f"proportions as string {proportions}")
proportionsSL = proportions.split(",") #list of trings
#print(f"proportions as list of strings {proportionsSL}")
proportionsFL = [] #lilst of floats
for i in range(len(proportionsSL)):
    proportionsFL.append(float(proportionsSL[i]))
    
#print(f"proportions as list of float {proportionsFL}")

# if sum(proportionsFL) != 1:
#     print(f"Wrong proportions, their sum is {sum(proportionsFL)}")
#     exit()

students_per_year = []
for p in proportionsFL:
    students_per_year.append(int(p*num_students))

print(f"{students_per_year} total={sum(students_per_year)}")

spare = num_students - sum(students_per_year)
print(f"spare students (rounding) = {spare}")

#adding the spare students to the biggest group
biggest_group = max(students_per_year)
where = students_per_year.index(biggest_group)
students_per_year[where] += spare
print(f"{students_per_year} updated")
 
total = 0
for i in range(len(students_per_year)):
    total = total + students_per_year[i] * year_cost[i]
raised = total /2
if raised >= trip_cost:
    print(f"YES we raised {raised}")
else:
    print(f"NO we raised {raised}")
