n=int(input('enter the element in list 1'))
l1=[]
for i in range(0,n+1):
	l1.append(i)
k=int(input('enter the element in list 1'))
l2=[]
for i in range(0,k+1):
	l2.append(i)
l=[i for i in l1 if i in l2]
print(l)
