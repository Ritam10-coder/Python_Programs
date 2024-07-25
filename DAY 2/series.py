def nthTerm(n) :

	if n <= 1 :
		return 1

	fact = 1
	for i in range(1, N) :
		fact = fact * i

	return fact
if __name__ == "__main__" :
     N = 14
print(nthTerm(N))


