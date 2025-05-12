#pitagora's table beautified

table = 10


for r in range (1,table+1):
    for c in range (1,table+1):
        num_str = str(r * c)
        fix_str = "     " + num_str
        fix_str = fix_str[-5:]
        print(fix_str, end="")
    print()


