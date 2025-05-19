import random
import string
# at least one Uppercase letter
# at least 2 digits
# at least one punctuation
# at least 16 characters

#print(random.randint(4, 9))
#print(random.sample([2, 3, 9, 17], 1))

A = random.sample((string.ascii_uppercase) , random.randint(1 , 4))
B = random.sample(string.digits, random.randint(1 , 4))
C = random.sample((string.punctuation), random.randint(1 , 4))
pass_len = random.randint(16 , 23)
x = pass_len - len(A) - len(B) - len(C)
D = random.sample(string.ascii_lowercase, x )

raw_pass = ''.join(A + B + C + D)
final_pass=''.join(random.sample(raw_pass , pass_len))
print(final_pass)
print (len(final_pass))

