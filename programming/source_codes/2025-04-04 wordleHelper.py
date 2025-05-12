#helper for wordle solutions
from sys import argv


def check_green(word, green):
    """function to check green:
    returns true if w has the correct chars in the correct positions"""
    for i in range(len(green)):
        if green[i] == "?":
            continue
        elif word[i] == green[i]:
            continue
        else: return False
    return True
    
    
def check_yellow(word, yellow):
    """function to check yellow:
    returns true if w contains all the yellow chars"""
    for c in yellow:
        if c not in word:
            return False
    return True


def check_black(word, black):
    """function to check black:
    returns true if w does not contains any black char"""
    for c in black:
        if c in word:
            return False
    return True


def check_yellow_position(w, yellow_position):
    """function to check yellow position:
    returns true if w contains all the yellows chars in a different position"""
    for y in yellow_position:
        for i in range(len(w)):
            if y[i] == w[i]:
                return False
    return True


#take input
green = argv[1]
yellow = argv[2]
black = argv[3]
yellow_position = argv[4:]
# for i in range(4,len(argv)):
#     yellow_position.append(argv[i])

result = []

#open file
words_file = open("words.txt", 'r') 

#check constraints
for line in words_file:               #reads the file just once
    l = line.strip()
    if not check_green(l, green):     #the greens are not in the right positions or are absent
        continue
    elif not check_yellow(l, yellow): #all the yellow are not present
        continue
    elif not check_black(l, black):   #contains one or more black chars
        continue
    elif not check_yellow_position(l, yellow_position):  #the yellows are in known wrong position
        continue
    else:
        result.append(l)              #all the previous are satisfied

print(result)

#close the file
words_file.close()                    #all the word that are compatible with the constraints