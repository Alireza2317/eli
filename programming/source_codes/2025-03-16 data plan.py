# data plan problem

monthly_offer = int(input("isert the amount of data per month by offer: "))
number_of_months = int(input("how many months to consider: "))

excess = 0

for m in range(number_of_months):
    actual = int(input(f"what is the usge for month {m+1}: "))
    excess = excess + monthly_offer - actual
print(f"you have {excess} data sitl available")