#string scanning, works for any sequence
s = "abcse"

for c in s: #scan by value
    print(c)
    
print(20*"-")
for i in range(len(s)): #scan by index
    print(s[i])