n = input("insert the phone number (4 digit): ")

if (n[0] == '9' or n[0] == '8') and (n[-1] == '9' or n[-1] == '8') and (n[1] == n[2]):
        
    print("do not answer")
else:
    print('answer')