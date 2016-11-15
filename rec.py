from random import randint

def parse():
	s=[]
	f = {(randint(0,9),randint(0,9)),
		(randint(0,9),randint(0,9)),
		(randint(0,9),randint(0,9)),
		(randint(0,9),randint(0,9)),
		}
	for i, o in f:
		s.append(i)
		s.append(o)
	return s


print parse()