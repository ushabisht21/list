a=[2,8,9,4,5]
i=1
b=[]
x=0
while i<len(a):
    c=a[i]-a[x]
    b.append(c)
    i=i+1
    x=x+1
print(b)  