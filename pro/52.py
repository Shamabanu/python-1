def square():
	min=999
	(r,l)=([],[])
	for i in range(4):
		for j in range(2):
			l.append(int(input()))
		r.append(l)
		for m in l:
			if min>m:
				min=m
		l=[]
	f=1
	for i in range(len(r)):
		dif=r[i][0]-r[i][1]
		if dif in(0,-min,min):
			continue
		else :
			f=0
			break
	if f!=0:
		print('yes')
	else :
		print('no')
try:
	square()
except:
	print('invalid')
  p
