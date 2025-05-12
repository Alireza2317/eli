#compute the frequencies form the input

s = input("insert a string: ")

f = {}


for c in s:
    if c == " ":
        continue
    f[c] = f.get(c,0) + 1

#sort the dictionay by keys
keysList = list(f.keys())
keysList.sort()

for k in keysList:
    print(f"{k} : {f[k]}")

#sort the dictionary by values
#print(f)