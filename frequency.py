a=[4,6,4,3,3,4,3,4,3,8]
i=0
k=[]
while i<len(a):
    j=0
    n=[]
    count=0
    while j<len(a):
        if a[i] in a:
            if a[i]==a[j]:
                count=count+1
        j=j+1   
    n.append(a[i])
    n.append(count)
    if n not in  k:
        k.append(n)
    i=i+1
print(k)             