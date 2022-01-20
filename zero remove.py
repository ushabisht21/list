a=[2,0,3,0,4,0,4,0,5,0]
i=0
k=[]
while i<len(a):
    if a[i]!=0:
        k.append(a[i])
    i=i+1
print(k)