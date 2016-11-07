def swap(list1, first, second):
	# first = list[0]
	# second = list[1]
	temp = first
	list1[0] = second
	list1[1] = temp



def srt(lst):
	
	# print temp
	for x in range(len(lst)-1):
		temp = 1
		
		for k in range(0,len(lst)):

			print lst[x]>=lst[k]
			print lst[x],lst[k]
			print lst
			if lst[x]>=lst[k]:
				k1=lst[x]
				lst[x]=lst[k]
				lst[k]=k1
				
			temp=temp+1
			# temp = temp+1
		


l = [15,14,4,13]
# print l
srt(l)
# swap(l, 15, 14)
print l