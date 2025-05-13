primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# indexes 0, 1, 2, 3,  4,  5,  6,  7,  8
#         -9 -8 -7 -6  -5  -4  -3  -2 -1
print(primes[8])
#indexing with [], 0 corresponds to first item, ...

print(primes[-1])
#negative index starts from the end


#slicing , similar to indexing, but retruns a list from for example second Item to 4th
#primes[1:4]
#print(primes[:3])
# from index 0 (first element) to index 2(third element)
#print(primes[3:])
# from index 3(4th elemnt) to the last element
#print(primes[0:4])
# from index 0(1st elemnt) to index 3(4th ele)
#print(primes[:])
# the whole list(as a 'copy')

#print(primes[2:-2])
# from index 2(3rd element) to index -3(3rd element from the end)
# ignores two elements from both ends
# like range there can be a third part, stepping (self_explanatory:)), like this >
#primes[0::2] > from index 0 to last, stepping 2 by 2
#print(primes[::-1])
# reverses the list
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

print(primes[-2:0:-1])
#[19, 17, 13, 11, 7, 5, 3]
#if the stepping is positive the first part should be smaller than the other one
#if the stepping is negative, the first one should be smaller than the other one
#despite the signe of stepping always the first one is included and the second one
# is not
print(primes[-1:-4:-2])
#[23, 17]

print('Hello there.'[::-1])







