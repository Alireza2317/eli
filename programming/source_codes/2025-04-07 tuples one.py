#first usage of tuples

def intersect(t1,t2):
    """ coputes the intersection of two tuples
    (i.e. common elements to both)"""
    result = ()
    for e in t1:
        if e in t2:
            result = result + (e,)
    return result

t = (1,"a",3,2.6,"z")
t1 = ("s",1,"3","z",2)

print(len(intersect(t,t1)))
print(intersect(t,t1))

