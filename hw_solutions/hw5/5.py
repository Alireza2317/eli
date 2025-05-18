#key -> (fiscal code,)
employees = {
	('126523493',): ('jack', 'johnson', 'oak st.', 'milan', 30),
	('999999999',): ('mark', 'thomson', 'maple st.', 'milan', 20),
	('777777777',): ('tom', 'smith', 'main st.', 'rome', 25)
}

#key -> (VAT code,)
companies = {
	('42',): ('Apple', 'milan'),
	('384',): ('Microsoft', 'rome')
}

#key -> (fiscal code, VAT code)
jobs = {
	('126523493', '42'): (2000),
	('999999999', '42'): (870),
	('777777777', '384'): (1600)
}

def sum_salaries_of_companies():
	salaries = {}

	for company_VAT in companies:
		s = 0
		for job, salary in jobs.items():
			if job[1] == company_VAT[0]:
				s += salary

		salaries[company_VAT[0]] = s

	return salaries


def get_salary(fiscal_code):
	total_salary = 0

	for job, salary in jobs.items():
		if job[0] == fiscal_code:
			total_salary += salary

	return total_salary


def employees_working_in(city_name):
	VATs = []
	for company_VAT, company_info in companies.items():
		if company_info[1] == city_name:
			VATs.append(company_VAT[0])

	fiscals_working_in_city = []
	for job in jobs:
		if job[1] in VATs:
			fiscals_working_in_city.append(job[0])

	employees_list = set()
	for employee, info in employees.items():
		if employee[0] in fiscals_working_in_city:
			employees_list.add(info)

	return employees_list

print(sum_salaries_of_companies())
print(get_salary('126523493'))
print(get_salary('999999999'))
print(get_salary('777777777'))
print(employees_working_in('rome'))
print(employees_working_in('milan'))