def note(L,x):
    print(f"enter note, \tid(L)  = {id(L)}, \tid(x) = {id(x)}")
    x += 1
    L.pop(0)
    print(f"exit  note, \tid(L)  = {id(L)}, \tid(x) = {id(x)}")
    return

L1 = [1,2,3,4]
a = 1000
print(f"before note, \tid(L1) = {id(L1)}, \tid(a) = {id(a)}")
note(L1,a)
print(f"afterf note, \tid(L1) = {id(L1)}, \tid(a) = {id(a)}")

print(f"L1 = {L1}")
print(f"a = {a}")
