#read a csv line and summs the number

s = input("insert a CSV line: ")

s_sub = ""
total = 0

for c in s:
    if c != ",": #c is a digit
        s_sub = s_sub + c
    else: #c is a comma
        total += int(s_sub)
        s_sub = ""
total += int(s_sub)
print(total)