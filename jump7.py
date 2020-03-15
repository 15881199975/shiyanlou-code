for n in range(1, 101):
	if n % 7 == 0 or (70 <= n <= 79) or n % 10 == 7:
		continue
	print(n)
