#solving teh actions figures problem

#1.1 reading the content of the n boxes
def read_boxes(n):
    '''
    reads n lines,CSV, each one:
        first element the number of action figures
        followings the height of them
    '''
    boxes = []
    for i in range(n):
        box = input("insert the CSV for the box: ").split(',')
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i]) #converting all the string elements in int elementss
        boxes.append(box)
    return boxes

#2.1 check if the actions figures inside the box b are in order
def box_ok(b):
    '''
    compare the order of the action figuers in the box
    '''
    for i in range(len(b)-1):
        if b[i] > b[i+1]:
            return False
    return True
    
#2 check the ordering inside each box
def all_boxes_ok(boxes):
    '''
    returns true if each box contains ordered action figures
    '''
    for b in boxes:
        if not box_ok(b):
            return False
    return True

#3.
def boxes_endpoints(boxes):
    '''
    delete all the middle values of the boxes
    '''
    ep = []
    for b in boxes:
        ep.append([b[0],b[-1]])
    return ep

#5.
def all_endpoins_ok(endpoints):
    for i in range(len(endpoints)-1):
        if endpoints[i][1] > endpoints[i+1][0]:
            return False
    return True
    

#=======================================
#main
#1. read input (what data structure?)
n = int(input("insert the number of boxes: "))
boxes = read_boxes(n)

#2. check each box
if not all_boxes_ok(boxes):
    print("NO")
else:
    #3. compute a new list with only left and right heights
    endpoints = boxes_endpoints(boxes)
    
    #4. sort the boxes
    endpoints.sort()
    
    #5. check if the boxes are well organized
    if all_endpoins_ok(endpoints):
        print('YES')
    else:
        print('NO')
    
    
    