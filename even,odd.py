list=[[2,3,4],[5,6,7,8],[10,12,13]]
i=0
even=[]
odd=[]
while i<len(list):
    if list[i]%2==0:
        even.append(list)[i]
        print(even)
    elif list[i]%2!=0:
        odd.append(list)[i]
        print(odd)
    i=i+1   






a=[2,4,6,5,7],[2,8,5,67,45,56],[2,56,34,43,89]
b=[]
c=[]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if (a[i][j])%2==0:
            b.append(a[i][j])
        else:
            c.append(a[i][j])
        j=j+1
    i=i+1
print(b)
print(c)       

