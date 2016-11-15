def binaryS(f):
	l = [1,2,4,5,6,7,8,9,10,11,12,13]
	midpos = len(l)/2

	found = False
	first = l[0]
	last = l[-1]
	print last
	print midpos

	if len(l)==0:
		print False

	if l[midpos]==f:
		print True

	while first<=last and not found:
		if f>l[midpos]:
			first = l[midpos]+1
			print first
			found = True
			print found

	

		


binaryS(1)
# from turtle import Turtle
# t=Turtle()
# for x in xrange(440):
# 	t.forward(5)
# 	t.left(10)
# 	# t.right(20)