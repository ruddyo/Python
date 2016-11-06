def swap(list1, first, second):
	# first = list[0]
	# second = list[1]
	temp = first
	list1[0] = second
	list1[1] = temp



def srt(lst):
	temp = 1
	for x in lst:
		# print x, x
		for k in xrange(temp,len(lst)):
			print lst
			if x>lst[k]:
				swap(lst, x, lst[k])
				print lst
		temp = temp+1


l = [15,14, 13]
# print l
srt(l)
# swap(l, 15, 14)
# print l