s1=input("Enter the 1st string:")
s2=input("Enter the 2nd string:")
s=list(s1)
flag=0
for x in range(len(s)-2):
	for y in range(len(s),x,-1):
		ans=''
		for z in range(x,y):
			ans=ans+s[z]
		if ans==s2:
			flag=1
			break
if flag==1:
	print("Yes")
else:
	print("No")
p
p
