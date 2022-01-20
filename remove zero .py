a=[2,3,4,0,5,6,67,7,0,0,0,0]
i=0
k=[]
while i<len(a):
    if a[i] !=0:
        k.append(a[i])
    i=i+1
print(k)