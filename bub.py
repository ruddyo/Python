def sw(a,b):
	a, b = b, a
	return [a,b]


def bub(list):
	for a, a_val in enumerate(list):
		for b, b_val in enumerate(list):
			if a_val < b_val:
				list[a],list[b]=list[b],list[a]
				print list
	return list



print bub([1,5,3,2,4])