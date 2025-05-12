# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))
characters = list('Hello')
nums = [*range(1, 11)]

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros = [0] * 10


# for
nums = []
for i in range(1, 11):
	nums.append(i)

print(nums)


# for
zeros2 = []
for _ in range(10):
	zeros2.append(0)

print(zeros2)

# list comprehension
nums2 = [i for i in range(1, 11)]

print(nums2)


# list comprehension
zeros3 = [0 for _ in range(10)]

print(zeros3)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
