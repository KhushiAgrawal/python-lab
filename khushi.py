L=[]
while 1:
     item = input ('Enter the Item')
     L.append(item)
     n=input("DO you Want continue Y/N")
     if n.lower()=='n':
       break
L.sort(reverse=True,key=len)
print(L)                                                                                                                                                                                                                           
