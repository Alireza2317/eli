#prints Pitagora's table - hugly looking

s = ""
for row in range(1,11):
    for col in range(1,11):
        s = s + str(row*col) +" "
    print(s)
    s = ""
    
