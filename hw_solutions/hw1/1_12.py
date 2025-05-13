point_a = (4, 0)
point_b = (0, -5)

slope = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])

# y - ya = m(x - xa) => y = mx + (ya - mxa)
y_intercept = point_a[1] - slope*point_a[0]

if y_intercept > 0:
	print(f'y = {slope:.2f}x + {y_intercept}')
elif y_intercept < 0:
	print(f'y = {slope:.2f}x - {-y_intercept}')
else:
	print(f'y = {slope:.2f}x')