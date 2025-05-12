#list subtraction

def intReadList(l):
    '''
    reads a list of integers in list l
    the list has unknown length
    returns by side effect 
    '''
    e = input("insert an integer [enter] to stop: ")
    while e:
        l.append(int(e))
        e = input("insert an integer {return] to stop: ")

def subtractList(l1,l2):
    '''
    deletes from l1 all the elements of l2
    works by side effects
    '''
    for e in l2:
        if e in l1:
            l1.remove(e)
    
    

l = []
s = []
intReadList(l)
intReadList(s)
subtractList(l,s)
print(l)
