#pitagora's table beautified

table = 10
s = ""

for row in range (1,table+1):
    for col in range (1,table+1):
        num_str = str(row * col)
        fix_str = "     " + num_str
        fix_str = fix_str[-5:]
        s = s + fix_str
    print(s)
    s = ""


