# the slot machine program
#
quarters = int(input("insert the Martha's number of coins: "))
first = int(input("insert the status of first machine [1-35]: "))
second = int(input("insert the status of second machine [1-100]: "))
third = int(input("insert the status of third machine [1-10]: "))

plays = 0 #the numbers of plays of Martha to be printed at the end
machine = 1

while quarters >= 1:
    quarters -= 1
    machine = plays % 3 + 1
    
    if machine == 1:       #Martha plays machine 1
        first += 1
        if first == 35:    #Martha wins some conins
            quarters += 30
            first = 0
    elif machine == 2:     #Martha plays machine 2
        second += 1
        if second == 100:
            quarters += 60 #Martha wins some conins
            second = 0
    elif machine == 3:     #Martha plays machine 3
        third += 1
        if third == 10:
            quarters += 9  #Martha wins some conins
            third = 0
    plays += 1

print(f"Martha played {plays} times before ending the quarters")
