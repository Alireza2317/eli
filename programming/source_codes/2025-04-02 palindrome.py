#recursive function to check palindrome

def pal(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return pal(s[1:-1])
        
    
def pal2(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and pal2(s[1:-1])

s = input("insert the string: ")
print(pal(s))
print(pal2(s))
