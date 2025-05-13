A = 'aaabbb'
B = 'cccdddeee'

A_triplets = []
i = 0
while i < len(A):
	A_triplets.append(A[i:i+3])
	i += 3

B_triplets = []
i = 0
while i < len(B):
	B_triplets.append(B[i:i+3])
	i += 3

print(A_triplets)
print(B_triplets)

output = ''
for i in range(min(len(A_triplets), len(B_triplets))):
	output += A_triplets[i] + B_triplets[i]

if len(A_triplets) > len(B_triplets):
	output += ''.join(A_triplets[len(B_triplets):])
else:
	output += ''.join(B_triplets[len(A_triplets):])

print(output)