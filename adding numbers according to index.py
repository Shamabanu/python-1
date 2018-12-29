n,q=input().split()
n=int(n)
q=int(q)
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
for j in range(q):
    c=0
    u,v=input().split()
    u=int(u)
    v=int(v)
    for i in range(u,v):
        c=c+int(l1[i])
    print(c)
