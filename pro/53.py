def checkpanag(str):
	l=[]
	for i in range(26):
		l.append(False)
	for s in str.lower():
		if s!=' ':
			l[ord(s)-ord('a')]=True
	for c in l:
		if c==False:
			return False
	return True
  
def main():
	s=input()
	print(checkpanag(s))
try:
	main()
except:
	print('invalid')
  p
