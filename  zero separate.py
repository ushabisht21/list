a=[2,0,4,0,5,0,6,7]
k=[]
j=[]
i=0
while i<len(a):
    if a[i]==0:
        k.append(a[i])
    if a[i]!=0:
        j.append (a[i])
    i=i+1
print(j+k)