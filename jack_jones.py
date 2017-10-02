
def sum_prime(number):
	if number == 1:
		return []

	for i in xrange(2, number):
        # Get remainder and quotient
		rd, qt = divmod(number, i)
		if not qt: # if equal to zero
			return [i] + sum_prime(rd)

	return [number]
def digit_sum(x):
	# a=map(str,x)
	d1=sum(map(int, str(x)))
	return d1
t=int(raw_input())
while(t>0):
	sum2=0
	l,r=map(int,raw_input().split())
	for i in range(l,r+1):
		s1=sum_prime(i)
		s3=list(set(s1))
		counter=sum(s3)
		s2=digit_sum(counter)
		sum2=sum2+s2
	print(sum2)
	t=t-1