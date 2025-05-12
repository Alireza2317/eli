#bakery bonus problem
i = input("number of franchise,number of days: ").split(",")
franchise = int(i[0])
days = int(i[1])

table = []

#insert values to the table
for d in range(days):
    row = input(f"sales for franchises for day {d+1}: ").split(",")
    for f in range(len(row)):
        row[f] = int(row[f])
    table.append(row)
print(table)

bonus = 0

# bonus overall frachises
for r in table:
    total = sum(row)
    if total % 13 == 0:
        bonus += total // 13

# bonus overall days for each franchise
for col_index in range(franchise):
    total = 0
    for row_index in range(days):
        total += table[row_index][col_index]
    if total % 13 == 0:
        bonus += total // 13
        
print(f"the toal bonusses are: {bonus}")

'''test:
3,2
4,5,4
9,8,9

=> 6
'''