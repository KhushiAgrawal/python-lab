k=list(map(int,input().split()))
b=[]
for i in k:
	if i not in b:
		b.append(i)
for i in b:
	print(i,end=' ')
p=len(b)
for i in range(0,p):
	print(b[i],end='**')
